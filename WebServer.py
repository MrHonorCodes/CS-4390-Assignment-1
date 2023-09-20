import socket
import sys

# Initialize web socket
web_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set port for web server
port_num = 8080
web_sock.bind(('', port_num))

# Listen for incoming connections
web_sock.listen(1)

print(f"Web server is active on port {port_num}")

while True:
    print("Awaiting client request...")
    
    # Accept incoming connection
    client_sock, client_address = web_sock.accept()

    try:
        # Receive HTTP request
        http_req = client_sock.recv(1024).decode()
        target_file = http_req.split()[1]
        
        # Open and read requested file
        with open(target_file[1:], 'r') as f_obj:
            file_data = f_obj.read()
        
        # Send HTTP header to client
        client_sock.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        # Send entire file content
        client_sock.send(file_data.encode())
        
        client_sock.send("\r\n".encode())
        client_sock.close()

    except FileNotFoundError:
        # Handle file not found scenario
        client_sock.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        client_sock.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        # Close client socket
        client_sock.close()

# Close web socket
web_sock.close()
sys.exit()  # Exit program
