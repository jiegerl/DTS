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
        pu = PathUtils()
        conf_path = pu.conf_path
        self.__conf_path = conf_path
        self.__conf_obj = Configure()

    @property
    def conf_obj(self):
        return self.__conf_obj

    def check_conf(self):
        conf_obj = self.__conf_obj
        # check if IP is valid
        pass
        # check if PORT is valid
        if not conf_obj.dsp_port.isdigit():
            return 1
        if not conf_obj.cmd_port.isdigit():
            return 2
        if not conf_obj.msg_port.isdigit():
            return 3
        if not conf_obj.rdc_port.isdigit():
            return 4
        return 0

    def apply_conf(self):
        conf = configparser.ConfigParser()
        conf.read(self.__conf_path)
        conf_obj = self.conf_obj
        conf_obj.sdl_ip = conf.get('IP', 'SDL_IP')
        conf_obj.cmd_port = conf.get('PORT', 'CMD_port')
        conf_obj.dsp_port = conf.get('PORT', 'DSP_PORT')
        conf_obj.msg_port = conf.get('PORT', 'MSG_PORT')
        conf_obj.rdc_port = conf.get('PORT', 'RDC_PORT')
        return 0
