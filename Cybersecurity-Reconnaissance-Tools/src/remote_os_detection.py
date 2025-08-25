import platform
import subprocess
import re

def detect_remote_os(host):
    try:
        # Check the operating system
        os_type = platform.system()

        if os_type == "Windows":
            # Send ICMP Echo Request and capture the TTL value on Windows
            response = subprocess.run(['ping', '-n', '1', '-w', '1000', host], capture_output=True, text=True)
        else:
            # Send ICMP Echo Request and capture the TTL value on Unix-like systems
            response = subprocess.run(['ping', '-c', '1', '-W', '1', host], capture_output=True, text=True)

        output = response.stdout

        # Extract the TTL value using regular expressions
        ttl_match = re.search(r"TTL=(\d+)", output)
        if ttl_match:
            ttl = int(ttl_match.group(1))
            os_name = ""

            # Compare the TTL value to known OS ranges
            if ttl <= 64:
                os_name = "Linux/Unix"
            elif 65 <= ttl <= 128:
                os_name = "Windows"
            elif 129 <= ttl <= 255:
                os_name = "Solaris/AIX"

            return os_name
        else:
            return False

    except Exception as e:
        return e
    
if __name__ == '__main__':
    # Provide the remote host IP or hostname
    remote_host = '192.168.1.1'
    result = detect_remote_os(remote_host)
    print(result)
