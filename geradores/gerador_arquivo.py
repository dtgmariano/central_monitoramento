from gerador import gerador
class util:
	@staticmethod
	def file_len(f):
		for i, l in enumerate(f):
			pass
		f.seek(0,0)
		return i + 1
class gerador_arquivo(gerador):
	def __init__(self,filename, fs, msecs, parser=None):
		self.source = open(filename,'r')
		self.fs = fs
		self.nlines = util.file_len(self.source)
		self.npoint = 0
		self.msecs = msecs
		self.parser = parser
	def getNext(self):
		q_pontos = (self.msecs*self.fs)/1000
		values = []
		cont = True
		while cont:
			cont = (self.nlines - self.npoint - q_pontos) < 0
			fim = min(self.nlines - self.npoint, q_pontos)
			for i in range(0,fim):
				val = self.source.readline().rstrip('\n')
				values.append((self.parser(val) if self.parser else val))
			self.npoint += fim
			q_pontos = q_pontos - fim
			if self.final():
				self.reseta()
		return values
	def final(self):
		return self.npoint == self.nlines
	def reseta(self):
		self.source.seek(0,0)
		self.npoint = 0
	def __del__(self):
		self.source.close()
if __name__ == '__main__':
	g = gerador_arquivo('.ecg_80',3000)
	data = g.get_msecs_of_data(500,int)
	print data
	print '--------------####--------------'
	data = g.get_msecs_of_data(500,int)
	print data
