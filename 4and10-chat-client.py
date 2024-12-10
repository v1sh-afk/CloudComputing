import socket,threading
def recv_msg(client_sock):
  while True:
    msg=client_sock.recv(1024).decode('UTF-8')
    if msg:
      print('\n')
      print(msg)
    else:
      break
def send_messa(client):
  name=input('enter the name: ')
  while True:
    msg=input('enter the message: ') 
    msg=name+msg 
    client.send(msg.encode('UTF-8'))  
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_sock.connect(('localhost',5000))
threading.Thread(target=recv_msg,args=(client_sock,)).start()
send_messa(client_sock)
