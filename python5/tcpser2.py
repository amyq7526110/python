#!/usr/bin/env python3

import  socket
import  time


host = ''           #
port = 12345        #
addr = (host,port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)
while True:
    try:
       cli_sock,cli_addr = s.accept()
    except KeyboardInterrupt:
        break
    print('Hello,',cli_addr)
    while True:
        data = cli_sock.recv(1024).decode()
        if data.strip() == 'q':
            break
        print(data)
        try:
#            sdata = input('> ') + '\r\n'
            sdata = '%s   %s \r\n' % (time.time(),data)
            cli_sock.send(sdata.encode())  # 将str编码为bytes
        except BrokenPipeError:
            break
    cli_sock.close()
s.close()

