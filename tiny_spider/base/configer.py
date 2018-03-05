import configparser

from tiny_spider.base.decorator import singleton
from tiny_spider.model.conf import Configure


@singleton
class Configer:
    def __new__(cls, conf_path):
        cls.__conf_path = conf_path
        cls.__conf_obj = Configure()
        return object.__new__(cls)

    @property
    def conf_path(self):
        return self.__conf_path

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
