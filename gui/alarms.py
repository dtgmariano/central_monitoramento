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
		verticalLayout.addWidget(self)
	def connectAlarm(self, mainwindow):
		QObject.connect(self.ui.edtMinFc_3, SIGNAL('textEdited(QString)'), lambda x,y='fcminalarm': mainwindow.alarmChanged(y,x))
		QObject.connect(self.ui.edtMaxFc_3, SIGNAL('textEdited(QString)'), lambda x,y='fcmaxalarm': mainwindow.alarmChanged(y,x))
		QObject.connect(self.ui.edtMinOxi_3, SIGNAL('textEdited(QString)'), lambda x,y='o2minalarm': mainwindow.alarmChanged(y,x))
		QObject.connect(self.ui.edtMaxOxi_3, SIGNAL('textEdited(QString)'), lambda x,y='o2maxalarm': mainwindow.alarmChanged(y,x))
		QObject.connect(self.ui.edtMinTemp_3, SIGNAL('textEdited(QString)'), lambda x,y='tempminalarm': mainwindow.alarmChanged(y,x))
		QObject.connect(self.ui.edtMaxTemp_3, SIGNAL('textEdited(QString)'), lambda x,y='tempmaxalarm': mainwindow.alarmChanged(y,x))
		QObject.connect(self.ui.edtMinPres_3, SIGNAL('textEdited(QString)'), lambda x,y='sysminalarm': mainwindow.alarmChanged(y,x.split('/')[0]))
		QObject.connect(self.ui.edtMaxPres_3, SIGNAL('textEdited(QString)'), lambda x,y='sysmaxalarm': mainwindow.alarmChanged(y,x.split('/')[0]))
		QObject.connect(self.ui.edtMinPres_3, SIGNAL('textEdited(QString)'), lambda x,y='dysminalarm': mainwindow.alarmChanged(y,x.split('/')[1]))
		QObject.connect(self.ui.edtMaxPres_3, SIGNAL('textEdited(QString)'), lambda x,y='dysmaxalarm': mainwindow.alarmChanged(y,x.split('/')[1]))
		

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	wind = AlarmForm()
	wind.show()
	app.exec_()
