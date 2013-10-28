from PyQt4.QtCore import QThread
import time

class UiWorkingThread(QThread):
	def __init__(self, monitIds, parent = None):
		super(UiWorkingThread, self).__init__(parent)
		self.monitIds = monitIds
		self.individual = False
	
	def run(self):
		while True:
			time.sleep(0.3)
			if self.individual:
				self.individual.atualizaIndividual()
			else:
				for mid in self.monitIds:
					self.monitIds[mid].atualizaGui()
