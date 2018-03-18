import xml

import logging

from tiny_spider.base import constant
from tiny_spider.base.decorator import singleton
from tiny_spider.model.data import Task
from tiny_spider.system.host_data import HostData
from tiny_spider.system.host_queue import HostQueue


@singleton
class Generator:
    def __new__(cls, *args, **kwargs):
        cls.__task_set = HostData().get(constant.DATA_TASK_KEY)
        cls.__task_queue = HostQueue().get(constant.QUEUE_TASK_KEY).queue
        return object.__new__(cls)

    def generate_from_file(self, file_path):
        """
            generate tasks
        """
        t = Task()
        t.task_id = '0'
        t.task_status = constant.STATUS_SEPARATE_KEY
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        parser.setContentHandler(t)
        parser.parse(file_path)
        self.__task_set[t.task_id] = t
        self.__task_queue.put(t)
        logging.info("generated task %s\n" % t.task_name)
        return 0
