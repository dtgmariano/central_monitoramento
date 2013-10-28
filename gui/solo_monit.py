from PyQt4.QtCore import *
from PyQt4.QtGui import *
from solo_monit_gui import Ui_SoloMonitForm
from alarms import AlarmForm
import math

class MonitForm(QWidget):
	def __init__(self, parent = None):
		super(MonitForm, self).__init__(parent)
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
		self.alarmForm = AlarmForm()
		self.alarmForm.setParent(self.ui.alarmePanel)
		self.ui.alarmePanel.hide()
		self.ui.parametrosPanel.setStyleSheet("background-color:black;");
		#self.hideAlarms()
		self.ui.btnalarm.clicked.connect(self.toggleAlarms)
		self.hidden = True
		self.monitController = None
	
	def toggleAlarms(self):
		if self.hidden == True:
			self.ui.alarmePanel.show()
			#self.showAlarms()
			self.hidden = False
		else:
			self.ui.alarmePanel.hide()
			#self.hideAlarms()
			self.hidden = True

	def showAlarms(self):
		for w in range(0, self.ui.gridLayout_alarms.count()):
			self.ui.gridLayout_alarms.itemAt(w).widget().show()

	def hideAlarms(self):
		for w in range(0, self.ui.gridLayout_alarms.count()):
			self.ui.gridLayout_alarms.itemAt(w).widget().hide()

	def setFonte(self,monitController):
		self.monitController = monitController

	def atualizaGui(self):
		if monitController:
			self.monitController.atualizaIndividual(self)


if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	wind = MonitForm()
	wind.show()
	app.exec_()
