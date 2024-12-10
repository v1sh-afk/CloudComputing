import threading, socket

clients = []
def handle_clients(connection, addr):

    print("Connetced ton: ",addr)

    clients.append(connection)

    while True:

        try:
            msg = connection.recv(4096).decode()
            broadcast(connection, msg)
            print("Message: ",msg)
        except:
            clients.remove(connection)
            connection.close()
            break

def broadcast(connection,msg):
    for c in clients:
        try:
            if c == connection:
                pass
            else:
                c.send(msg.encode('utf-8'))
        except:
            clients.remove(c)
            c.close()


ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(('localhost',5000))
ss.listen()
while True:
    c,a = ss.accept()
    thread = threading.Thread(target = handle_clients,args=(c,a))
    thread.start()
            
