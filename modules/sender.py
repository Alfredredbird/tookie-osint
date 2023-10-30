"""
Client that sends the file (uploads)
"""
import argparse
import os
import socket

import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4  # 4KB
filename = input("File To Send: ⤷ ")
host = str(input("Host IP: ⤷ "))
port = 5001


def send_file(filename, host, port, SEPARATOR, BUFFER_SIZE):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # start sending the file
    progress = tqdm.tqdm(
        range(filesize),
        f"Sending {filename}",
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


send_file(filename, host, port, SEPARATOR, BUFFER_SIZE)
