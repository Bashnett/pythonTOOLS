#!/bin/python3
lipo=[]

import os
from termcolor import colored
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(10)


os.system("figlet PyPORT")

print("[+] Welcomet to PyPORT [+]")

host=input("Enter the IP_ADDRESS to SCAN: ")

def port_scan(port):
    if sock.connect_ex((host,port)):
        print(colored(f"Port {port} is Closed.",'red'))
    else:
        print(colored(f"Port {port} is Open.",'green'))

Num=int(input('''[+] How many port you want to scan? [+]
        [+] 1= For scanning one port enter 1
        [+] 2= For scanning list of port enter 2
        [+] 3= For scanning BETWEEN ports enter 3
       Port= '''))
if Num==1:
    i=int(input("Enter the port you want to Scan: "))
    port_scan(i)

elif Num==2:
    n=int(input("How many list of port you want to scan? "))
    for j in range(n):
        lipo.append(int(input(f"Enter the [{j+1}] port you want to Scan: ")))
    for i in lipo:
        port_scan(i)

elif Num==3:
    print('''More than 100 ports cannot be scanned at once.
    so,you can scan 100 ports like from 1-100 or 300-400
    ''')
    f=int(input("Enter Starting port of Scan: "))
    l=int(input("Enter End port of Scan: "))
    for i in range(f,l):
        port_scan(i)

else:
    print("Please Enter form [1-3] According to Instruction")


