#!/bin/python3
lipo=[]

import os
from termcolor import colored
import socket

os.system("figlet PyPORT")

print(colored("[+] Welcomet to PyPORT [+]\n",'blue'))

host=input(colored("Enter the IP_ADDRESS to SCAN: ",'red'))


def port_scan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(10)
    if s:
        result = s.connect_ex((host, port))
        if result == 0:
            print(colored(f"\nPort {port} is open\n",'green'))
        s.close()
    else:
        print("Failed to create socket")


Num=int(input(colored('''[+] How many port you want to scan? [+]
        [+] 1= For scanning one port enter 1
        [+] 2= For scanning list of port enter 2
        [+] 3= For scanning BETWEEN ports enter 3
       Port= ''','green')))
if Num==1:
    i=int(input(colored("\nEnter the port you want to Scan: ",'green')))
    port_scan(i)

elif Num==2:
    n=int(input(colored("\nHow many list of port you want to scan? ",'red')))
    for j in range(n):
        lipo.append(int(input(colored(f"Enter the [{j+1}] port you want to Scan: ",'green'))))
    for i in lipo:
        port_scan(i)

elif Num==3:
    print(colored('''\nYou can scan number of ports like this:''','green'))
    f=int(input(colored("Enter Starting port to Scan: ",'yellow')))
    l=int(input(colored("Enter End port to Scan: ",'yellow')))
    for i in range(f,l):
        port_scan(i)
    print(colored(f"Other ports are Closed\n",'red'))

else:
    print(colored("Please Enter form [1-3] According to Instruction",'red'))
