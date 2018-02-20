import threading

import time

from tiny_spider.apps.cbo.movie_discoverer import MovieDiscoverer
from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.core.req_webspider.msg_processor import MsgProcessor
from tiny_spider.model.task import Response


@singleton
class ReqDownloader(threading.Thread):
    def __new__(cls, *args, **kwargs):
        q = QueueManager()
        cls.__request_queue = q.get(Global.get_req_crawling_type())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__req_queue = self.__request_queue.queue

    def run(self):
        while True:
            self.download_page()
            time.sleep(3)

    def download_page(self):
        """
        S.download_page() -> int

        Download html page according to type of source page.
        :return: negative number presents request data or system initial error;
                 non negative number presents the count of fail urls.
        """
        obj_req = self.__req_queue.get()
        list_urls = list()
        list_fail_urls = list()
        if obj_req.req_type == '0':  # cbo movie discoverer
            cbo_discoverer = MovieDiscoverer()
            res = cbo_discoverer.init_sys("conf/config.ini")
            if res == -1:
                return -1
            list_urls = cbo_discoverer.load_req(obj_req.urls_args)
            list_fail_urls = cbo_discoverer.exec_spider(list_urls)
        pages_count = len(list_urls) - len(list_fail_urls)
        obj_res = Response()
        obj_res.task_id = obj_req.task_id
        obj_res.req_id = obj_req.req_id
        obj_res.req_status = Global.get_res_crawled_type()
        obj_res.pages_count = pages_count
        obj_res.pages_args = dict()
        mp = MsgProcessor()
        mp.send_res_msg(obj_res)
        return len(list_fail_urls)





