#!/usr/bin/env python3

import  socket

host = ''           #
port = 12345        #
addr = (host,port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)
cli_sock,cli_addr = s.accept()
print('Hello,',cli_addr)
data = cli_sock.recv(1024)
print(data)
cli_sock.send(b'i wsnd \n\r')
cli_sock.close()
s.close()

