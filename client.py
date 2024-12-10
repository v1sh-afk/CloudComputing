import pickle, socket

class Object():

    def __init__(self, name ,num):
        self.name = name
        self.num = num

def client():

    csocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection = csocket.connect(('localhost',5000))
    print("conne")
    csocket.sendall(pickle.dumps(Object('A',1)))
    data = csocket.recv(4096)
    ro = pickle.loads(data)
    print(ro.name)
    print(ro.num)
    print("jj")
    csocket.close()

client()