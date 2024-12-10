import threading
import time

class MessageQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()  # To ensure thread safety when accessing the queue

    def push(self, message):
        with self.lock:
            self.queue.append(message)
            print(f"Message pushed: {message}")

    def pop(self):
        with self.lock:
            if self.queue:
                return self.queue.pop(0)  # Remove the first message (FIFO)
            else:
                return None

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0
