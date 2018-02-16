import logging
import os

from tiny_spider.utils.path_manager import PathManager


class Logger:
    def __init__(self, node_type):
        self.__node_type = node_type

    def execute(self):
        logging.info("%s's logger started!" % self.__node_type)
        logging.basicConfig(level=logging.NOTSET)
        root_logger = logging.getLogger()
        log_folder = '../../'
        log_file_name = '%sn.log' % self.__node_type
        log_file_path = os.path.join(log_folder, log_file_name)
        file_handler = logging.FileHandler(log_file_path)
        root_logger.addHandler(file_handler)