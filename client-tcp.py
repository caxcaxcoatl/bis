#!/usr/bin/env python3

import socket
import sys

import bis_common

CHUNK=1024

def usage ():
    print ("""
usage: bis local:port remote:port file
    """)


if __name__ == "__main__":
    if len (sys.argv) != 4:
        usage()
        sys.exit(1)

    local = split_addres(sys.argv[1])
    remote = split_addres(sys.argv[2])
    filename = sys.argv[3]

    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(local)
        print ("Client socket bound; press ENTER to connect and send file")
        print (s)
        input()
        connect (remote)
        print ("Connected to %s; starting transfer" % remote)
        print (s)
        with open(filename, "rb") as f:
            total = 0
            while True:
                data = f.read(CHUNK)
                if len(data) == 0:
                    print ("\rFile transfer complete.    ")
                    break
                s.send(data)
                total += len(data)
                print ("\r%s bytes transferred" % total)

