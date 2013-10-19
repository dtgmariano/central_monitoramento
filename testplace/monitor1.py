import sys
sys.path.insert(0, '../API')
sys.path.insert(0, '../geradores')
sys.path.insert(0, '../hl7parser')
sys.path.insert(0, '../monitor')

#from gerador_simples import gerador_simples, gerador_duplo
#from gerador_aquivo import gerador_arquivo
from hl7parser import patient, measure, channel, oru_wav
from monitorapi import ICUMonitor, ICUMonitorFactory
from monitor_multi import monitor_multi
from twisted.internet import reactor

ip = "localhost"
port = 60000

smsg = None

def setmsg():
	global smsg
	return smsg
	

if __name__ == '__main__':
	mon = monitor_multi(ip)
	mon.preenche()
	orw = mon.get_orw((ip, 'CEN'))
	#global smsg
	smsg = orw.to_str()
	moni = ICUMonitorFactory(setmsg, ip, port)
	moni.sendmsg(reactor)
	reactor.run()
	
