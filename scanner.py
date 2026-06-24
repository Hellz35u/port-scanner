import socket


def scan_port(ip, port):
    sock = None

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False

    finally:
        if sock:
            sock.close()

    return result == 0
