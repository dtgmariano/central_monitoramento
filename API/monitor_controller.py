import sys
import copy
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from threading import Lock
from controller import Controller
class MonitorController(Controller):
	def __init__(self, gui, ident):
		super(MonitorController,self).__init__(gui)
		self.ident = ident
		
	def atualizaGui(self):
		self.filaLock.acquire()
		if not self.fila.empty():
			paciente = self.fila.get()
			self.setLabel(self.gui.lbPaciente, paciente.name)
			self.setLabel(self.gui.lbMonitor, self.ident)
			self.atualizaLabels(self.gui, paciente)
		self.filaLock.release()

	

	

	
		

