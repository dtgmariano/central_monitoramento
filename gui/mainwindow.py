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
		
		#self.setTab(Menubar, self.ui.menubar, "menubar")
		#QObject.connect(self.ui.actionAbrir, SIGNAL("triggered()"), self.abrirConexao)
		#self.ui.statusbar.showMessage("Teste")
		
		self.monitores = []
		self.setMonitores(8)
		self.monitQueue = Queue()
		self.monitList = []
		self.monitIds = {}
		self.wthread = UiWorkingThread(self.monitIds, self)
		self.wthread.start()

		#Server api
		self.reactor = qtreactor
		self.port = 60000 #Port number
		self.server = ICUServerFactory(self.port, self.dataReceived, self.ackMsg) #Create server
		self.server.start(self.reactor) #Starts server, listening on the specified port number
	
	def abrirConexao(self):
		self.ui.statusbar.showMessage("Teste")
			
	#function that receives incoming data from twisted api
	def dataReceived(self, data):
		orw = oru_wav_factory.create_oru(data)
		objPatient = patient_factory.create_patient(orw.segments)
		if orw.filler[0] not in self.monitIds:
			pos = len(self.monitIds)
			self.monitIds[orw.filler[0]] = MonitorController(self.monitores[pos].ui, orw.filler[0])
			self.monitIds[orw.filler[0]].addPaciente(objPatient)
		else:
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

	#instancia os objetos da classe "MyMonitor" no form de Monitores "monitForms"
	def setMonitores(self, maxMonitores):
		gridMonitores = QGridLayout(self.ui.widget)
		for i in range(0,maxMonitores):
			row = 0 if i/4 == 0 else 1
			self.monitores.append(MyMonitor())
			gridMonitores.addWidget(self.monitores[i], row, i%4)
			gridMonitores.setColumnMinimumWidth(i%4,250)
		

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
