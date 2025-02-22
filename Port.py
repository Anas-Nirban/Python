import socket

def scan_port(ip, port):
    """Checks if a port on a given IP address is open."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0

print("Welcome to the Basic Port Scanner!")

# Input the IP address and port range to scan
target_ip = input("Enter the IP address to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print(f"\nScanning IP: {target_ip} from Port {start_port} to {end_port}...\n")

# Loop through the specified port range
for port in range(start_port, end_port + 1):
    if scan_port(target_ip, port):
        print(f"Port {port} is OPEN.")
    else:
        print(f"Port {port} is CLOSED.")
        
print("\nPort scanning completed.")
