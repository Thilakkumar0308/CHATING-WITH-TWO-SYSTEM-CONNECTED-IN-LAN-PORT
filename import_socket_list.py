import socket
import threading

def handle_client(client_socket, client_address):
    """Handles communication with a connected client."""
    print(f"Connection established with {client_address}")
    client_socket.send("Welcome to the server! You can send and receive messages.".encode())

    while True:
        try:
            # Receive command from the client
            command = client_socket.recv(1024).decode()
            if not command:
                break  # Exit if the connection is closed
            
            print(f"Client {client_address} sent: {command}")

            if command.lower() == 'exit':
                print(f"Closing connection with {client_address}.")
                client_socket.send("Goodbye!".encode())
                break

            # Echo command back to the client (or process it)
            response = f"Server received: {command}"
            client_socket.send(response.encode())

            # Now, allow server to send messages to client
            server_msg = input("Enter message to send to client (or 'exit' to close): ")
            if server_msg.lower() == 'exit':
                client_socket.send("Server is closing connection.".encode())
                break
            client_socket.send(server_msg.encode())

        except Exception as e:
            print(f"Error with {client_address}: {e}")
            break

    client_socket.close()
    print(f"Connection closed with {client_address}")

def start_server():
    """Starts the server to accept connections."""
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
