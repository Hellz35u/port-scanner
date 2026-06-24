from scanner import scan_port
from validators import validate_ip, validate_port, validate_port_range

ip = input("Enter IP: ")

if not validate_ip(ip):
    print("Invalid IP address")
    exit()

start_port = input("Start port: ")
end_port = input("End port: ")

if not validate_port(start_port):
    print("Start port must be a number between 1 - 65535")
    exit()

if not validate_port(end_port):
    print("End port must be a number between 1 - 65535")
    exit()

if not validate_port_range(start_port, end_port):
    print("Start port must be smaller than or equal to End port")
    exit()

print(f"Scanning IP: {ip} ...")

start_port = int(start_port)
end_port = int(end_port)

for port in range(start_port, end_port + 1):
    if scan_port(ip,port):
        print(f"Port {port} is OPEN")

