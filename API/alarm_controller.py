class AlarmController:
	def __init__(self, alarmForm):
		self.alarmForm = alarmForm
		self.minal = 0
		self.maxal = 1
		self.alarmresp = []

		self.sysalarm = [int(self.alarmForm.ui.edtMinPres_3.text().split('/')[0]), int(self.alarmForm.ui.edtMaxPres_3.text().split('/')[0])]
		
		self.dysalarm = [int(self.alarmForm.ui.edtMinPres_3.text().split('/')[1]), int(self.alarmForm.ui.edtMaxPres_3.text().split('/')[1])]	
		self.fcalarm = [int(self.alarmForm.ui.edtMinFc_3.text()), int(self.alarmForm.ui.edtMaxFc_3.text())]

		self.o2alarm = [int(self.alarmForm.ui.edtMinOxi_3.text()), int(self.alarmForm.ui.edtMaxOxi_3.text())]

		self.tempalarm = [int(self.alarmForm.ui.edtMinTemp_3.text()), int(self.alarmForm.ui.edtMaxTemp_3.text())]

	def setAlarms(self, syst, dyst, fc, spo, temp):
		self.sysalarm = syst
		self.dystalarm = dyst
		self.fcalarm = fc
		self.o2alarm = spo
		self.tempalarm = temp

	def check(self, measures):
		self.alarmresp = []
		self.alarmresp.append(self.checkPres(int(str(measures[1].channels[1].data).strip('[]')), int(str(measures[1].channels[1].data).strip('[]'))))
		self.alarmresp.append(self.checkSpo(int(str(measures[2].channels[0].data).strip('[]'))))
		self.alarmresp.append(self.checkTemp(int(str(measures[0].channels[0].data).strip('[]'))))
		self.alarmresp.append(self.checkFc(int(str(measures[3].channels[0].data).strip('[]'))))
		return self.alarmresp

	def checkFc(self, fc):
		if fc < self.fcalarm[self.minal] or fc > self.fcalarm[self.maxal]:
			return True
		else:
			return False

	def checkSpo(self, spo):
		if spo < self.o2alarm[self.minal] or spo > self.o2alarm[self.maxal]:
			return True
		else:
			return False

	def checkTemp(self, temp):
		if temp < self.tempalarm[self.minal] or temp > self.tempalarm[self.maxal]:
			return True
		else:
			return False

	def checkPres(self, sys, dys):
		if (sys < self.sysalarm[self.minal] and dys < self.dysalarm[self.minal]) or (sys > self.sysalarm[self.maxal] and dys > self.dysalarm[self.maxal]):
			return True
		else:
			return False
