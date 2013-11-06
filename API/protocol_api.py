from twisted.internet import protocol
from twisted.protocols.basic import LineReceiver

class ICUProtocol(LineReceiver):
	def __init__(self, factory, conok_callback=None, rcv_callback=None):
		self.factory = factory
		self.conok_callback = conok_callback
		self.rcv_callback = rcv_callback

	def connectionMade(self):
		self.conok_callback(self)

	def lineReceived(self, line):
		self.rcv_callback(line)
