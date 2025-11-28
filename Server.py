import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

while True:
    client, address = server.accept()
    request = client.recv(1024).decode()

    with open('index.html', 'r') as file:
        raw_html = file.read()

    response = ("HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html\r\n"
    f"Content-Length: {len(raw_html)}r\n"
    "\r\n"
    f"{raw_html}")

    url = request.split('\r\n')[0]
    print(url)
    client.sendall(response.encode())
    client.close()
    