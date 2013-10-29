from controller import Controller
from Queue import Queue
from threading import Lock
class IndividualController(Controller):
	def __init__(self, gui, ident = None):
		super(IndividualController, self).__init__(gui)
		self.ident = ident
		self.alarms = None
		self.setAlertMap(gui.ui)

	def atualizaGui(self):
		self.filaLock.acquire()
		if not self.fila.empty():
			paciente = self.fila.get()
			self.setLabel(self.gui.ui.lbPaciente, paciente.name)
			self.atualizaLabels(self.gui.ui, paciente)
			self.gui.plotter.atualiza(paciente.measures[4].channels[0].data)
			self.atualizaAlarmes(paciente, '_white')
		self.filaLock.release()

	def clearPacientes(self):
		self.filaLock.acquire()
		self.fila.queue.clear()
		self.filaLock.release()