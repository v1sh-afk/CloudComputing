import time
import threading

class MessageQueueServer:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def push_message(self, message):
        with self.lock:
            self.queue.append(message)
            print(f"Server: Message '{message}' added to the queue.")

    def get_message(self):
        with self.lock:
            if self.queue:
                return self.queue.pop(0)
            else:
                return None

def simulate_server(server):
    while True:
        message = input("Enter message to send to client (type 'exit' to stop): ")
        if message.lower() == 'exit':
            break
        server.push_message(message)
        time.sleep(1)  # Simulating delay

if __name__ == "__main__":
    server = MessageQueueServer()
    server_thread = threading.Thread(target=simulate_server, args=(server,))
    server_thread.start()
    server_thread.join()
