import socket
import sys

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(' '.join(sys.argv[1::]).encode("utf-8"))

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()
