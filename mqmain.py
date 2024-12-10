from messageClass import MessageQueue
from mqserver import Server
from mqclient import Client
import threading
if __name__ == "__main__":
    message_queue = MessageQueue()

    # Create server and client objects
    server = Server(message_queue)
    client = Client(message_queue)

    while True:
        msg = input("Enter message: ")
        if msg == "exit":
            break
        server.produce_messages(msg)
        print(message_queue)
        client.consume_messages()

