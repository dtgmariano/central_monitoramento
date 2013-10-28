class GenPlotter:
	def __init__(self, chart, lim = 5000):
		self.chart = chart
		self.lim = lim
		self.yax = []
		self.xax = []

	def atualiza(self, data):
		self.yax += data
		ini = self.xax[-1] if self.xax else 0
		self.xax += range(ini,ini+len(data))
		self.chart.plot(self.xax, self.yax, clear = True)
		self.reseta()

	def reseta(self):
		if len(self.xax) > self.lim:
			self.xax = []
			self.yax = []
