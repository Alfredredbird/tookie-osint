#! /usr/bin/env python3

"""
Alfred: Alfred is a advanced OSINT information gathering tool
"""

import os
import sys

if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 10):
        print(
            "Alfred requires Python 3.10+\nYou are using Python %s, which is not supported by Alfred"
            % (python_version)
        )
        sys.exit(1)

    print(os.path.abspath(__file__))
    if os.name == "nt":
        os.system("cd ..")
        os.system("python.exe brib.py")
    else:
        os.system("python3 brib.py")
