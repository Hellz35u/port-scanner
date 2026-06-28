"""TCP port scanner — probes ports in parallel using threaded socket connections."""

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# Try a TCP connection to a single port; return True if the port is open
def scan_port(ip, port):
    sock = None

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Short timeout so closed/filtered ports don't stall the scan
        sock.settimeout(0.5)

        # connect_ex returns 0 on success, errno otherwise (non-blocking style)
        result = sock.connect_ex((ip, port))

    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False

    finally:
        if sock:
            sock.close()

    return result == 0

# Scan many ports concurrently and return a list of open port numbers
def scan_ports(ip, ports):
    open_ports = []

    # Thread pool speeds up large ranges; each worker runs scan_port()
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {
            executor.submit(scan_port, ip, port): port
            for port in ports
        }

        # Process results as they finish (order may differ from input)
        for future in as_completed(futures):
            port = futures[future]

            if future.result():
                open_ports.append(port)

    return open_ports
