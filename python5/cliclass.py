#!/usr/bin/env python3
import socket
import sys

def communicate(cli_sock):
    while True:
        data = input('> ') + '\r\n'
        cli_sock.send(data.encode())
        if data.strip() == 'q':
            break
        print(cli_sock.recv(1024).decode())
if __name__ == '__main__':
    host =  sys.argv[1]
    port =  int(sys.argv[2])
    addr =  (host,port)      # 客户端连接的服务其地址
    c = socket.socket()
    c.connect(addr)
    communicate(c)





