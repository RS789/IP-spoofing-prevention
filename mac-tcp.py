#!/usr/bin/python

#Port Scanner using SYN Scanning (Half Open TCP Scanning)

from scapy.all import *
import sys, argparse


#the 'argparse' module makes it easy to write user-freindly command-line interfaces. 
#it also automatically generates help and usage messages and issues errors on invalid arguments

argParser = argparse.ArgumentParser(description='TCP SYN Scanner for a single host.')
argParser.add_argument('--version','-v',action='version', version = '%(prog)s is at version 1.0.0')
argParser.add_argument('host',metavar = 'host', type=str, help='The hostname or IP to scan.')
argParser.add_argument('-p', metavar='port', nargs=2, type=str, help='port range scan eg 80 443')
argParser.add_argument('-t', metavar = 'timeout', type=float, help = 'The time to wait for ACKs.', default=1)
arguments = argParser.parse_args()

print ('Scanning host %s' %(arguments.host))

startPort = 1
endPort = 65535

if arguments.p != None: #if we have arguments
    startPort = int(arguments.p[0])
    endPort = int(arguments.p[1])

for port in xrange (startPort, endPort +1):
    packet=sr1(IP(dst=arguments.host)/TCP(dport=port,flags='S'),verbose=0,timeout=arguments.t)
    if packet:
        print ('Port %d is open!' % port)
