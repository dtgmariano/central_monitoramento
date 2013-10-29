import sys
sys.path.insert(0, '../API')
from alarm_controller import AlarmController
sys.path.insert(0, '../hl7parser')
from hl7parser import patient, measure, channel
from Queue import Queue
from threading import Lock
from PyQt4.QtCore import *

class MonitorController:
	lbMap = {1:("lbTemperatura","C"), 3:("lbPressao","mmHg"), 4:("lbO2","%"), 5:("lbFC","bpm")}

	def __init__(self, monitGui, ident, alarmForm):
		self.monitGui = monitGui
		self.ident = ident
		self.fila = Queue()
		self.individual = None
		self.filaLock = Lock()
		self.alarms = AlarmController(alarmForm)
		self.alarmresp = []
		self.pac = None
		
	def atualizaGui(self):
		self.filaLock.acquire()
		if not self.fila.empty():
			paciente = self.fila.get()
			self.pac = paciente
			self.setLabel(self.monitGui.lbPaciente, paciente.name)
			self.setLabel(self.monitGui.lbMonitor, self.ident)
			self.atualizaLabels(self.monitGui, paciente)	
		self.filaLock.release()	

	
	def atualizaIndividual(self):
		self.filaLock.acquire()
		if not self.fila.empty():
			paciente = self.fila.get()
			self.atualizaLabels(self.individual.ui, paciente)
			self.individual.plotter.atualiza(paciente.measures[4].channels[0].data)
		self.filaLock.release()

	def setLabel(self, label, dado, unidade = ''):
		label.setText("%s %s" % (dado, unidade))

	def addPaciente(self, paciente):
		self.filaLock.acquire()
		self.fila.put(paciente)
		self.filaLock.release()

	def setIndividual(self, individualGui):
		self.individual = individualGui

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

	def atualizaAlarmes(self):
		self.alarmresp = []
		alarmcheck = self.alarms.check(self.pac.measures)
		self.alarmresp.append([self.monitGui.alertPressao, alarmcheck[0]])
		self.alarmresp.append([self.monitGui.alertO2, alarmcheck[1]])
		self.alarmresp.append([self.monitGui.alertTemperatura, alarmcheck[2]])
		self.alarmresp.append([self.monitGui.alertFC, alarmcheck[3]])
		return self.alarmresp

