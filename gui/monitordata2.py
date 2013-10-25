from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pyqtgraph as pg
import numpy as np
from monitordata1 import Ui_Form
import math
import time
		
class MyMonitor(QDialog):
	def __init__(self, parent = None):
		super(MyMonitor, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	frm = MyMonitor()
	frm.show()
	app.exec_()
