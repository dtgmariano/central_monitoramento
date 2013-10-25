from PyQt4.QtCore import *
from PyQt4.QtGui import *
from solo_monitp import Ui_SoloMonitForm
import math

class MyWindow(QWidget):
	def __init__(self, parent = None):
		super(MyWindow, self).__init__(parent)
		self.ui = Ui_SoloMonitForm()
		self.ui.setupUi(self)
		self.t = range(0,100)
		self.x = [v*0.01 for v in self.t]
		self.y = [math.sin(2*math.pi*v) for v in self.x]
		self.ui.ecgchart.plot(self.x, self.y)
		self.pal = QPalette()
		self.pal.setColor(QPalette.Background, Qt.black)
		self.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.red)
		self.ui.lblbpm.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.blue)
		self.ui.lblspo.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.green)
		self.ui.lblnibp.setPalette(self.pal)
		self.pal.setColor(QPalette.Foreground, Qt.red)
		self.ui.lbltemp.setPalette(self.pal)
		self.hideAlarms()
		self.ui.btnalarm.clicked.connect(self.toggleAlarms)
		self.hidden = True
	
	def toggleAlarms(self):
		if self.hidden == True:
			self.showAlarms()
			self.hidden = False
		else:
			self.hideAlarms()
			self.hidden = True

	def showAlarms(self):
		for w in range(0, self.ui.gridLayout_alarms.count()):
			self.ui.gridLayout_alarms.itemAt(w).widget().show()

	def hideAlarms(self):
		for w in range(0, self.ui.gridLayout_alarms.count()):
			self.ui.gridLayout_alarms.itemAt(w).widget().hide()

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	wind = MyWindow()
	wind.show()
	app.exec_()
