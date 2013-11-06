from twisted.internet import protocol
from twisted.internet.task import LoopingCall
from protocol_api import ICUProtocol

class ICUClient(protocol.ClientFactory):
	def __init__(self, reactor, ip=None, port=None, rcv_callback=None):
		self.reactor = reactor
		self.data_received = rcv_callback
		self.ip = ip if ip else 'localhost'
		self.port = port if port else 60000
		self.msg = None
		self.proto = None
		self.looping_func = None

	def buildProtocol(self, addr):
		if not self.proto:
			self.proto = ICUProtocol(self, self.clientReady, self.data_received)
		return self.proto

	def clientReady(self, proto):
		self.proto.sendLine(self.msg)
		self.proto.transport.loseConnection()

	def send_msg(self):
		self.connection = self.reactor.connectTCP(self.ip, self.port, self)

	def set_msg(self, msg):
		self.msg = msg

	def start_sending(self, time):
		self.looping_func = LoopingCall(self.send_msg)
		self.looping_func.start(time)
	
	def stop_sending(self):
		self.looping_func.stop()

	def clientConnectionFailed(self, connector, reason):
		pass
		
	def clientConnectionLost(self, connector, reason):
		pass

if __name__ == "__main__":
	from twisted.internet import reactor
	a = ICUClient(reactor)
	a.set_msg("Hello!\nAgain!")
	a.send_msg()
	reactor.run()
