#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:a1_server.py
@time:2020/12/06
@target:先打开server端监听，再执行client端请求，把transforfile.txt内容传送给results.log
"""

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostip = "192.168.2.108"
port = 6666

serverSocket.bind((hostip, port))

serverSocket.listen(1)

while True:
    clientSocket, clientAddr = serverSocket.accept()
    file = open("results.log", "a+", encoding="utf-8")
    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        elif data.decode('utf-8') == 'quit.EOF':
            exit(1)
        else:
            # file.write('\n')
            file.write(data.decode('utf-8'))
            # file.write(data.decode('utf-8')+'\n')

    file.close()
    clientSocket.close()
