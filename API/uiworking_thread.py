from PyQt4.QtCore import *
import time
from threading import Event

class UiWorkingThread(QThread):
	def __init__(self, parent = None):
		super(UiWorkingThread, self).__init__(parent)
		self.individual = False
		self.hasStoped = Event()
	
	def run(self):
		while not self.hasStoped.isSet():
			time.sleep(0.3)
			if self.individual:
				self.emit(SIGNAL('setIndividual'))
			else:
				self.emit(SIGNAL('setGroup'))

	def stop(self):
		self.hasStoped.set()

	def isStoped(self):
		return not self.hasStoped.isSet()