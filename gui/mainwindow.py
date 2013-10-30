#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#add folders to path for importing classes
import sys
sys.path.insert(0, '../API')
sys.path.insert(0, '../hl7parser')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_gui import Ui_MainWindow
from config import ConfigForm
from solo_monit import MonitForm
from monitordata import MyMonitor
from uiworking_thread import UiWorkingThread
from monitor_controller import MonitorController
from individual_controller import IndividualController

#Queue for managing processes
from Queue import Queue
#HL7 Parser
from hl7parser import patient, measure, channel, oru_wav, oru_wav_factory, patient_factory, obx
#Twisted API for server
from icucenterapi import ICUCenter, ICUServerFactory
#Twisted imports
from twisted.internet.task import LoopingCall
from threading import Lock


class MainWindow(QMainWindow):

	def __init__(self, qtreactor):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setTab(ConfigForm, self.ui.tabConfig, "configForm")
		self.setTab(MonitForm, self.ui.tabPacient, "monitForm")
		self.gridMonitores = QGridLayout(self.ui.widget)
		self.monitores = []
		#self.maxNumMonitors = 8
		#self.setMonitores()
		self.monitIds = {}
		self.iController = IndividualController(self.monitForm)
		self.iController.gui.alarmForm.connectAlarm(self)
		#self.wthread = UiWorkingThread(self)
		#self.wthread.start()
		QObject.connect(self.ui.actionAbrir, SIGNAL("triggered()"), self.openConnection)
		QObject.connect(self.ui.actionFechar, SIGNAL("triggered()"), self.closeConnection)
		QObject.connect(self.ui.tabWidget, SIGNAL('currentChanged(int)'), self.abaChanged)
		#self.connect(self.wthread, SIGNAL('setIndividual'), self.atualizaIndividual, Qt.QueuedConnection)
		#self.connect(self.wthread, SIGNAL('setGroup'), self.atualizaGrupo, Qt.QueuedConnection)
		self.reactor = qtreactor
		#self.port = int(self.configForm.ui.edtPort.text()) #Port number
		#self.port = 60000
		#self.server = ICUServerFactory(self.port, self.dataReceived, self.ackMsg) #Create server
		#self.server.start(self.reactor) #Starts server, listening on the specified port number
		self.alarmslist = []
		self.alarmslist.append([self.configForm.alarmForm.ui.edtMinPres_3.text(), self.configForm.alarmForm.ui.edtMaxPres_3.text()])
		self.alarmslist.append([self.configForm.alarmForm.ui.edtMinOxi_3.text(), self.configForm.alarmForm.ui.edtMaxOxi_3.text()])
		self.alarmslist.append([self.configForm.alarmForm.ui.edtMinTemp_3.text(), self.configForm.alarmForm.ui.edtMaxTemp_3.text()])
		self.alarmslist.append([self.configForm.alarmForm.ui.edtMinFc_3.text(), self.configForm.alarmForm.ui.edtMaxFc_3.text()])


	def openConnection(self):
		#Desabilita actionAbrir e habilita actionFechar
		self.ui.actionAbrir.setEnabled(0)
		self.ui.actionFechar.setEnabled(1)
		
		#Desabilita configForm e habilita monitForm
		self.configForm.setEnabled(0)
		self.monitForm.setEnabled(1)

		#self.setMonitores()

		self.maxNumMonitors = int(self.configForm.ui.edtMaxMon.text()) #Number of maximum monitors
		self.port = int(self.configForm.ui.edtPort.text()) #Port number
		
		self.server = ICUServerFactory(self.port, self.dataReceived, self.ackMsg) #Create server
		self.server.start(self.reactor) #Starts server, listening on the specified port number

		self.wthread = UiWorkingThread(self)
		
		self.connect(self.wthread, SIGNAL('setIndividual'), self.atualizaIndividual, Qt.QueuedConnection)
		self.connect(self.wthread, SIGNAL('setGroup'), self.atualizaGrupo, Qt.QueuedConnection)

		self.wthread.start()

		#Atualiza barra de status
		self.ui.statusbar.showMessage("Connection ON")

	def closeConnection(self):
		#Desabilita actionFechar e habilita actionAbrir
		self.ui.actionAbrir.setEnabled(1)
		self.ui.actionFechar.setEnabled(0)
		
		#Desabilita monitForm e habilita configForm
		self.configForm.setEnabled(1)
		self.monitForm.setEnabled(0)

		self.disconnect(self.wthread, SIGNAL('setIndividual'), self.atualizaIndividual)
		self.disconnect(self.wthread, SIGNAL('setGroup'), self.atualizaGrupo)

		self.wthread.stop()
		self.removeMonitors()
		self.server.stop(self.reactor)

		self.monitores = []
		self.monitIds = {}

		#Atualiza barra de status
		self.ui.statusbar.showMessage("Connection OFF")

	def alarmChanged(self, field, value):
		setattr(self.iController.alarms, field, int(value))

	def atualizaIndividual(self):
		self.iController.atualizaGui()

	def atualizaGrupo(self):
		for mid in self.monitIds:
			self.monitIds[mid].atualizaGui()

	#function that receives incoming data from twisted api
	def dataReceived(self, data):
		orw = oru_wav_factory.create_oru(data)
		if orw.filler[0] in self.monitIds and (not any(map(lambda x: isinstance(x,obx),orw.segments))):
			self.removeMonitor(orw.filler[0])
			del self.monitIds[orw.filler[0]]
		else:
			objPatient = patient_factory.create_patient(orw.segments)
			
			if orw.filler[0] not in self.monitIds and self.gridMonitores.count() < self.maxNumMonitors:
				pos = len(self.monitIds)
				self.monitores.append(MyMonitor())
				self.addMonitor(self.monitores[pos])
				self.monitIds[orw.filler[0]] = MonitorController(self.monitores[pos], orw.filler[0], self.alarmslist) 
				self.monitores[pos].conecta(self, self.monitIds[orw.filler[0]])
			else:
				message = "Has reached maximum number of monitors: " + str(self.maxNumMonitors)
				self.ui.statusbar.showMessage(message)
				if orw.filler[0] == self.iController.ident:
					self.iController.addPaciente(patient_factory.create_patient(oru_wav_factory.create_oru(data).segments))
			
			self.monitIds[orw.filler[0]].addPaciente(objPatient)
	
	#ack message sent when data is received
	def ackMsg(self):
		return "ACK"

	def setTab(self,tabClass,tab,name = None):
		verticalLayout = QVBoxLayout(tab)
		tab_inst = tabClass()
		verticalLayout.addWidget(tab_inst)
		if isinstance(name,str):
			setattr(self,name, tab_inst)

	def removeMonitors(self):
		for filler_id in self.monitIds:
			self.removeMonitor(filler_id)

	def addMonitor(self, monitor):
		index = self.gridMonitores.count()
		row = 0 if index/4 == 0 else 1
		self.gridMonitores.addWidget(monitor, row, index%4)
		self.gridMonitores.setColumnMinimumWidth(index%4,300)

	def removeMonitor(self, filler_id):
		controller = self.monitIds[filler_id]
		self.monitores.remove(controller.gui)
		self.gridMonitores.removeWidget(controller.gui)
		controller.gui.deleteLater()
		
		#message = "Monitor removed"
		#self.ui.statusbar.showMessage(message)
		

	def trocaControle(self, fonte):
		#self.controller = fonte.controller
		#self.controller.setIndividual(self.monitForm)
		self.iController.ident = fonte.controller.ident
		self.iController.clearPacientes()
		self.iController.alarms = fonte.controller.alarms
		self.ui.tabWidget.setCurrentIndex(1)

	def abaChanged(self):
		if self.ui.tabWidget.currentIndex() == 1:
			self.wthread.individual = True
		else:
			self.wthread.individual = False

if __name__ == "__main__":
        
        app = QApplication([])

        try:
                import qt4reactor
        except: 
                from twisted.internet import qt4reactor

        qt4reactor.install()

        from twisted.internet import reactor
        frm = MainWindow(reactor)
        frm.show()
        reactor.run()
