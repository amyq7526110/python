#!/usr/bin/env python3
import socket

host = '127.0.0.1'
port = 12345
addr = (host,port)
c = socket.socket(type=socket.SOCK_DGRAM)
while True:
    data = input('> ') + '\r\n'
    if data.strip() == 'q':
        break
    c.sendto(data.encode(),addr)
    print(c.recvfrom(1024)[0].decode())
c.close()

