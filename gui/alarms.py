from PyQt4.QtCore import *
from PyQt4.QtGui import *
from alarms_gui import Ui_AlarmsForm

class AlarmForm(QWidget):
	def __init__(self, parent = None):
		super(AlarmForm, self).__init__(parent)
		self.ui = Ui_AlarmsForm()
		self.ui.setupUi(self)
	def setParent(self,parent):
		verticalLayout = QVBoxLayout(parent)
		alarmForm = AlarmForm()
		verticalLayout.addWidget(alarmForm)

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	wind = AlarmForm()
	wind.show()
	app.exec_()
