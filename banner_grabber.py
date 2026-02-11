import socket

target = "127.0.0.1"
port = 80

s = socket.socket()
s.connect((target, port))

s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
response = s.recv(1024)

print(response.decode(errors="ignore"))

s.close()