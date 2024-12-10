import socket,threading

def receive_message(csocket):

    while True:
        try:
            data = csocket.recv(4096).decode()
            print(data)
        except:
            csocket.close()
            break
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.connect(('localhost',5000))
thread = threading.Thread(target = receive_message,args = (cs,))
while True:
    try:
        msg = input()
        if msg == 'exit':
            cs.close()
            print("Exited")
        else:
            cs.send(msg.encode('utf-8'))
    except:
        cs.close()
        break
    
        
