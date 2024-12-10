import time
class Client:
    def __init__(self, message_queue):
        self.message_queue = message_queue

    def consume_messages(self):
        if not self.message_queue.is_empty():
            message = self.message_queue.pop()
            print(f"Client received: {message}")
        else:
            print("Client: Queue is empty, waiting for new messages.")