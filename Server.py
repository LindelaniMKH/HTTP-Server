import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    client, address = server.accept()
    request = client.recv(1024).decode()
    response = ("HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    "Content-Length: <your length here>\r\n"
    "\r\n"
    "<html><h1>Hello World</h1></html>")
    url = request.split('\r\n')[0]
    print(url)
    client.sendall(response.encode())
    client.close()