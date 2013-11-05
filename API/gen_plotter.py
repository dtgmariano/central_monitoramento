class GenPlotter:
	def __init__(self, chart, lim = 5000):
		self.chart = chart
		self.lim = lim
		self.yax = []
		self.xax = []
		self.count = 25

	def atualiza(self, data):
		self.yax += data
		ini = self.xax[-1] if self.xax else 0
		self.xax += range(ini,ini+len(data))
		self.chart.plot(self.xax, self.yax, clear = True)
		self.ajustaEixo(ini, len(data), 500)
		self.reseta()

	def ajustaEixo(self, ini, tam, span):
		if self.count == 0:
			self.chart.setXRange(ini, ini + tam + span)
			self.count = 25
		else:
			self.count -= 1

	def reseta(self):
		if len(self.xax) > self.lim:
			self.xax = []
			self.yax = []
