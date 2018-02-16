import json
import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.net.tcp_manager import TCPManager


@singleton
class ReqPreprocessor(threading.Thread):

    def prepare_request(self):
        while True:
            dict_req = self.__req_queue.get()
            print(dict_req)
