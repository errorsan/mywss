import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with ssl.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

