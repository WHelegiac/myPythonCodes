'''
Author: WanHao
Date: 2022-02-13 22:35:42
LastEditors: Do not edit
LastEditTime: 2022-02-13 22:36:44
FilePath: \my_python_codes\Socket\client.py
FileDescription: Lazy~~~
'''

import socket

from click import ClickException


#1.创建套接字

client = socket.socket()
client.connect(('127.0.0.1','8999'))

while True