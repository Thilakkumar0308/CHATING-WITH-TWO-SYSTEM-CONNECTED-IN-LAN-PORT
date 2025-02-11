import socket
import threading

def receive_messages(client_socket):
    """Handles receiving messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\nServer: {message}\nEnter command: ", end="")
        except:
            break

def start_client():
    """Connects to the server and allows bidirectional communication."""
    server_ip = '192.168.17.113'  # Replace with the actual server IP
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))
        print("Connected to the server")

        # Start a separate thread to listen for messages from the server
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        while True:
            # Get user input and send it to the server
            command = input("Enter command (or 'exit' to quit): ")
            client_socket.send(command.encode())

            if command.lower() == 'exit':
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
