import threading

import time

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.core.req_webspider.msg_processor import MsgProcessor
from tiny_spider.model.data import Request


@singleton
class ReqPreprocessor(threading.Thread):
    def __new__(cls, *args, **kwargs):
        q = QueueManager()
        cls.__req_msg_queue = q.get(Global.get_msg_req())
        cls.__req_data_queue = q.get(Global.get_queue_req())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__req_m_queue = self.__req_msg_queue.queue
        self.__req_d_queue = self.__req_data_queue.queue

    def run(self):
        while True:
            self.prepare_request()
            time.sleep(3)

    def prepare_request(self):
        dict_req = self.__req_queue.get()
        obj_req = Request()
        obj_req.req_id = dict_req
        self.__req_d_queue.put(obj_req)
