import socket

host = "example.com"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
client.send(request.encode())

response = client.recv(4096)
print(response.decode(errors="ignore"))

client.close()