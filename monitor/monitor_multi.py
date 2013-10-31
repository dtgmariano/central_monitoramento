import sys
sys.path.insert(0, '../geradores')
sys.path.insert(0, '../hl7parser')
from gerador_simples import gerador_simples, gerador_duplo
from gerador_arquivo import gerador_arquivo
from hl7parser import patient, measure, channel, oru_wav
from random import choice
class monitor_multi:
	nomes = ['John', 'Clark','Peter', 'Stela', 'Marta', 'Richard', 'Eve', 'Adam']
	ecgs = [(40, '.ecg_40'), (80, '.ecg_80'), (120, '.ecg_120'), (180, '.ecg_180')]
	def __init__(self,ip):
		self.id = ip
		self.geradores = self.create_gen()
		self.monitored = patient(1,choice(self.nomes))
		self.add_measures()
	def add_measures(self):
		for k in self.geradores.keys():
			genr = self.geradores[k]
			m = measure(k)
			if isinstance(genr, gerador_duplo):
				for g in genr.gens:
					m.add_channel(g.chn)
			else:
				m.add_channel(genr.chn)
			self.monitored.add_measure(m)
	def create_gen(self):
		pressao = gerador_duplo(gerador_simples(120,5),gerador_simples(80,3))
		pressao.gs1.info(1, 'pa', (0,300), 'Systolic', 1, 60)
		pressao.gs2.info(2, 'pa', (0,300), 'Dyastolic', 1, 60)
		temperatura = gerador_duplo(gerador_simples(38,3), gerador_simples(35,4))
		temperatura.gs1.info(1, 'C', (0,100), 'Temperature CH1', 1, 60)
		temperatura.gs2.info(2, 'C', (0,100), 'Temperature CH2', 1, 60)
		spo2 = gerador_simples(92,3)
		spo2.info(1, '%O2', (0, 100), 'Oximetry', 1, 60)
		cor = choice(self.ecgs)
		ecg = gerador_arquivo('../resources/'+cor[1],1000,500,int)
		ecg.info(1, 'mv', (-1024,1024), 'D2', 1, 1000)
		fc = gerador_simples(cor[0],5)
		fc.info(1, 'BPM', (0,300), 'Cardiac Rate', 1, 60)
		return {3:pressao, 1:temperatura, 4:spo2, 6:ecg, 5:fc}
	def preenche(self):
		for m in self.monitored.measures:
			for chn in m.channels:
				chn.bind_data(chn.gen.getNext())
	def get_orw(self,placer):
		orw = oru_wav(placer, (self.id,'MON'))
		orw.add_patient(self.monitored)
		orw.fill_segments()
		return orw

if __name__ == '__main__':
	mon = monitor_multi('9090909090')
	mon.preenche()
	orw = mon.get_orw(('90909090909','CEN'))
	print orw
