import socket
import threading
import time
import MySQLdb

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print str(data)
		except:
			pass
		finally:
			tLock.release()
host = '127.0.0.1'
port = 0

server = ('127.0.0.1', 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)
conn = MySQLdb.connect(host="localhost", user="root", passwd="MySuperPassword", db="chats")
x = conn.cursor()
print "Connected to database"


rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

alias = raw_input("Name: ")
print "Retrieving previous chats"
x.execute("SELECT * FROM `chat_logs`")
records = x.fetchall()
for r in records:
	print str(r[2])+" : : "+str(r[1])
print "Finished loading previous chats"
message = raw_input(alias + " -> ")
while message != 'q':
	if message != '':
		s.sendto(alias + ": " + message, server)
	tLock.acquire()
	message = raw_input(alias + "-> ")
	tLock.release()
	time.sleep(0.2)
shutdown = True
rT.join()
s.close()
