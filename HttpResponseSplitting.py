# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
import socket

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# '/' URL is bound with welcome() function.
def welcome():
    return "Welcome to the Flask Web Server!"

def handle_client(client_socket):
    # Receive the client's request
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request: {request}")

    # Extract the parameter value from the request (simulated vulnerable code)
    parameter_value = request.split('param=')[1].split(' ')[0]

    # Create a vulnerable HTTP response (simulated vulnerability)
    http_response = f"HTTP/1.1 200 OK\r\n"
    http_response += f"Content-Type: text/html\r\n"
    http_response += f"Set-Cookie: sessionid=abc123; param={parameter_value}\r\n"
    http_response += f"\r\n"
    http_response += f"<html><body><h1>Hello World!</h1></body></html>\r\n"

    # Send the HTTP response to the client
    client_socket.send(http_response.encode('utf-8'))
    client_socket.close()

def main():
    # Create a socket and bind it to localhost on port 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)
    print("Listening on port 8080...")

    while True:
        # Accept incoming client connections
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Handle the client connection
        handle_client(client_socket)

if __name__ == "__main__":
    main()


