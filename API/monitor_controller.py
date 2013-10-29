import sys
sys.path.insert(0, '../API')
from alarm_controller import AlarmController
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from threading import Lock
from controller import Controller

class MonitorController(Controller):
	
	def __init__(self, gui, ident, alarmslist):
		super(MonitorController,self).__init__(gui)
		self.ident = ident
		self.alarms = AlarmController(alarmslist)
		self.alarmresp = []
		self.pac = None
		self.alarmresp = None
		self.alertMap = {0:self.gui.lbPressao, 1:self.gui.lbO2, 2:self.gui.lbTemperatura, 3:self.gui.lbFC}
		
	def atualizaGui(self):
		self.filaLock.acquire()
		if not self.fila.empty():
			paciente = self.fila.get()
			self.setLabel(self.gui.lbPaciente, paciente.name)
			self.setLabel(self.gui.lbMonitor, self.ident)
			self.atualizaLabels(self.gui, paciente)
			self.atualizaAlarmes(paciente)
		self.filaLock.release()
		self.alarmresp = self.alarms.check(paciente.measures)
		
	def atualizaAlarmes(self, paciente):
		alarmcheck = self.alarms.check(paciente.measures)
		for idx,val in enumerate(alarmcheck):
			if val:
				self.alertMap[idx].setStyleSheet("color:red")#.show()
			else:
				self.alertMap[idx].setStyleSheet("")#.hide()
		
		if any(alarmcheck): 
			self.gui.panel.setStyleSheet('QWidget#panel{background-color: rgb(255, 184, 137);border-radius: 5px; border: 1px solid rgb(255, 141, 1);}') 
		else:
			self.gui.panel.setStyleSheet("QWidget#panel{border-radius: 5px; border: 1px solid black;}")
