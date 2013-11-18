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
from gen_plotter import GenPlotter
from client_api import ICUClient
import time

#ip = "192.168.2.10" Biolab
#ip = '10.5.1.194' Biolab
#ip = 'localhost'
#ip = '192.168.1.57' Hostel
#ip = '10.42.0.12'
ip = '10.42.0.1'
port = 60000

class MonitSim(QWidget):
	def __init__(self, qtreactor, qtip, qtport, parent = None):
		super(MonitSim, self).__init__(parent)
		self.reactor = qtreactor
		self.ip = qtip
		self.port = qtport
		self.ui = Ui_MonitSimForm()
		self.ui.setupUi(self)
		self.plotter = GenPlotter(self.ui.ecgChart)
		self.smsg = None
		self.monit = monitor_multi(sys.argv[1])
		#Twisted client api
		#self.monitw = ICUMonitorFactory(self.setmsg, self.ip, self.port) #Create client
		self.monitw = ICUClient(reactor, self.ip, self.port)

	def closeEvent(self, event):
		self.loop.stop()
		self.monitw.stop_sending()
		time.sleep(1)
		fecha = oru_wav((12312,'CEN'),(sys.argv[1], 'MON'))
		p1 = patient(1,'Jonas Brothers')
		m1 = measure()
		p1.add_measure(m1)
		fecha.add_patient(p1)
		fecha.fill_segments()
		#self.smsg = fecha.to_str()
		self.monitw.msg = fecha.to_str()
		self.monitw.send_msg()
		#time.sleep(5)
		#self.reactor.stop()

	#Message that is sent to the icu center. HL7 format
	def setmsg(self):
		return self.smsg
	
	#Initiates the monitor
	def turnOn(self):
		self.loop = LoopingCall(self.genMeasure)
		self.loop.start(0.3) #Starts function that generates measures
#		self.monitw.startsend(self.reactor, 0.3) #Starts function that sends data to the icu center
		self.monitw.start_sending(0.3)

	#Generates new measures from the patient
	def genMeasure(self):
		self.monit.preenche() 
		orw = self.monit.get_orw((sys.argv[1], 'CEN'))
#		self.smsg = orw.to_str()
		self.monitw.msg = orw.to_str()

		#Creates strings with the measures
		strTemp = str(self.monit.monitored.measures[0].channels[0].data).strip('[]') #Temp
		strO2 = str(self.monit.monitored.measures[2].channels[0].data).strip('[]') #SpO2
		strFc = str(self.monit.monitored.measures[3].channels[0].data).strip('[]') #BPM
		strSys = str(self.monit.monitored.measures[1].channels[0].data).strip('[]') #Systolic
		strDys = str(self.monit.monitored.measures[1].channels[1].data).strip('[]') #Dyastolic
		strName = str(self.monit.monitored.name)
		strId = str(sys.argv[1])
		#Updates the labels for showing the measures
		self.ui.lbTemperatura.setText(strTemp) 
		self.ui.lbO2.setText(strO2)
		self.ui.lbFC.setText(strFc)
		self.ui.lbPressao.setText(strSys + '/' + strDys)
		self.ui.lbPaciente.setText(strName)
		self.ui.lbMonitor.setText(strId)
		self.plotter.atualiza(self.monit.monitored.measures[4].channels[0].data)

		
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
