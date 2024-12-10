import pickle
import socket

class Object():
    def __init__(self,name,num):
        self.name = name
        self.num = num

def server():

    ssocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ssocket.bind(('localhost',5000))
    ssocket.listen(1)
    connection, address = ssocket.accept()
    print("Connected to address",address)

    data  = connection.recv(4096)
    ro = pickle.loads(data)
    print(ro.name)
    print(ro.num)

    so = Object("B",2)
    connection.sendall(pickle.dumps(so))

    connection.close()
    ssocket.close()

server()