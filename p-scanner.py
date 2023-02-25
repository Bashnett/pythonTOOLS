#!/bin/python3

from socket import *
import argparse
from threading import *

G = '\033[32m'
R = '\x1b[31m'  # Red color escape code
W = '\x1b[0m'   # Reset color escape code
Y = '\x1b[33m'  # Yellow color escape code

print('''%s                                                 
 _ __        ___  ___ __ _ _ __  _ __   ___ _ __ 
| '_ \ _____/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| |_) |_____\__ \ (_| (_| | | | | | | |  __/ |   
| .__/      |___/\___\__,_|_| |_|_| |_|\___|_|   
|_|                                            %s%s
                                        
            # Coded by potT                                 
'''%(R,W,G))


def connScan(tgtHost, tgtPort):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print(f"[+] {tgtPort} is Open")
    except:
        print(f"[+] {tgtPort} is Closed")

    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)

    except:
        print('Unknown Host %s ' %tgtHost)

    try:
        tgtName=gethostbyaddr(tgtIP)
        print('[+] Scan Results for: ' + tgtName[0])

    except:
        print('[+] Scan Results for: ' + tgtIP)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t=Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser=argparse.ArgumentParser(description='Usage of program: '+'-H <target Host> -p <target ports>')
    parser.add_argument('-H', dest='tgtHost', type=str, help='specify target host')
    parser.add_argument('-p', dest='tgtPort', type=str, help='specify target Ports separated by comma')
    args=parser.parse_args()
    tgtHost=args.tgtHost
    tgtPorts=str(args.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage )
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__=='__main__':
    main()
