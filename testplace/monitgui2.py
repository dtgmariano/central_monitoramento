from PyQt4.QtCore import *
from PyQt4.QtGui import *
from monitgui1 import Ui_MonitForm
import math
import time

class WorkingThread(QThread):
	def __init__(self, mw):
		super(WorkingThread, self).__init__(mw.ui.graphicsView)
		self.graph = mw.ui.graphicsView
		
	def run(self):
		while True:
			time.sleep(0.125)
			self.emit(SIGNAL('setStatus'))
			
class MyMonitor(QDialog):
	def __init__(self, parent = None):
		super(MyMonitor, self).__init__(parent)
		self.c1 = 0
		self.c2 = 0
		self.x = []
		self.y = []
		self.ui = Ui_MonitForm()
		self.ui.setupUi(self)
		self.th = WorkingThread(self)
		self.connect(self.th, SIGNAL('setStatus'), self.plotfunc, Qt.QueuedConnection)
		self.th.start()
		#self.t1 = QTimer()
		#self.t1.timeout.connect(self.th.start)
		#self.t1.start()
	def plotfunc(self):
		for i in range(0,10):
			self.x.append(self.c1)
			self.y.append(self.c2)
			self.c1 += 0.01
			self.c2 = math.sin(2*math.pi*self.c1)
		self.ui.graphicsView.plot(self.x, self.y, clear = True)
		if len(self.x) >= 1000:
			self.x = []
			self.y = []
			self.c1 = 0
		

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	frm = MyMonitor()
	#frm.t1.start()
	frm.show()
	app.exec_()
