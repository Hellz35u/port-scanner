import os
import json
from report import save_scan_result
from scanner import scan_port
from validators import validate_ip, validate_port, validate_port_range
from services import get_service_name
from datetime import datetime

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

open_ports = []

for port in range(start_port, end_port + 1):
    if scan_port(ip,port):
        service = get_service_name(port)
        open_ports.append({
        "port": port,
        "service": service
    })
        print(f"Port {port} is OPEN ({service})")

print("\nPORT | STATUS | SERVICE")

for port_info in open_ports:
    print(f"{port_info['port']}     OPEN     ({port_info['service']})")

save_scan_result(ip,open_ports)



