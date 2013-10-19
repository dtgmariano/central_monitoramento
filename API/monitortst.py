from twisted.internet import protocol, reactor
from twisted.internet.task import LoopingCall
from monitorapi import *

ip = "localhost"
port = 60000
counter = 0
stmsg = ""

def msgcall():
	global stmsg
	return stmsg

def setmsg():
	global stmsg, counter

	if counter == 0:
		stmsg = "jovem"
	elif counter == 1:
		stmsg = "brow"
	elif counter == 2:
		stmsg = "sr sr sr"
	
	print counter
	counter += 1
	if counter > 2:
		counter = 0

monit = CTIMonitorFactory(msgcall, ip, port)
LoopingCall(setmsg).start(0.5)
monit.startsend(reactor, 1)
reactor.run()
