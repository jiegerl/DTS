import configparser
import time

import logging

from tiny_spider.base import constant
from tiny_spider.base.decorator import singleton
from tiny_spider.model.data import Request
from tiny_spider.processor import cbo_download_page
from tiny_spider.system.host_data import HostData
from tiny_spider.system.host_queue import HostQueue


@singleton
class Scheduler:

    def __new__(cls):
        q = HostQueue()
        cls.__task_queue = q.get(constant.QUEUE_TASK_KEY).queue
        cls.__reqs_queue = q.get(constant.QUEUE_REQS_KEY).queue
        d = HostData()
        cls.__task_set = d.get(constant.DATA_TASK_KEY)
        cls.__reqs_set = d.get(constant.DATA_REQS_KEY)
        return object.__new__(cls)

    def separate_task_into_request(self):
        while True:
            task = self.__task_queue.get()  # if empty, block here
            if int(task.task_type) == 0:
                conf = configparser.ConfigParser()
                conf.read(task.task_path)
                from_year = conf.getint('extend', 'from_year')
                to_year = conf.getint('extend', 'to_year')
                from_page = conf.getint('extend', 'from_page')
                to_page = conf.getint('extend', 'to_page')
                # template_url = conf.get('base', 'template_url')
                template_url = 'http://www.cbooo.cn/Mdata/getMdata_movie?area=50&year=%s&pIndex=%s'
                logging.info("separating task's year from %s to %s and its page from %d to %s\n" % (
                from_year, to_year, from_page, to_page))

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
                        req.req_status = constant.STATUS_DISPATCH_KEY
                        self.__reqs_queue.put(req)
                        self.__reqs_set[req.req_id] = req
                        logging.info("separated task %s into req %s\n" % (task.task_id, req.req_id))

                self.__task_set[task.task_id].task_status = constant.STATUS_DISPATCH_KEY

    def dispatch_request_to_processor(self):
        while True:
            obj_req = self.__reqs_queue.get()
            result = cbo_download_page.delay(obj_req)
            while not result.ready():
                time.sleep(1)
            print('task done:{0}'.format(result.get()))
