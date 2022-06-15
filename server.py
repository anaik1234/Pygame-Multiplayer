from socket import *
from threading import Thread

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 5500))
server.listen(10)

print('Server Started')

def positionupdate(conn1, conn2):
    while True:
        position = conn1.recv(1024).decode()
        conn2.send(position.encode())

conn1, conn1_addr = server.accept()
conn2, conn2_addr = server.accept()
conn1.send('Go'.encode())
conn2.send('Go'.encode())

conn1_Thread1 = Thread(target=positionupdate, args=[conn1, conn2])
conn2_Thread1 = Thread(target=positionupdate, args=[conn2, conn1])

conn1_Thread1.start()
conn2_Thread1.start()