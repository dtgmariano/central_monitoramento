import sys
sys.path.insert(0, '../API')
sys.path.insert(0, '../geradores')
sys.path.insert(0, '../hl7parser')
sys.path.insert(0, '../monitor')

from hl7parser import patient, measure, channel, oru_wav
from monitgui1 import Ui_MonitForm
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from monitorapi import ICUMonitor, ICUMonitorFactory
from twisted.internet.task import LoopingCall
from monitor_multi import monitor_multi

ip = "localhost"
port = 60000

class MyMonitor(QDialog):
	def __init__(self, qtreactor, qtip, qtport, parent = None):
		super(MyMonitor, self).__init__(parent)
		self.reactor = qtreactor
		self.ip = qtip
		self.port = qtport
		self.smsg = None
		self.x = []
		self.y = []
		self.monit = monitor_multi(ip)
		self.monitw = ICUMonitorFactory(self.setmsg, self.ip, self.port)
	def setmsg(self):		
		return self.smsg
	
	def turnOn(self):
		LoopingCall(self.gerfunc).start(0.3)
		self.monitw.startsend(self.reactor, 0.5)

	def gerfunc(self):
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
	mainwindow = MyMonitor(reactor, ip, port)
	mainwindow.show()
	mainwindow.turnOn()
	reactor.run()	
