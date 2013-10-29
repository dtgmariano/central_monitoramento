#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue
from threading import Lock
from PyQt4.QtCore import QString
from PyQt4.QtGui import QPixmap
class Controller(object):
	lbMap = {1:("lbTemperatura","ºC"), 3:("lbPressao","mmHg"), 4:("lbO2","%"), 5:("lbFC","bpm")}
	def __init__(self, gui):
		self.gui = gui
		self.fila = Queue()
		self.filaLock = Lock()
		

	def setAlertMap(self, gui):
		self.alertMap = {0:(gui.imgPressao, gui.lbPressao, 'pressao'), 1:(gui.imgO2, gui.lbO2, 'spo'), 2:(gui.imgTemperatura, gui.lbTemperatura, 'temp'), 3:(gui.imgFC, gui.lbFC, 'fc')}

	def addPaciente(self, paciente):
		self.filaLock.acquire()
		self.fila.put(paciente)
		self.filaLock.release()

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
		label.setText(QString.fromUtf8("%s %s" % (dado, unidade)))


	def atualizaAlarmes(self, paciente, base = ''):
		alarmcheck = self.alarms.check(paciente.measures)
		extensao = 'png'
		for idx,val in enumerate(alarmcheck):
			if val:
				self.alertMap[idx][0].setPixmap(QPixmap("icones/%s%s.%s" % (self.alertMap[idx][2], '_red', extensao)))
			else:
				self.alertMap[idx][0].setPixmap(QPixmap("icones/%s%s.%s" % (self.alertMap[idx][2], base, extensao)))
		self.gui.ui.imgFC.setPixmap(QPixmap("icones/fc_white.png"))