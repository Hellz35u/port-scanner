"""Persist scan results to JSON files in the results/ directory."""

import os
import json
from datetime import datetime


def save_scan_result(ip, open_ports):
    """Write scan metadata and open ports to a timestamped JSON file."""
    scan_result = {
        "ip": ip,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "open_ports": open_ports
    }

    # Create results folder if it doesn't exist yet
    os.makedirs("results", exist_ok=True)

    # Unique filename per scan so runs don't overwrite each other
    file_name = datetime.now().strftime("scan_%Y-%m-%d_%H-%M-%S.json")
    file_path = os.path.join("results", file_name)

    try:
        with open(file_path, "w") as file:
            json.dump(scan_result, file, indent=4)

    except OSError as e:
        print(f"Failed to save scan results: {e}")
        return False

    return True
