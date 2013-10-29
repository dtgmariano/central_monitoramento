#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue
from threading import Lock
from PyQt4.QtCore import QString
class Controller(object):
	lbMap = {1:("lbTemperatura","ºC"), 3:("lbPressao","mmHg"), 4:("lbO2","%"), 5:("lbFC","bpm")}
	def __init__(self, gui):
		self.gui = gui
		self.fila = Queue()
		self.filaLock = Lock()

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
