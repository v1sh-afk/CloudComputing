import time
class Server:
    def __init__(self, message_queue):
        self.message_queue = message_queue

    def produce_messages(self,message):
        if message.lower() == 'exit':
            return
        self.message_queue.push(message)