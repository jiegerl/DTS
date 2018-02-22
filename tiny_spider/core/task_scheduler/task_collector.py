import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.data_manager import DataManager
from tiny_spider.core.queue_manager import QueueManager


@singleton
class TaskCollector(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__res_local_queue = q.get(Global.get_queue_res())
        d = DataManager()
        cls.__req_data_set = d.get(Global.get_data_req())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__res_queue = self.__res_local_queue.queue
        self.__req_set = self.__req_data_set

    def run(self):
        while True:
            self.collect_res()

    def collect_res(self):
        res = self.__res_queue.get()
