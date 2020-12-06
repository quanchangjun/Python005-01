#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:a2_client.py
@time:2020/12/06
"""

import socket

targetHost = "192.168.2.108"
targetPort = 6666

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((targetHost, targetPort))

with open("transforfile.txt", "r+", encoding="utf-8") as f:
    for line in f.readlines():
        clientSocket.send(line.encode('utf-8'))

clientSocket.send('quit.EOF'.encode('utf-8'))
