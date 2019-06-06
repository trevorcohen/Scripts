#!/usr/bin/python3
# Gets the list of ports open for a given IP in a pretty comma seperated list
# TODO get rid of trailing comma 
# Note - this does imply that you are using AutoRecon by Tib3rius to initially scan IP

import os, re
IP = input("Enter IP: ")
startPath = '/root/Documents/AutoRecon/results/'
endPath = '/scans/xml/' 
Path = startPath + IP + endPath
reg = re.compile('(portid=\"(\d+))')
base = 0
print("")
try:
        os.chdir(Path)
        print("Open Ports= ",end = '')
        with open("_full_tcp_nmap.xml") as f:
                for line in f:
                        if reg.search(line):
                                port = reg.search(line).group(2)
                                if int(port) > base:
                                        print(port + "," , end='')
                                        base = int(port)
        print("")
except IOError:
        print('There could be an issue with the path, try again ')
