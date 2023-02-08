#!/usr/bin/env python

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
