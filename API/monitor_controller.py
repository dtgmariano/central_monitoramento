import sys
sys.path.insert(0, '../API')
from alarm_controller import AlarmController
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from threading import Lock
from controller import Controller
from PyQt4.QtGui import QPixmap

class MonitorController(Controller):
	
	def __init__(self, gui, ident, alarmslist):
		super(MonitorController,self).__init__(gui)
		self.ident = ident
		self.alarms = AlarmController(alarmslist)
		self.setAlertMap(gui.ui)
		
		
	def atualizaGui(self):
		self.filaLock.acquire()
		if not self.fila.empty():
			paciente = self.fila.get()
			self.setLabel(self.gui.ui.lbPaciente, paciente.name)
			self.setLabel(self.gui.ui.lbMonitor, self.ident)
			self.atualizaLabels(self.gui.ui, paciente)
			self.atualizaAlarmes(paciente)
		self.filaLock.release()
		
	def atualizaAlarmes(self, paciente, base = ''):
		alarmcheck = self.alarms.check(paciente.measures)
		extensao = 'png'
		for idx,val in enumerate(alarmcheck):
			if val:
				self.alertMap[idx][0].setPixmap(QPixmap("icones/%s%s.%s" % (self.alertMap[idx][2], '_red', extensao)))
				self.alertMap[idx][1].setStyleSheet("color:red")#.show()
			else:
				self.alertMap[idx][0].setPixmap(QPixmap("icones/%s%s.%s" % (self.alertMap[idx][2], base, extensao)))
				self.alertMap[idx][1].setStyleSheet("")#.hide()
		if any(alarmcheck): 
			self.gui.ui.panel.setStyleSheet('QWidget#panel{background-color: rgb(255, 184, 137);border-radius: 5px; border: 1px solid rgb(255, 141, 1);}') 
		else:
			self.gui.ui.panel.setStyleSheet("QWidget#panel{border-radius: 5px; border: 1px solid black;}")
