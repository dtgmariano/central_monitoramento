import sys
import copy
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from threading import Lock
class MonitorController:
	lbMap = {1:("lbTemperatura","C"), 3:("lbPressao","mmHg"), 4:("lbO2","%"), 5:("lbFC","bpm")}

	def __init__(self, monitGui, ident):
		self.monitGui = monitGui
		self.ident = ident
		self.fila = Queue()
		self.individual = None
		self.filaLock = Lock()

	def atualizaGui(self):
		if not self.fila.empty():
			paciente = self.fila.get()
			self.setLabel(self.monitGui.lbPaciente, paciente.name)
			self.setLabel(self.monitGui.lbMonitor, self.ident)
			self.atualizaLabels(self.monitGui, paciente)
				
	def atualizaIndividual(self):
		if not self.fila.empty():
			paciente = self.fila.get()
			self.atualizaLabels(self.individual.ui, paciente)
			self.individual.plotter.atualiza(paciente.measures[4].channels[0].data)

	def setLabel(self, label, dado, unidade = ''):
		label.setText("%s %s" % (dado, unidade))

	def addPaciente(self, paciente):
		self.fila.put(paciente)

	def setIndividual(self, individualGui):
		self.individual = individualGui

	def atualizaLabels(self, gui, paciente):
		for m in paciente.measures:
			if m.cod == 6:
				continue
			lb = getattr(gui,self.lbMap[m.cod][0])
			un = self.lbMap[m.cod][1]
			if m.cod == 3:
				self.setLabel(lb, ("%s/%s" % (m.channels[0].data[0], m.channels[1].data[0])), un)
			else:
				self.setLabel(lb, str(m.channels[0].data[0]), un)
		

