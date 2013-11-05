from twisted.internet import protocol, reactor
from twisted.internet.task import LoopingCall
from twisted.protocols.basic import LineReceiver

class ICUProtocol(LineReceiver):
	def __init__(self, factory, conok_callback, rcv_callback):
		self.factory = factory
		self.conok_callback = conok_callback
		self.rcv = rcv_callback

	def connectionMade(self):
		self.conok_callback(self)

	def lineReceived(self, line):
		self.rcv(line)

class ICUClientFactory(protocol.ClientFactory):
	def __init__(self, conok_callback, rcv_callback):
		self.proto = None
		self.conok = conok_callback
		self.rcv = rcv_callback

	def buildProtocol(self, addr):
		return ICUClientProtocol(self, self.clientReady, self.rcv)

	def clientReady(self, proto):
		self.proto = proto 
		self.conok()

	def msg_received(self, line):
		self.rcv(line)

	def send_msg(self, msg):	
		if self.proto:
			self.proto.sendLine(msg)

	def clientConnectionLost(self, connector, reason):
		pass

	def clientConnectionFailed(self, connector, reason):
		pass
