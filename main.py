from report import save_scan_result
from scan_modes import get__full_scan, get_custom_scan, get_quick_scan
from scanner import scan_ports
from validators import validate_ip, validate_port, validate_port_range
from services import get_service_name

# --- Choose scan mode and build the port range to probe ---
choice = input("Choose scan mode: \n[1] - Full Scan(all ports) \n[2] - Quick Scan(1-1024) \n[3] - Custom Scan \n Enter your choice: ")

match choice:
    case "1":
        ports = get__full_scan()

    case "2":
        ports = get_quick_scan()

    case "3":
        # --- Get and validate port range (must be 1–65535, start <= end) ---
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

        ports = get_custom_scan(int(start_port), int(end_port))

    case _:
        print("Invalid choice.")

# --- Get and validate target IP ---
ip = input("Enter IP: ")

if not validate_ip(ip):
    print("Invalid IP address")
    exit()

print(f"Scanning IP: {ip} ...")

# Collect open ports with their associated service names
open_ports = []

# scan_ports returns only the port numbers that responded as open
open_port_numbers = scan_ports(ip, ports)

for port in open_port_numbers:
    service = get_service_name(port)
    open_ports.append({
        "port": port,
        "service": service
    })
    print(f"Port {port} is OPEN ({service})")

# Summary table of all open ports found
print("\nPORT | STATUS | SERVICE")

for port_info in open_ports:
    print(f"{port_info['port']}     OPEN     ({port_info['service']})")

# Persist scan results (e.g. to a file or report)
save_scan_result(ip, open_ports)
