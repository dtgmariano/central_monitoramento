import sys
sys.path.insert(0, '../API')
sys.path.insert(0, '../geradores')
sys.path.insert(0, '../hl7parser')
sys.path.insert(0, '../monitor')

from hl7parser import patient, measure, channel, oru_wav
from monitsim_gui import Ui_MonitSimForm
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from monitorapi import ICUMonitor, ICUMonitorFactory
from twisted.internet.task import LoopingCall
from monitor_multi import monitor_multi

ip = "localhost"
port = 60000

class MonitSim(QWidget):
	def __init__(self, qtreactor, qtip, qtport, parent = None):
		super(MonitSim, self).__init__(parent)
		self.reactor = qtreactor
		self.ip = qtip
		self.port = qtport
		self.ui = Ui_MonitSimForm()
		self.ui.setupUi(self)
		self.smsg = None
		self.x = []
		self.y = []
		self.monit = monitor_multi(ip)
		#Twisted client api
		self.monitw = ICUMonitorFactory(self.setmsg, self.ip, self.port) #Create client

	#Message that is sent to the icu center. HL7 format
	def setmsg(self):		
		return self.smsg
	
	#Initiates the monitor
	def turnOn(self):
		LoopingCall(self.genMeasure).start(0.3) #Starts function that generates measures
		self.monitw.startsend(self.reactor, 0.3) #Starts function that sends data to the icu center

	#Generates new measures from the patient
	def genMeasure(self):
		self.monit.preenche() 
		orw = self.monit.get_orw((self.ip, 'CEN'))
		self.smsg = orw.to_str()
		print self.smsg
		
if __name__ ==  "__main__":
	app = QApplication(sys.argv)

	try:
		import qt4reactor
	except:
		from twisted.internet import qt4reactor

	qt4reactor.install()

	from twisted.internet import reactor
	mainwindow = MonitSim(reactor, ip, port)
	mainwindow.show()
	mainwindow.turnOn()
	reactor.run()	
