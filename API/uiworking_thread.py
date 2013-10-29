from PyQt4.QtCore import *
import time

class UiWorkingThread(QThread):
	def __init__(self, monitIds, parent = None):
		super(UiWorkingThread, self).__init__(parent)
		self.monitIds = monitIds
		self.individual = False
		self.signal = SIGNAL('signal')
	
	def run(self):
		while True:
			time.sleep(0.3)
			if self.individual:
				self.individual.atualizaIndividual()
			else:
				for mid in self.monitIds:
					self.monitIds[mid].atualizaGui()
					self.emit(self.signal, self.monitIds[mid].atualizaAlarmes())
