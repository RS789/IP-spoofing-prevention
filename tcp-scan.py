#! /usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = raw_input('What website to scan?: ')

def pscan(port):
    try:
        con = s.connect((target,port))
        return True
    except:
        return False


for x in range(25):
    if pscan(x):
        print('Port',x,'is open')
