#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
minPort = int(input("Enter min port: "))
maxPort = int(input("Enter max port: "))
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

with open('ports.txt', 'a') as ports_file:
    ports_file.write("-" * 60)
    ports_file.write('\n')
    t1 = datetime.now()

    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
                ports_file.write('Port ' + format(port) + ': 	 Open\n')
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        ports_file.write('Hostname could not be resolved. Exiting\n')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        ports_file.write('Couldn\'t connect to server\n')
        sys.exit()
    t2 = datetime.now()
    total = t2 - t1
    print('Scanning Completed in: ', total)
    ports_file.write('Scanning Completed in: ' + str(total))
    ports_file.write('\n')
