import sys
sys.path.insert(0, '../API')
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from solo_monit_gui import Ui_SoloMonitForm
from alarms import AlarmForm
from gen_plotter import GenPlotter
import math

class MonitForm(QWidget):
	lbMap = {1:("lbTemperatura","C"), 3:("lbPressao","mmHg"), 4:("lbO2","%"), 5:("lbFC","bpm")}
	def __init__(self, parent = None):
		super(MonitForm, self).__init__(parent)
		self.ui = Ui_SoloMonitForm()
		self.ui.setupUi(self)
		self.alarmForm = AlarmForm()
		self.alarmForm.setParent(self.ui.alarmePanel)
		self.ui.alarmePanel.hide()
		self.ui.parametrosPanel.setStyleSheet("background-color:black;");
		#self.hideAlarms()
		self.ui.btnalarm.clicked.connect(self.toggleAlarms)
		self.hidden = True
		self.monitController = None
		self.plotter = GenPlotter(self.ui.ecgchart,100000)
		self.controller = None
	
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

	def atualiza(self, paciente):
		self.atualizaLabels(self.ui, paciente)
		self.plotter.atualiza(paciente.measures[4].channels[0].data)

	def atualizaLabels(self, gui, paciente):
		for m in paciente.measures:
			if m.cod == 6:
				continue
			lb = getattr(gui,self.lbMap[m.cod][0])
			un = self.lbMap[m.cod][1]
			if m.cod == 3:
				self.setLabel(lb, ("%s/%s" % (m.channels[0].data[0], m.channels[1].data[0])), un)
			else:
				self.setLabel(lb, str(m.channels[0].data[0]), un)

	def setLabel(self, label, dado, unidade = ''):
		label.setText("%s %s" % (dado, unidade))


if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	wind = MonitForm()
	wind.show()
	app.exec_()
