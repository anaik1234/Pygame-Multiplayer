from threading import Thread
import os



def Server():
    os.system('python3 server.py')

def client():
    os.system('python3 client.py')

Thread(target=Server).start()
Thread(target=client).start()
Thread(target=client).start()