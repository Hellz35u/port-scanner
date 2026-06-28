"""Input validation for IP addresses and port ranges."""

import ipaddress

# Return True if ip is a valid IPv4 or IPv6 address.
def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False

# Return True if port is a numeric string in the valid range 1–65535
def validate_port(port):
    if not port.isdigit():
        return False

    port = int(port)

    return 1 <= port <= 65535

# Return True if start_port is less than or equal to end_port
def validate_port_range(start_port, end_port):
    return int(start_port) <= int(end_port)
