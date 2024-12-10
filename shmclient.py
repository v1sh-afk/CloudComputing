# client.py

from multiprocessing import shared_memory
import time

def client(shm_name):
    shm = None  # Initialize shm to None
    try:
        # Attach to the existing shared memory block
        shm = shared_memory.SharedMemory(name=shm_name)
        print("Client: Attached to shared memory with name:", shm_name)
        
        # Read data from shared memory
        data = bytes(shm.buf[:]).decode('utf-8').strip('\x00')
        print("Client: Read message from shared memory:", data)
        
    except FileNotFoundError:
        print("Client: Shared memory with name", shm_name, "does not exist.")
    
    finally:
        # Only close shared memory if it was successfully attached
        if shm:
            shm.close()
            print("Client: Shared memory closed.")

if __name__ == "__main__":
    # Update this to the actual name printed by the server
    shm_name = "wnsm_0f4a9dc0"  # Replace with shared memory name from the server output
    time.sleep(1)  # Optional delay to ensure the server has created the memory
    client(shm_name)
