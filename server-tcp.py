#!/usr/bin/env python3

import socket
import sys

import bis_common

CHUNK=1024

def usage ():
    print ("""
usage: server-tcp.py local:port remote:port file

    Accepts a single connection on local:port, ensures it comes from remote:port,
    and saves its transmission on the named file
    """)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)

    local = split_address(sys.argv[1])
    remote = split_address(sys.argv[2])
    filename = sys.argv[3]

    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(local)
        s.listen()
        conn, address = s.accept()
        with conn:
            if conn.getpeername() != remote:
                print ("Peer (%s) not authorized.  Expected %s" % (conn.getpeername(), remote))
                sys.exit(1)
            with open (filename, "wb") as f:
                while True:
                    data = conn.recv(CHUNK)
                    if len(data) == 0:
                        print ("Transmission complete")
                        break
                    f.write(data)
                
