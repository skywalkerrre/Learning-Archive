import socket
from concurrent.futures import ThreadPoolExecutor
#from threading import current_thread

def check_port(host, port):
    #thread_num = current_thread().name
    #print(f"Thread {thread_num} trying port {port}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((host, port))
    sock.close()

    if result == 0:
        return port

def find_open_ports(host, start_port, end_port):
    open_ports = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_port, host, port) for port in range(start_port, end_port + 1)]

        for future in futures:
            port = future.result()
            if port:
                open_ports.append(port)

    return open_ports

if __name__ == '__main__':
    # Provide the remote host IP or hostname
    remote_host = '192.168.1.4'

    start_port = 2100
    end_port = 2123

    open_ports = find_open_ports(remote_host, start_port, end_port)

    if open_ports:
        print(f"Open ports on {remote_host}:")
        for port in open_ports:
            print(port)
    else:
        print(f"No open ports found on {remote_host}")
