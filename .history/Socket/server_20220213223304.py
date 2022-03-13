'''
Author: WanHao
Date: 2022-02-13 22:27:48
LastEditors: Do not edit
LastEditTime: 2022-02-13 22:32:29
FilePath: \my_python_codes\Socket\server.py
FileDescription: Lazy~~~
'''

import socket
from threading import local



#1.创建套接字
server = socket.socket()

#2.绑定套接字
local_host = ('127.0.0.1',8999)
server.bind(local_host)

#3监听套接字(数量为1)
server.listen(1)

#4.接受连接
sock ,addr = server.accept()

print(f"The connect address : {}")