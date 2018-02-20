import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager


@singleton
class TaskCollector(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__task_separating_queue = q.get(Global.get_res_crawled_type())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pass

    def collect_res(self):
        pass
