from twisted.internet import protocol, reactor
from twisted.internet.task import LoopingCall
from icucenterapi import *

PORT = 60000

def rcvdata(data):
	print data

def ackmsg():
	return "this is my ack msg"

server = ICUServerFactory(PORT, rcvdata, ackmsg)
server.start(reactor)
reactor.run()
