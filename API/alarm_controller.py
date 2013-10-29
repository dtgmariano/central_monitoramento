class AlarmController:
	def __init__(self, alarmlist):
		self.minv = 0
		self.maxv = 1
		self.alarmresp = []
		self.setAlarms(alarmlist[0], alarmlist[1], alarmlist[2], alarmlist[3])
		
	def setAlarms(self, sysdys, o2, temp, fc):
		self.sysalarm = [int(sysdys[self.minv].split('/')[0]), int(sysdys[self.maxv].split('/')[0])]
		self.dysalarm = [int(sysdys[self.minv].split('/')[1]), int(sysdys[self.maxv].split('/')[1])]
		self.fcalarm = [int(fc[self.minv]), int(fc[self.maxv])]
		self.o2alarm = [int(o2[self.minv]), int(o2[self.maxv])]
		self.tempalarm = [int(temp[self.minv]), int(temp[self.maxv])]

	def check(self, measures):
		self.alarmresp = []
		self.alarmresp.append(self.checkPres(int(str(measures[1].channels[1].data).strip('[]')), int(str(measures[1].channels[1].data).strip('[]'))))
		self.alarmresp.append(self.checkSpo(int(str(measures[2].channels[0].data).strip('[]'))))
		self.alarmresp.append(self.checkTemp(int(str(measures[0].channels[0].data).strip('[]'))))
		self.alarmresp.append(self.checkFc(int(str(measures[3].channels[0].data).strip('[]'))))
		return self.alarmresp

	def checkFc(self, fc):
		if fc < self.fcalarm[self.minv] or fc > self.fcalarm[self.maxv]:
			return True
		else:
			return False

	def checkSpo(self, spo):
		if spo < self.o2alarm[self.minv] or spo > self.o2alarm[self.maxv]:
			return True
		else:
			return False

	def checkTemp(self, temp):
		if temp < self.tempalarm[self.minv] or temp > self.tempalarm[self.maxv]:
			return True
		else:
			return False

	def checkPres(self, sys, dys):
		if (sys < self.sysalarm[self.minv] and dys < self.dysalarm[self.minv]) or (sys > self.sysalarm[self.maxv] and dys > self.dysalarm[self.maxv]):
			return True
		else:
			return False
