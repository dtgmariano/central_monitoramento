import sys
sys.path.insert(0, '../API')
sys.path.insert(0, '../geradores')
sys.path.insert(0, '../hl7parser')
sys.path.insert(0, '../monitor')

from hl7parser import patient, measure, channel, oru_wav, oru_wav_factory, patient_factory
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
		#This region sets the background black and changes the color or each parameter label
		'''
		self.pal = QPalette()
		self.pal.setColor(QPalette.Background, Qt.black)
		self.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.blue)
		self.ui.lbO2.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.red)
		self.ui.lbTemperatura.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.yellow)
		self.ui.lbPressao.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.green)
		self.ui.lbFC.setPalette(self.pal)
		'''
		self.smsg = None
		self.x = []
		self.y = []
		self.monit = monitor_multi(ip)
		#Twisted client api
		self.monitw = ICUMonitorFactory(self.setmsg, self.ip, self.port) #Create client
		#ECG chart
		self.count1 = 0
		self.xax = []
		self.yax = []

	#Message that is sent to the icu center. HL7 format
	def setmsg(self):		
		return self.smsg
	
	#Initiates the monitor
	def turnOn(self):
		LoopingCall(self.genMeasure).start(0.1) #Starts function that generates measures
		self.monitw.startsend(self.reactor, 0.1) #Starts function that sends data to the icu center

	#Generates new measures from the patient
	def genMeasure(self):
		self.monit.preenche() 
		orw = self.monit.get_orw((self.ip, 'CEN'))
		self.smsg = orw.to_str()

		#Creates strings with the measures
		strTemp = str(self.monit.monitored.measures[0].channels[0].data).strip('[]') #Temp
		strO2 = str(self.monit.monitored.measures[2].channels[0].data).strip('[]') #SpO2
		strFc = str(self.monit.monitored.measures[3].channels[0].data).strip('[]') #BPM
		strSys = str(self.monit.monitored.measures[1].channels[0].data).strip('[]') #Systolic
		strDys = str(self.monit.monitored.measures[1].channels[1].data).strip('[]') #Dyastolic

		#Updates the labels for showing the measures
		self.ui.lbTemperatura.setText(strTemp) 
		self.ui.lbO2.setText(strO2)
		self.ui.lbFC.setText(strFc)
		self.ui.lbPressao.setText(strSys + '/' + strDys)

		#Plotting
		#creates Xaxis and Yaxis
		for val in self.monit.monitored.measures[4].channels[0].data:			
			self.xax.append(self.count1)
			self.yax.append(val)
			self.count1+=1
		self.ui.ecgChart.plot(self.xax, self.yax, clear = True) #Invalidade chart
		#Prevents list from growing too large
		if self.count1 > 5000:
			self.count1 = 0
			self.xax = []
			self.yax = []

		
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
