import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

def request_page(page):
    with open(page, 'r') as file:
        raw_html = file.read()
    return raw_html

def send_data(client, response):
    client.sendall(response.encode())

while True:
    client, address = server.accept()
    request = client.recv(1024).decode()

    url = request.split('\r\n')[0]
    method = url.split(' ')[0]
    path = url.split(' ')[1]

    if path == '/' and method == 'GET':
        page = request_page('/home/lindelani-mkhaliphi/Documents/Scripts/HttpServer/Pages/index.html')

        response = ("HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(page)}\r\n"
        "\r\n"
        f"{page}")

        send_data(client, response)

    elif path == '/why' and method == 'GET':
        page = request_page('/home/lindelani-mkhaliphi/Documents/Scripts/HttpServer/Pages/why.html')

        response = ("HTTP/1.1 200 OK\r\n"
        "Content_type: text/html\r\n"
        f"Content-Length: {len(page)}\r\n"
        "\r\n"
        f"{page}")

        send_data(client, response)

    elif path == '/favicon.ico' and method == 'GET':
        print("Exit")

    elif path == '/form' and method == 'GET':
        page = request_page('/home/lindelani-mkhaliphi/Documents/Scripts/HttpServer/Pages/form.html')

        response = ("HTTP/1.1 200 OK\r\n"
        "Content-type: text/html\r\n"
        f"Content-Length: {len(page)}\r\n"
        "\r\n"
        f"{page}"
        )

        send_data(client, response)
    
    elif path == '/form' and method == 'POST':

        print(repr(request))

        data = request.split('\r\n')[-1]

        data_lis = data.split('&')
        print(data_lis)

    client.close()
    