"""Well-known port-to-service name mappings."""

# Common TCP ports and their typical services (not exhaustive)
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Alt"
}

# Return the service name for a port, or 'unknown' if not in the lookup table
def get_service_name(port):
    return COMMON_SERVICES.get(port, "unknown")
