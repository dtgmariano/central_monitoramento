from PyQt4.QtCore import *
from PyQt4.QtGui import *
from monitgui1 import Ui_MonitForm
import math

class MyMonitor(QDialog):
	def __init__(self, parent = None):
		super(MyMonitor, self).__init__(parent)
		self.ui = Ui_MonitForm()
		self.ui.setupUi(self)
		self.t1 = QTimer()
		self.t1.timeout.connect(self.plotfunc)
		self.t1.start()
		self.c1 = 0
		self.c2 = 0
		self.x = []
		self.y = []

	def plotfunc(self):
		self.x.append(self.c1)
		self.y.append(self.c2)
		self.c1 += 0.01
		self.c2 = math.sin(2*math.pi*self.c1)
		self.ui.graphicsView.plot(self.x, self.y, clear = True)
		

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	frm = MyMonitor()
	#frm.t1.start()
	frm.show()
	app.exec_()
