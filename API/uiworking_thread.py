from PyQt4.QtCore import QThread
import time

class UiWorkingThread(QThread):
	def __init__(self, monitIds, parent = None):
		super(UiWorkingThread, self).__init__(parent)
		self.monitIds = monitIds
	
	def run(self):
		while True:
			time.sleep(0.3)
			for mid in self.monitIds:
				self.monitIds[mid].atualizaGui()
				self.monitIds[mid].atualizaIndividual()		
