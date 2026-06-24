from scanner import scan_port

ip = input("Enter IP: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"Scanning {ip}...")

for port in range(start_port, end_port + 1):
    if scan_port(ip,port):
        print(f"Port {port} is OPEN")

