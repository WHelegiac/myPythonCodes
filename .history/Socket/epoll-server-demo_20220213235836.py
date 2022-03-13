'''
Author: WanHao
Date: 2022-02-13 23:55:59
LastEditors: Do not edit
LastEditTime: 2022-02-13 23:58:05
FilePath: \my_python_codes\Socket\epoll-server-demo.py
FileDescription: Lazy~~~
'''

from http import server
import socket
import select

def serve():
    server = socket.socket()
    server.bind(('127.0.0.1',8999))
    server.listen(1)
    
    epoll = select.epoll()
    epoll.register(server.fileno(),sle)
    

    