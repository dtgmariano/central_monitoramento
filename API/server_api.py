from twisted.internet import protocol

class ICUServer(protocol.Factory):
	def __init__(self, reactor, gui_port, gui_rcv_callback = None):
		self.reactor = reactor
		self.port = gui_port
		self.rcv_callback = gui_rcv_callback
		self.conn = None
	
	def buildProtocol(self, addr):
		self.proto = ICUProtocol(self, None, self.rcv_callback)
		return self.proto

	def start_listening(self):
		self.conn = self.reactor.listenTCP(self.port, self)

	def stop_listening(self):
		self.conn.stopListening()

def data_rcv(data):
	print data

if __name__ == "__main__":
	from twisted.internet import reactor
	a = ICUServer(reactor, 60000, data_rcv)
	a.start_listening()
	reactor.run()
