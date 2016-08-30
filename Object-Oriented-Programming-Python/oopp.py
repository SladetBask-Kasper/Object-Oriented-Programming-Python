from random import randrange, uniform
import socket
import os
import platform
import sys
import time

author = ""

def println(arg):
	print(arg)
def printf(arg):
	print(arg)
def quit(value = 1):
	if value == 1:
		exit()
	else:
		pass
def makeSock(protocol = "TCP"):
	if protocol == "TCP" or protocol == "tcp":
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		return tcp
	elif protocol == "UDP" or protocol == "udp":
		udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return udp
	else:
		#print("            [!] ERROR\nUnable to find socket protocol")
		return False
def null():
	return None
def NULL():
	return None
def nil():
	return None
def true():
	return True
def false():
	return False
def rng(min = 0, max = 100):
	num1 = min
	num2 = max
	if num1 >= num2:
		printf("	[!] Invalid Numbers\n 		RNG Recived Invalid Numbers (first number bigger than last) smaller is "+str(max)+ " And Bigger is "+str(min)+ "!!!")
		return None
	# randrange gives you an integral value
	irand = randrange(num1, num2)
	return irand
def sockSend(ip = "ERR", port = 80, proto = "TCP", msg = "|", socket = None):
	if ip == "ERR":
		#print("		[!] Socket Error\n 		Unknown Socket Type Was Given To Socket")
		return False
	elif ip == "err":
		#print("NoSocket")
		return False
	else:
		if proto == "UDP":
			try:
				socket.sendto(data, (ip, int(port)))
			except:
				#print("Error Sending Packet... You have No Internet... Socket Closed!")
				#socket.close()
				return False
			return True
		elif proto == "TCP":
			try:
				socket.send(msg.encode('utf_8'))
			except socket.error:
				#print("ip Down or your internet down or socket error due to too many packets! Socket Closed!")
				#socket.close()
				return False
			return True
def connectedSocket(ip = "ERR", port = 80):
	if ip == "ERR":
		print("Need An IP...")
		return False
	s = makeSock()
	try:
		s.connect((ip, port))
	except socket.gaierror or socket.error:
		print("Socket Error...")
		return False
	return s
def connectTo(ip = "ERR", port = 80, socket = None):
	if ip == "ERR":
		#print("Need an ip")
		return False
	try:
		socket.connect((ip, port))
	except:
		#print("ERROR CONNECTING TO TARGET")
		return False
	return True
def get(var):
	return var
def sockets(proto = None):

	TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	if proto == None:
		return TCP
	elif proto == "UDP":
		return UDP
	elif proto == "TCP":
		return TCP
def system(arg):
	os.system(arg)
def author(name):
	global author
	author = name
def getAuthor():
	global author
	return author
def getPlatform():
	plat = platform.system()
	return plat
def getPlatform2():
	arrayz = []
	plat = platform.system()
	name = sys.platform
	lolz = os.name
	arrayz.append(plat)
	arrayz.append(name)
	arrayz.append(lolz)
	return arrayz
def sayPlatform2():
	platformzzz = getPlatform2()
	for i in platformzzz:
		printf(i)
def makeString(intz):
	ret = str(intz)
	return ret
def makeInt(strz):
	ret = int(strz)
	return ret
def htmlProject(name = "test", scriptExt = ".js"):
	if getPlatform() == "Windows" and " " not in name:
		cmd1 = "mkdir "+str(name)
		cmd3 = "echo code > "+str(name)+ "\\"+str(name)+ scriptExt
		cmd4 = "echo code > "+str(name)+ "\\"+str(name)+ ".css"
		cmd5 = "echo code > "+str(name)+ "\\"+str(name)+ ".html"
		system(cmd1)
		time.sleep(2)
		system(cmd3)
		if scriptExt == ".coffee" or scriptExt == ".Coffee":
			cmdcs = "echo code > "+str(name)+ "\\"+str(name)+ ".js"
			system(cmdcs)
		system(cmd4)
		system(cmd5)
		return True
	else:
		return False
def wait(seconds):
	try:
		time.sleep(seconds)
	except:
		return False
	return True
