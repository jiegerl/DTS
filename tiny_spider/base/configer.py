import configparser

import os

from tiny_spider.base.decorator import singleton
from tiny_spider.model.conf import Configure
from tiny_spider.utils.path_manager import PathUtils


@singleton
class Configer:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        pu = PathUtils(os.getcwd())
        conf_path = pu.conf_path
        self.__conf_path = conf_path
        self.__conf_obj = Configure()

    @property
    def conf_obj(self):
        return self.__conf_obj

    def apply_conf(self):
        conf = configparser.ConfigParser()
        conf.read(self.__conf_path)
        conf_obj = self.conf_obj
        conf_obj.sdl_ip = conf.get('ip', 'sdl_ip')
        conf_obj.cmd_port = conf.get('port', 'cmd_port')
        conf_obj.dsp_port = conf.get('port', 'dsp_port')
        conf_obj.msg_port = conf.get('port', 'msg_port')
        conf_obj.rdc_port = conf.get('port', 'rdc_port')
        return 0
