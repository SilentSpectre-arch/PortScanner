#!/bin/env python3

import socket
from concurrent.futures import ThreadPoolExecutor
import sys
import time

#Colors

PINK="\033[95m"
GREEN="\033[92m"
RED="\033[91m"
CYAN="\033[96m"
YELLOW="\033[93m"
RESET="\033[0m"

#Banner

def banner():
    print(PINK + r"""
   ███████╗██╗██╗     ███████╗███╗   ██╗████████╗
   ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝
   ███████╗██║██║     █████╗  ██╔██╗ ██║   ██║
   ╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║
   ███████║██║███████╗███████╗██║ ╚████║   ██║
   ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝

              [ Silent Port Scanner ]
    """ + RESET)


def scan_port(target,port):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result= sock.connect_ex((target,port))

        if result == 0:
            return port

        return None

    finally:
        sock.close()

def main():
    target=input("Enter Target: ")
    p_s= int(input("Start Port: "))
    p_e= int(input("End Port: "))
    ports=range(p_s,p_e)

    with ThreadPoolExecutor(max_workers=100) as exec:
        result = exec.map(
            lambda port: scan_port(target,port),ports
        )

        for result in result:
            if result:
                print(f"Port {result} is open")

if __name__ == "__main__":
    main()