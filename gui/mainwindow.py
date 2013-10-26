from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_gui import Ui_MainWindow
from config import ConfigForm
from solo_monit import MonitForm
from monitordata import MyMonitor

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setTab(ConfigForm, self.ui.tabConfig, "configForm")
		self.setTab(MonitForm, self.ui.tabPacient, "monitForm")
		self.monitores = []
		self.setMonitores()
	
	def setTab(self,tabClass,tab,name = None):
		verticalLayout = QVBoxLayout(tab)
		tab_inst = tabClass()
		verticalLayout.addWidget(tab_inst)
		if isinstance(name,str):
			setattr(self,name, tab_inst)

	def setMonitores(self):
		gridMonitores = QGridLayout(self.ui.widget)
		for i in range(0,8):
			row = 0 if i/4 == 0 else 1
			self.monitores.append(MyMonitor())
			gridMonitores.addWidget(self.monitores[i], row, i%4)
			gridMonitores.setColumnMinimumWidth(i%4,250)
		


if __name__ == "__main__":
	import sys
	app = QApplication([])
	frm = MainWindow()
	frm.show()
	sys.exit(app.exec_())