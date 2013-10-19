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
from twisted.internet.task import LoopingCall

ip = "localhost"
port = 60000

smsg = None

def setmsg():
	global smsg
	return smsg
	
def createmsg(m):
	m.preenche()
	orw = mon.get_orw((ip, 'CEN'))	
	global smsg
	smsg = orw.to_str()

if __name__ == '__main__':
	mon = monitor_multi(ip)		
	monit = ICUMonitorFactory(setmsg, ip, port)	
	LoopingCall(createmsg, mon).start(0.5)
	monit.startsend(reactor, 0.5)
	reactor.run()
	
