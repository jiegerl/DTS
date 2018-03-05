import socket

import os

from tiny_spider.base.configer import Configer
from tiny_spider.base.decorator import singleton
from tiny_spider.utils.path_manager import PathUtils


@singleton
class TCPManager:

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        conf_obj = Configer().conf_obj
        self.__sdl_ip = conf_obj.sdl_ip
        self.__dsp_port = conf_obj.dsp_port
        self.__cmd_port = conf_obj.cmd_port

    def set_dispatcher_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.__sdl_ip, self.__dsp_port))
        s.listen(5)
        return s

    def get_dispatcher_connect(self, dsp_ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((dsp_ip, self.__dsp_port))
        return s

    def set_cmd_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.__sdl_ip, self.__cmd_port))
        s.listen(5)
        return s

    def get_cmd_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.__sdl_ip, self.__cmd_port))
        return s
