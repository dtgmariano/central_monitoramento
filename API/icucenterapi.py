from twisted.internet import protocol

class ICUCenter(protocol.Protocol):

	def __init__(self, gui_port, gui_rcv_callback, gui_ack_callback):
		self.port = gui_port
		self.rcv_callback = gui_rcv_callback
		self.ack_callback = gui_ack_callback

	def dataReceived(self, data):
		self.rcv_callback(data)
		self.transport.write(self.ack_callback())

class ICUServerFactory(protocol.Factory):
	def __init__(self, gui_port, gui_rcv_callback, gui_ack_callback):
		self.port = gui_port
		self.rcv_callback = gui_rcv_callback
		self.ack_callback = gui_ack_callback
		self.conn = None

	def buildProtocol(self, addr):
		return ICUCenter(self.port, self.rcv_callback, self.ack_callback)

	def start(self, gui_reactor):
		self.conn = gui_reactor.listenTCP(self.port, self)

	def stop(self, gui_reactor):
		self.conn.stopListening()
