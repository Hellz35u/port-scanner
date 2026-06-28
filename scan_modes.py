"""Predefined port ranges for full, quick, and custom scan modes."""

from scanner import scan_ports


def get_quick_scan():
    """Return ports 1–1024 — common services (HTTP, SSH, FTP, etc.)."""
    return range(1, 1025)


def get__full_scan():
    """Return all valid TCP ports 1–65535."""
    return range(1, 65536)


def get_custom_scan(start_port, end_port):
    """Return an inclusive port range from start_port through end_port."""
    # range() excludes the upper bound, so +1 includes end_port
    return range(start_port, end_port + 1)
