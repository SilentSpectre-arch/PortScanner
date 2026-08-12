#!/bin/env python3

import socket

def scan_port(target,port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result=sock.connect_ex((target,port))

    if result == 0:
        print(f"Port: {port} is open")
    sock.close()

target= input("Enter target: ")

for port in range(1,1025):
    scan_port(target,port)

