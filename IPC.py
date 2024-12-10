import os
import multiprocessing

def parent_child_communication():
    # Create two pipes: one for parent-to-child and one for child-to-parent communication
    parent_to_child, child_to_parent = os.pipe(), os.pipe()

    # Fork using multiprocessing
    def parent_process():
        # Close unused ends of pipes
        os.close(parent_to_child[0])  # Close reading end of parent-to-child pipe
        os.close(child_to_parent[1])  # Close writing end of child-to-parent pipe

        # Message from parent to child
        parent_message = "Hello from parent!".encode()
        os.write(parent_to_child[1], parent_message)
        print("Parent: Sent message to child.")

        # Read response from the child
        child_response = os.read(child_to_parent[0], 1024).decode()
        print("Parent: Received response from child:", child_response)

        # Close used ends of pipes
        os.close(parent_to_child[1])
        os.close(child_to_parent[0])

    def child_process():
        # Close unused ends of pipes
        os.close(parent_to_child[1])  # Close writing end of parent-to-child pipe
        os.close(child_to_parent[0])  # Close reading end of child-to-parent pipe

        # Read message from the parent
        parent_message = os.read(parent_to_child[0], 1024).decode()
        print("Child: Received message from parent:", parent_message)

        # Message from child to parent
        child_message = "Hello from child!".encode()
        os.write(child_to_parent[1], child_message)
        print("Child: Sent response to parent.")

        # Close used ends of pipes
        os.close(parent_to_child[0])
        os.close(child_to_parent[1])

    # Create parent and child processes
    parent = multiprocessing.Process(target=parent_process)
    child = multiprocessing.Process(target=child_process)

    # Start the processes
    parent.start()
    child.start()

    # Wait for both processes to finish
    parent.join()
    child.join()

if __name__ == "__main__":
    parent_child_communication()
