# CHATING-WITH-TWO-SYSTEM-CONNECTED-IN-LAN-PORT

Key Features Added
✅ Bidirectional Communication → The server can now send messages to the client, and vice versa.
✅ Multi-Client Support → The server uses threads to handle multiple connections at once.
✅ Non-Blocking Client Input → The client listens for messages from the server while also allowing user input.
✅ Graceful Handling → Prevents crashes when the connection is closed unexpectedly.

How It Works
Run the Server (python server.py) on the host machine.
Run the Client (python client.py) on another machine and connect to the server.
Both client and server can now send and receive messages.
Type 'exit' on either side to close the connection.
Would you like any additional features, such as command execution on the client or server? 🔥







You said:
HOW TO USE THIS
ChatGPT said:
How to Use This Bidirectional Client-Server Program 🚀
Step 1: Run the Server (on the main computer)
On the server machine (your PC), follow these steps:
Save the server code to a file named server.py
Run the server script
Open a terminal or command prompt
Navigate to the folder where server.py is located
Run the following command:
nginx
Copy
Edit
python server.py
The server will start listening for incoming connections on port 12345
Step 2: Run the Client (on another device)
On the client machine (another PC), follow these steps:
Save the client code to a file named client.py
Edit client.py and update server_ip
Replace 192.168.17.114 with the actual IP address of the server PC
To find your server's local IP address:
Windows: Run ipconfig in Command Prompt
Linux/Mac: Run ifconfig or hostname -I in Terminal
Run the client script
Open a terminal or command prompt
Navigate to the folder where client.py is located
Run the following command:
nginx
Copy
Edit
python client.py
The client will try to connect to the server
Step 3: Communicate Between Client and Server
🔹 After the client connects:

The server will display "Connection established with <client IP>"
The client will receive a welcome message from the server
The client can send messages or commands to the server
The server can send messages back to the client
Example Interaction
Client types: Hello, Server!
Server sees: Client <IP> sent: Hello, Server!
Server responds: Hi Client!
Client receives: "Server: Hi Client!"
Step 4: Exit the Program
Either side can type exit to close the connection.
The connection will be terminated, and the server will be ready for new connections.
Extra Features You Can Add
✅ Allow Server to Execute Commands on Client (like running scripts remotely)
✅ File Transfer Support (send files between client and server)
✅ Encrypt Messages (for secure communication)

Would you like to add any of these features? 🚀
