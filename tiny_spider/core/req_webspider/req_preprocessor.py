import threading

import time

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager


@singleton
class ReqPreprocessor(threading.Thread):
    def __new__(cls, *args, **kwargs):
        q = QueueManager()
        cls.__req_preparing_queue = q.get(Global.get_req_preparing_type())
        cls.__req_crawling_queue = q.get(Global.get_req_crawling_type())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__preparing_queue = self.__req_preparing_queue.queue
        self.__crawling_queue = self.__req_crawling_queue.queue

    def run(self):
        while True:
            self.prepare_request()
            time.sleep(3)

    def prepare_request(self):
        dict_req = self.__preparing_queue.get()
        self.__crawling_queue.put(dict_req)