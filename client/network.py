import socket
import json


class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = ip.split(":")
        if ip[0] == "":
            self.host = socket.gethostbyname(socket.gethostname())
        else:
            self.host = ip[0]
        self.port = int(ip[1])
        self.addr = (self.host, self.port)
        self.connect()

    def connect(self):
        self.client.connect(self.addr)

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            response = self.client.recv(2048).decode()
            return response
        except socket.error as e:
            return str(e)