#!/bin/env python3

import socket

target=input("Enter Target: ")

for port in range(1,1025):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(2)
    result=sock.connect_ex((target,port))

    if result == 0:
        print(f"Port: {port} is open")

    
    sock.close()