import sys
sys.path.insert(0, '../API')
from alarm_controller import AlarmController
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from threading import Lock
from controller import Controller

class MonitorController(Controller):
	
	def __init__(self, gui, ident, alarmForm):
		super(MonitorController,self).__init__(gui)
		self.ident = ident
		self.alarms = AlarmController(alarmForm)
		self.alarmresp = None
		
	def atualizaGui(self):
		self.filaLock.acquire()
		if not self.fila.empty():
			paciente = self.fila.get()
			self.setLabel(self.gui.lbPaciente, paciente.name)
			self.setLabel(self.gui.lbMonitor, self.ident)
			self.atualizaLabels(self.gui, paciente)
		self.filaLock.release()
		self.alarmresp = self.alarms.check(paciente.measures)
		print self.alarmresp

		'''	
		if self.alarmresp[0] == True:
			self.monitGui.alertPressao.show()
		else:
			self.monitGui.alertPressao.hide()
		
		if self.alarmresp[1] == True:
			self.monitGui.alertO2.show()
		else:
			self.monitGui.alertO2.hide()
		'''
	
		if self.alarmresp[2] == True:
			self.monitGui.alertTemperatura.setText("OK")
		else:
			self.monitGui.alertTemperatura.setText("NOT")
		
		'''
		if self.alarmresp[3] == True:
			self.monitGui.alertFC.show()
		else:
			self.monitGui.alertFC.hide()
		'''

	

	

	
		

