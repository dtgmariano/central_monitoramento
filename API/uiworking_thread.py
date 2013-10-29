from PyQt4.QtCore import *


import time

class UiWorkingThread(QThread):
	def __init__(self, parent = None):
		super(UiWorkingThread, self).__init__(parent)
		self.individual = False
	
	def run(self):
		while True:
			time.sleep(0.3)
			if self.individual:
				self.emit(SIGNAL('setIndividual'))
				#self.controller.atualizaGui()
			else:
				self.emit(SIGNAL('setGroup'))
				#for mid in self.monitIds:
					#self.monitIds[mid].atualizaGui()