import os

from tiny_spider.base.decorator import singleton


@singleton
class PathManager:
    def __new__(cls, root_path):
        return object.__new__(cls, root_path)

    def __init__(self, root_path):
        self.__root_path = root_path
        self.__conf_path = os.path.join(root_path,'/conf')
        self.__doc_path = os.path.join(root_path,'/doc')
        self.__log_path = os.path.join(root_path,'/logs')

    @property
    def root_path(self):
        return self.__root_path

    @root_path.setter
    def root_path(self, root_path):
        self.__root_path = root_path

    @property
    def conf_path(self):
        return self.__conf_path

    @conf_path.setter
    def conf_path(self, conf_path):
        self.__conf_path = conf_path

    @property
    def doc_path(self):
        return self.__doc_path

    @doc_path.setter
    def doc_path(self, doc_path):
        self.__doc_path = doc_path

    @property
    def log_path(self):
        return self.__log_path

    @log_path.setter
    def log_path(self, log_path):
        self.__log_path = log_path