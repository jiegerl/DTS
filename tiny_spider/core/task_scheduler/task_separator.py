import logging
import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.model.task import Request


@singleton
class TaskSeparator(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__task_separating_queue = q.get(Global.get_task_separating_type())
        cls.__task_separated_queue = q.get(Global.get_task_separated_type())
        cls.__req_dispatching_queue = q.get(Global.get_req_dispatching_type())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        q = self.__task_separating_queue.queue
        self.__separating_queue = q
        p = self.__task_separated_queue.queue
        self.__task_separated_queue = p
        t = self.__req_dispatching_queue.queue
        self.__req_dispatching_queue = t

    def run(self):
        logging.info("task separator started!")
        while True:
            self.separate_task()

    def separate_task(self):
        task = self.__separating_queue.get()    # if empty, block here

        req = Request()
        req.task_id = task.task_id
        req.req_id = task.task_id
        req.req_path = task.task_path
        req.req_type = task.task_type
        req.urls_count = 0
        req.urls_set = list()

        self.__req_dispatching_queue.put(req)
        self.__task_separated_queue.put(task)
        logging.info("separated task %s into req %s\n" % task, req)
