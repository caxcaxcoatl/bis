#!/usr/bin/env python3

import socket
import sys

CHUNK=1024

def usage ():
    print ("""
usage: bis local:port remote:port file
    """)

def split_address(addr):
    try:
        a, p = addr.split(":")
    except Exception as e:
        print ("Address %s not valid: %s", addr, e)
        sys.exit(1)

    try:
        p = int(p)
    except Except as e:
        print ("Port %s not valid: %s", p, e)
        sys.exit(1)

    return (a, p)

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

