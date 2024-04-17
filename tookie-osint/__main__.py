#! /usr/bin/env python3

"""
tookie-osint: tookie-osint is an advanced OSINT information gathering tool
"""

import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="tookie-osint OSINT Tool (Command-Line)")
    
    parser.add_argument(
        "-w", "--webui",
        action="store_true",
        help="Run tookie-osint with the webui"
    )
    return parser.parse_args()


def main():
    print("tookie-osint is starting...")
    args = parse_args()
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 10):
        print(
            f"tookie-osint requires Python 3.10+\nYou are using Python {python_version}, which is not supported by tookie-osint"
        )
        sys.exit(1)

    print(os.path.abspath(__file__))
    if args.webui:
     if os.name == "nt":
        os.system("python.exe webui/webui.py")
     else:
        os.system("python3 webui/webui.py")
    else:    
     if os.name == "nt":
        os.system("python.exe brib.py")
     else:
        os.system("python3 brib.py")

if __name__ == "__main__":
    main()
