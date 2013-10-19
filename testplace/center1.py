import sys
sys.path.insert(0, '../API')
sys.path.insert(0, '../hl7parser')

from hl7parser import patient, measure, channel, oru_wav, oru_wav_factory, patient_factory
from icucenterapi import ICUCenter, ICUServerFactory
from twisted.internet import reactor

PORT = 60000

def rcvdata(data):
	orw2 = oru_wav_factory.create_oru(data)
	p2 = patient_factory.create_patient(orw2.segments)
	print p2.measures[4].channels[0].data, p2.measures[4].channels[0].descricao 
	
def ackmsg():
		return "ok"
		
if __name__ == "__main__":
	server = ICUServerFactory(PORT, rcvdata, ackmsg)
	server.start(reactor)
	reactor.run()
		
