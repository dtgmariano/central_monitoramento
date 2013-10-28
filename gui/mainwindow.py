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
from alarm_controller import AlarmController

#Queue for managing processes
from Queue import Queue
#HL7 Parser
from hl7parser import patient, measure, channel, oru_wav, oru_wav_factory, patient_factory
#Twisted API for server
from icucenterapi import ICUCenter, ICUServerFactory
#Twisted imports
from twisted.internet.task import LoopingCall
#Thread imports
from threading import Lock


class MainWindow(QMainWindow):
	def __init__(self, qtreactor):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setTab(ConfigForm, self.ui.tabConfig, "configForm")
		self.setTab(MonitForm, self.ui.tabPacient, "monitForm")
		self.monitores = []
		self.setMonitores()
		self.monitQueue = Queue()
		self.monitList = []
		self.monitIds = {}
		self.wthread = UiWorkingThread(self.monitIds, self)
		self.wthread.start()
		QObject.connect(self.ui.tabWidget, SIGNAL('currentChanged(int)'), self.abaChanged)
		self.controller = None
		#self.individual = None
		self.lock = Lock()
		#Server api
		self.reactor = qtreactor
		#self.port = int(self.configForm.ui.edtPort.text()) #Port number
		self.port = 60000
		self.server = ICUServerFactory(self.port, self.dataReceived, self.ackMsg) #Create server
		self.server.start(self.reactor) #Starts server, listening on the specified port number

	#function that receives incoming data from twisted api
	def dataReceived(self, data):
		orw = oru_wav_factory.create_oru(data)
		objPatient = patient_factory.create_patient(orw.segments)
		if orw.filler[0] not in self.monitIds:
			pos = len(self.monitIds)
			self.monitIds[orw.filler[0]] = MonitorController(self.monitores[pos].ui, orw.filler[0], self.configForm.alarmForm) 
			self.monitores[pos].conecta(self, self.monitIds[orw.filler[0]])
			self.monitIds[orw.filler[0]].addPaciente(objPatient)
		else:
			self.monitIds[orw.filler[0]].addPaciente(objPatient)
		#if self.individual:
		#		self.individual.atualizaIndividual()
		#else:
		#	for mid in self.monitIds:
		#		self.monitIds[mid].atualizaGui()
	
	#ack message sent when data is received
	def ackMsg(self):
		return "ACK"
	
	def setTab(self,tabClass,tab,name = None):
		verticalLayout = QVBoxLayout(tab)
		tab_inst = tabClass()
		verticalLayout.addWidget(tab_inst)
		if isinstance(name,str):
			setattr(self,name, tab_inst)

	def setMonitores(self):
		gridMonitores = QGridLayout(self.ui.widget)
		for i in range(0,8):
			row = 0 if i/4 == 0 else 1
			self.monitores.append(MyMonitor())
			gridMonitores.addWidget(self.monitores[i], row, i%4)
			gridMonitores.setColumnMinimumWidth(i%4,250)

	def trocaControle(self, fonte):
		self.controller = fonte.controller
		self.controller.setIndividual(self.monitForm)
		self.ui.tabWidget.setCurrentIndex(1)


	def abaChanged(self):
		if self.ui.tabWidget.currentIndex() == 1:
			self.wthread.individual = self.controller
		else:
			self.wthread.individual = None

		

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
