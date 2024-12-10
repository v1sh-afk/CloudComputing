import socket,threading
clients=[]
def handle_client(client,addr):
    print(f'made new connection {addr}')
    while True:
        msg=client.recv(1024)
        if msg:
            try:
                broadcast(client,msg)
            except:
                print(f'error occured with{client_socket}')    
                break
        else:
            print('error')    
            break
    clients.remove(client)
    client.close()
def broadcast(sender,msg):
    for client in clients:
        if client!=sender:
            try:
                client.send(msg)
            except:
                print('error')

server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(('localhost',5000))
server_sock.listen()
while True:
    client_socket,addr=server_sock.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client,args=(client_socket,addr)).start()