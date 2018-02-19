import threading

import time

from tiny_spider.apps.cbo.movie_discoverer import MovieDiscoverer
from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager


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
        :return:negative number presents request data or system initial error;
                non negative number presents the count of fail urls.
        """
        dict_req = self.__req_queue.get()
        if 'req_type' in dict_req.keys():
            list_fail_urls = list()
            if dict_req['req_type'] == '0':  # cbo movie discoverer
                cbo_discoverer = MovieDiscoverer()
                res = cbo_discoverer.init_sys("conf/config.ini")
                if res == -1:
                    return -1
                list_urls = cbo_discoverer.load_req(dict_req['urls_args'])
                list_fail_urls = cbo_discoverer.exec_spider(list_urls)
            return len(list_fail_urls)
        else:
            return -1




