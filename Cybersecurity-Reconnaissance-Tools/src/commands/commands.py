import click
import re
from .handlers import detect_os_handler, find_open_ports_handler, find_app_handler, add_port_handler

@click.group()
def cycon():
    """Cyber Security Reconnaisance tools"""
    pass

@cycon.command()
@click.option('--ip', 'ip', help="IP Adress of remote node")
def detect_os(ip):
    """Detect the operating system of a remote host"""
    result = detect_os_handler(ip)
    click.echo(result)

@cycon.command()
@click.option('--ip', 'ip', help="IP Adress of remote node")
@click.option('--start', 'start_port', type=int, help="Port number lower bound", default = 0, show_default=True)
@click.option('--end', 'end_port', type=int, help="Port number upper bound", default = 65536, show_default=True)
def find_open_ports(ip, start_port, end_port):
    """Find open ports on a remote host"""
    result = find_open_ports_handler(ip, start_port, end_port)
    click.echo(result)

@cycon.command()
@click.option('--ip', 'ip', help="IP Adress of remote node")
@click.option('--port', 'port', type=int, help="Port number", default = 0, show_default=True)
def detect_app(ip, port):
    """Find the Application running on an open port"""
    result = find_app_handler(ip, port)
    click.echo(result)

@cycon.command()
@click.option('--app', 'app', help="Name of the application")
@click.option('--port', 'port', type=int, help="Port number", default = 0, show_default=True)
def add_app(port, app):
    """Find open ports on a remote host"""
    result = add_port_handler(port, app)
    click.echo(result)


if __name__ == '__main__':
    cycon()
