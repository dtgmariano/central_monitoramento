from PyQt4.QtCore import *
from PyQt4.QtGui import *
from centgui3 import Ui_Form
from monitgui2 import MyMonitor

class myWindow(QWidget):
	def __init__(self, parent = None):
		QWidget.__init__(self)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		QObject.connect(self.ui.btnNew, SIGNAL('clicked()'), self.Create)	
		QObject.connect(self.ui.btnClose, SIGNAL('clicked()'), self.Close)	
		self.obj = None	
		self.objlist = []

	def Create(self):
		self.obj = MyMonitor(self)
		#self.obj.setGeometry(500, 500, 550, 550)
		#self.obj.show()
		self.ui.graficos.addWidget(self.obj)
		self.ui.graficos.setRowMinimumHeight(len(self.objlist),256)
		self.objlist.append(self.obj)
		print self.objlist
		
	def Close(self):
		self.objlist.pop().close()		
		
if __name__ == "__main__":
	import sys
	app = QApplication([])
	frm = myWindow()
	frm.show()
	sys.exit(app.exec_())

