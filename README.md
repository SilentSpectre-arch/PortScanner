███████╗██╗██╗     ███████╗███╗   ██╗████████╗
   ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝
   ███████╗██║██║     █████╗  ██╔██╗ ██║   ██║
   ╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║
   ███████║██║███████╗███████╗██║ ╚████║   ██║
   ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝

# Port Scanner

A simple and fast TCP port scanner written in python using the built-in `socket` library and `ThreadPoolExecutor`


## Features

- TCP port scanning
- IPv4 support
- Custom start and end port
- Multithrreaded scanning
- Socket timeout
- Simple terminal banner
- Colored terminal output
- Automatic socket cleanup
- No external Python dependencies

## Requirements

- Python3
- Linux, macOS or Windows

Check your Python version:

````bash
Python3 --version
````

## Installation

Clone the repo:

````bash
git clone https://github.com/SilentSpectre-arch/PortScanner.git
cd PortScanner
````

## Usage
````bash
python3 port-scanner.py
````

You will be asked for the target:

````bash
Enter Target: 127.0.0.1
Start Port: 1
End Port: 1024
````

Example output:

````text
Port 22 is open
port 80 is open
port 443 is open
````

You can also scan a hostname.

## Limitations

This is a basic port scanner and currently does not include:

- UDP scanning
- Service detection
- Banner grabbing
- OS detection
- Stealth scanning
- Advance scan techniques

These features can be added in future versions.