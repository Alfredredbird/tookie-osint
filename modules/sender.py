"""
Client that sends the file (uploads)
"""
import argparse
import os
import socket
from configparser import ConfigParser

import tqdm

from modules.lang import *

config = ConfigParser()
language_code = getLang(config)
language_module = load_language(language_code)

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4  # 4KB
filename = input(language_module.sender4)
host = str(input("Host IP: ⤷ "))
port = 5001


def send_file(filename, host, port, SEPARATOR, BUFFER_SIZE, language_module):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"{language_module.sender1} {host}:{port}")
    s.connect((host, port))
    print(language_module.sender2)

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(
        range(filesize),
        f"{language_module.sender3} {filename}",
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    )
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the socket
    s.close()


send_file(filename, host, port, SEPARATOR, BUFFER_SIZE, language_module)
