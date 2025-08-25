import socket
from src.db.db import get_application_by_port, connect_db

def identify_application(ip, port):
    # try:
    #     # Create a socket object and set a timeout
    #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     sock.settimeout(2)

    #     # Connect to the specified IP and port
    #     sock.connect((ip, port))

    #     # Receive the response (banner) from the application
    #     response = sock.recv(1024).decode()

    #     # Close the socket connection
    #     sock.close()

    #     # Print the application banner or response
    #     #print(f"Application running on {ip}:{port}:")
    #     print(response.strip())
    #     return response.strip()

    # except socket.timeout:
    #     print(f"Connection to {ip}:{port} timed out.")
    # except socket.error as e:
    #     print(f"Error: {e}")
    # except Exception as e:
    #     print(f"Unexpected error occurred: {e}")
    database_name = 'portmap.db'
    connection = connect_db(database_name)
    app = get_application_by_port(connection, port)
    return app


if __name__ == '__main__':
    # Provide the IP address and port of the open application
    target_ip = '127.0.0.1'
    target_port = 80

    # Call the function to identify the application running on the open port
    identify_application(target_ip, target_port)
