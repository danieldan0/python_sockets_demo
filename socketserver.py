import socket
from random import choice

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if not data:
        continue
    marks = [chr(i) for i in range(768, 879)]
    string = data.decode("utf-8")
    newstring = ""
    for char in string:
        newstring += char + choice(marks)
    conn.send(newstring.encode("utf-8"))
