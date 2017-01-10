import socket
import time

import MySQLdb
import time
import socket

host = '127.0.0.1'
port = 5000

try:
	print "Starting server ....."
	clients = []
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	s.setblocking(1)
	print "Server started"
	conn = MySQLdb.connect(host="localhost", user="root", passwd="MySuperPassword", db="chats")
	x = conn.cursor()
except Exception, err:
	print Exception, err
	
	
quitting = False

while not quitting:
	try:
		data, addr = s.recvfrom(1024)
		if "Quit" in str(data):
			quitting = True
		if addr not in clients:
			clients.append(addr)
			
		print time.ctime(time.time()) + str(addr) + ": :" + str(data)
		for client in clients:
			s.sendto(data, client)
			x.execute("INSERT INTO `chat_logs` VALUES ('0','"+str(data)+"', '"+time.strftime('%Y-%m-%d %H:%M:%S')+"')")
			conn.commit()
	except Exception, err:
		print Exception, err
s.close()
