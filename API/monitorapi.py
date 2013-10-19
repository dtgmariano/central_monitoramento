from twisted.internet import protocol, reactor
from twisted.internet.task import LoopingCall

class ICUMonitor(protocol.Protocol):
	
	def __init__(self, gui_msg_callback):
		self.msg_callback = gui_msg_callback

	def connectionMade(self):		
		self.transport.write(self.msg_callback())
		self.transport.loseConnection()

class ICUMonitorFactory(protocol.ClientFactory):
	def __init__(self, gui_msg_callback, gui_ip, gui_port):
		self.ip = gui_ip
		self.port = gui_port
		self.msg_callback = gui_msg_callback
		self.objmonit = None

	def buildProtocol(self, addr):
		return ICUMonitor(self.msg_callback)

	def sendmsg(self, gui_reactor):
		gui_reactor.connectTCP(self.ip, self.port, self)

	def startsend(self, gui_reactor, timerep):
		LoopingCall(self.sendmsg, gui_reactor).start(timerep)
