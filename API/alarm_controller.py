class AlarmController:
	def __init__(self, alarmlist):
		self.minv = 0
		self.maxv = 1
		self.alarmresp = []
		self.setAlarms(alarmlist[0], alarmlist[1], alarmlist[2], alarmlist[3])
		
	def setAlarms(self, sysdys, o2, temp, fc):
		self.sysminalarm = int(sysdys[self.minv].split('/')[0])
		self.sysmaxalarm =  int(sysdys[self.maxv].split('/')[0])
		self.dysminalarm = int(sysdys[self.minv].split('/')[1])
		self.dysmaxalarm =  int(sysdys[self.maxv].split('/')[1])
		self.fcminalarm = int(fc[self.minv])
		self.fcmaxalarm =  int(fc[self.maxv])
		self.o2minalarm = int(o2[self.minv])
		self.o2maxalarm =  int(o2[self.maxv])
		self.tempminalarm = int(temp[self.minv])
		self.tempmaxalarm =  int(temp[self.maxv])

	def check(self, measures):
		self.alarmresp = []
		self.alarmresp.append(self.checkPres(int(str(measures[1].channels[1].data).strip('[]')), int(str(measures[1].channels[1].data).strip('[]'))))
		self.alarmresp.append(self.checkSpo(int(str(measures[2].channels[0].data).strip('[]'))))
		self.alarmresp.append(self.checkTemp(int(str(measures[0].channels[0].data).strip('[]'))))
		self.alarmresp.append(self.checkFc(int(str(measures[3].channels[0].data).strip('[]'))))
		return self.alarmresp

	def checkFc(self, fc):
		if fc < self.fcminalarm or fc > self.fcmaxalarm:
			return True
		else:
			return False

	def checkSpo(self, spo):
		if spo < self.o2minalarm or spo > self.o2maxalarm:
			return True
		else:
			return False

	def checkTemp(self, temp):
		if temp < self.tempminalarm or temp > self.tempmaxalarm:
			return True
		else:
			return False

	def checkPres(self, sys, dys):
		if (sys < self.sysminalarm and dys < self.dysminalarm) or (sys > self.sysmaxalarm and dys > self.dysmaxalarm):
			return True
		else:
			return False
