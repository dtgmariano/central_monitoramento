from gerador import gerador
import numpy as np
from random import choice
class gerador_simples(gerador):
	def __init__(self, mean, sd):
		self.mean = mean
		self.sd = sd
		self.base = np.random.random_integers(self.mean - self.sd, self.mean + self.sd, 1)[0]
		self.list = [self.base for i in range(0,10)] + [self.base+(sd/2), self.base-(sd/2)]
	def getNext(self,n = 1):
		return [choice(self.list) for i in range(0,n)]
		#return np.random.random_integers(self.mean - self.sd, self.mean + self.sd, n)

class gerador_duplo:
	def __init__(self, gs1, gs2):
		self.gs1 = gs1
		self.gs2 = gs2
		self.gens = [gs1,gs2]
	def getNext(self, n = 1):
		s1 = self.gs1.getNext(n)
		s2 = self.gs2.getNext(n)
		return zip(s1,s2)

if __name__ == '__main__':
	g = gerador_simples(80,4)
	g1 = gerador_simples(120,5)
	g2 = gerador_simples(80,3)
	gd = gerador_duplo(g1,g2)
	n = 0
	while n < 10:
		print g.getNext(n+1)
		print gd.getNext(n+1)
		n += 1
	
