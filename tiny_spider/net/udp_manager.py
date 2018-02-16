import socket


class UDPManager:
    def __init__(self):
        self.__schedule_ip = '127.0.0.1'
        self.__message_port = 9991

    def set_scheduler_msg_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.__schedule_ip, self.__message_port))
        return s

    def get_scheduler_msg_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((self.__schedule_ip, self.__message_port))
        return s
