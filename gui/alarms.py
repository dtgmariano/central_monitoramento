from PyQt4.QtCore import *
from PyQt4.QtGui import *
from alarms_gui import Ui_AlarmsForm

class AlarmForm(QWidget):
	def __init__(self, parent = None):
		super(AlarmForm, self).__init__(parent)
		self.ui = Ui_AlarmsForm()
		self.ui.setupUi(self)
		QObject.connect(self.ui.edtMaxFc_3, SIGNAL('textEdited(QString)'), self.showval)
	def setParent(self,parent):
		verticalLayout = QVBoxLayout(parent)
		alarmForm = AlarmForm()
		verticalLayout.addWidget(alarmForm)
	def showval(self):
		print self, self.ui.edtMinOxi_3.text()
	def connectAlarm(self, mainwindow):
		QObject.connect(self.ui.edtMinFc_3, SIGNAL('texEdited(QString)'), lambda field = 'fcalarm', almvalue = [int(self.ui.edtMinFc_3.text()), int(self.ui.edtMaxFc_3.text())]: mainwindow.alarmChanged(field, almvalue))
		self.ui.edtMinOxi_3.setText('200')
		print self, self.ui.edtMinOxi_3.text()

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	wind = AlarmForm()
	wind.show()
	app.exec_()
