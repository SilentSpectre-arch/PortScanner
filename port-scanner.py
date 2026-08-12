#!/bin/env python3

import socket

def scan_port(target,port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        result=sock.connect_ex((target,port))

        if result == 0:
            return True

        return False

    finally:
        sock.close()

target=input("Enter Target: ")

open_ports=[]

for port in range(1,1025):
    if scan_port(target,port):
        open_ports.append(port)

print(open_ports)