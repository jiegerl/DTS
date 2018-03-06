import os

from tiny_spider.base.decorator import singleton


@singleton
class PathUtils:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.__conf_path = os.path.join('..', 'conf', 'config.ini')
        self.__docs_path = os.path.join('..', 'docs')
        self.__logs_path = os.path.join('..', 'logs')

    @property
    def conf_path(self):
        return self.__conf_path

    @conf_path.setter
    def conf_path(self, conf_path):
        self.__conf_path = conf_path

    @property
    def docs_path(self):
        return self.__docs_path

    @docs_path.setter
    def docs_path(self, docs_path):
        self.__docs_path = docs_path

    @property
    def logs_path(self):
        return self.__logs_path

    @logs_path.setter
    def logs_path(self, logs_path):
        self.__logs_path = logs_path
