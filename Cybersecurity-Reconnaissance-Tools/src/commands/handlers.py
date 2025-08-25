from src.remote_os_detection import detect_remote_os
from src.open_port_scanner import find_open_ports
from src.detect_app import identify_application
from src.db.db import add_port_application, connect_db

open_ports = []
def detect_os_handler(ip):
    os_name = detect_remote_os(ip)

    if isinstance(os_name, Exception):
        return f'Error: {os_name}'
    
    if os_name:
        return f'The OS of the host: {ip} is {os_name}'
    else:
        return f'Could not determine OS of host: {ip}'

    
def find_open_ports_handler(ip, start_port, end_port):

    open_ports = find_open_ports(ip, start_port, end_port)

    if open_ports:
        print(f"Found open ports on host: {ip}")
        for port in open_ports:
            print(port)
    else:
        print(f"No open ports found on host: {ip} in the given port range({start_port}-{end_port})")


def find_app_handler(ip, port):

    response = identify_application(ip, port)

    if response:
        print(f"Application running on port {port} is: {response}")
        for port in open_ports:
            print(port)
    else:
        print(f"Failed to identify application running on port {port}")


def add_port_handler(port, app):
    database_name = 'portmap.db'
    connection = connect_db(database_name)
    
    if add_port_application(connection, port, app):
        print(f'Added {port}:{app} to database')
    else:
        print("Error adding to database")
