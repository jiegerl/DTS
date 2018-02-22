import configparser
import logging
import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.data_manager import DataManager
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.model.data import Request


@singleton
class TaskSeparator(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__task_local_queue = q.get(Global.get_queue_task())
        cls.__req_local_queue = q.get(Global.get_queue_req())
        d = DataManager()
        cls.__data_task_set = d.get(Global.get_data_task())
        cls.__data_req_set = d.get(Global.get_data_req())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__task_queue = self.__task_local_queue.queue
        self.__req_queue = self.__req_local_queue.queue
        self.__task_set = self.__data_task_set
        self.__req_set = self.__data_req_set

    def run(self):
        logging.info("task separator started!")
        while True:
            self.separate_task()

    def separate_task(self):
        task = self.__task_queue.get()    # if empty, block here
        if int(task.task_type) == 0:
            conf = configparser.ConfigParser()
            conf.read(task.task_path)
            from_year = conf.getint('extend', 'from_year')
            to_year = conf.getint('extend', 'to_year')
            from_page = conf.getint('extend', 'from_page')
            to_page = conf.getint('extend', 'to_page')
            template_url = conf.get('base', 'template_url')
            logging.info("separating task's year from %s to req %s and its page from %d to %s\n" % (from_year, to_year, from_page, to_page))

            req_count = 0
            for item in range(from_year, to_year):
                for ele in range(from_page, to_page, 5):
                    req = Request()
                    req.task_id = task.task_id
                    req.req_id = task.task_id + "_" + str(req_count)
                    req.req_type = task.task_type
                    remain_page = to_page - ele
                    if remain_page < 5:
                        req.urls_count = remain_page
                    else:
                        req.urls_count = 5
                    dict_args = dict()
                    dict_args['from_year'] = item
                    dict_args['to_year'] = item + 1
                    dict_args['from_page'] = ele
                    dict_args['to_page'] = ele + req.urls_count
                    dict_args['template_url'] = template_url
                    req_count += 1
                    req.urls_args = dict_args
                    req.req_status = Global.get_status_dispatching()
                    self.__req_queue.put(req)
                    self.__req_set[req.req_id] = req
                    logging.info("separated task %s into req %s\n" % (task.task_id, req.req_id))

            self.__task_set[task.task_id].task_status = Global.get_status_dispatching()