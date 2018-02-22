import socket


class TCPManager:
    def __init__(self):
        self.__schedule_ip = '127.0.0.1'
        self.__dispatch_port = 8008
        self.__submit_port = 8181

    def set_dispatcher_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', self.__dispatch_port))
        s.listen(5)
        return s

    def get_dispatcher_connect(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, self.__dispatch_port))
        return s

    def set_cmd_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.__schedule_ip, self.__submit_port))
        s.listen(5)
        return s

    def get_cmd_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__schedule_ip, self.__submit_port))
        return s
