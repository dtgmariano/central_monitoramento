from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_gui import Ui_MainWindow
from config import ConfigForm
from solo_monit import MonitForm

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setTab(ConfigForm, self.ui.tabConfig, "configForm")
		self.setTab(MonitForm, self.ui.tabPacient, "monitForm")
	
	def setTab(self,tabClass,tab,name = None):
		verticalLayout = QVBoxLayout(tab)
		tab_inst = tabClass()
		verticalLayout.addWidget(tab_inst)
		if isinstance(name,str):
			setattr(self,name, tab_inst)
		


if __name__ == "__main__":
	import sys
	app = QApplication([])
	frm = MainWindow()
	frm.show()
	sys.exit(app.exec_())