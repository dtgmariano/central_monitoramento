sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
class MonitorController:
	lbMap = {1:("lbTemperatura","°C"), 3:("lbPressao","mmHg"), 4:("lbO2","\%"), 5:("lbFC","bpm")}

	def __init__(self, monitGui, ident):
		self.monitGui = monitGui
		self.id = ident
		self.fila = Queue()

	def atualizaGui(self):
		paciente = self.fila.get()
		self.setLabel(monitGui.lbPaciente, paciente.name)
		self.setLabel(monitGui.lbMonitor, ident)
		for m in paciente.measures:
			lb = monitGui.getattr(lbMap[m.cod][0])
			un = lbMap[m.cod][1]
			if m.cod == 3:
				self.setLabel(lb, ("%s/%s" % m.channels[0].data[0], m.channels[0].data[1]), un)
			else:
				self.setLabel(lb, str(m.channels[0].data[0]), un)


	def setLabel(self, label, dado, unidade = ''):
		label.setText("%s %s" % (dado, unidade))

	def addPaciente(self, paciente):
		self.fila.put(paciente)

	def atualizaIndividual(self):
		pass

