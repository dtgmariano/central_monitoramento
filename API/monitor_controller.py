import sys
sys.path.insert(0, '../API')
from alarm_controller import AlarmController
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from threading import Lock
from controller import Controller

class MonitorController:
	
	def __init__(self, gui, ident, alarmslist):
		super(MonitorController,self).__init__(gui)
		self.ident = ident
		self.alarms = AlarmController(alarmslist)
		self.alarmresp = []
		self.pac = None
		self.alarmresp = None
		self.alertMap = {0:self.gui.alertPressao, 1:self.gui.alertO2, 2:self.gui.alertTemperatura, 3:self.gui.alertFC}
		
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
		print self.alarmresp

		
	def atualizaAlarmes(self, paciente):
		alarmcheck = self.alarms.check(paciente.measures)
		for idx,val in enumerate(alarmcheck):
			if val:
				alertMap[idx].show()
			else:
				alertMap[idx].hide()	
