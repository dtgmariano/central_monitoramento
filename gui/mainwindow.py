from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_gui import Ui_MainWindow
from config import ConfigForm

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setConfigTab()
		self.setPatientTab()

	def setPatientTab(self):
		self.patientForm = 
	def setConfigTab(self):
		self.configForm = ConfigForm(self.ui.tabConfig)


if __name__ == "__main__":
	import sys
	app = QApplication([])
	frm = MainWindow()
	frm.show()
	sys.exit(app.exec_())