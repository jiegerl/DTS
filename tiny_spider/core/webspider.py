from tiny_spider.base.common import Global
from tiny_spider.base.logger import Logger
from tiny_spider.base.decorator import singleton
from tiny_spider.core.req_webspider.req_downloader import ReqDownloader
from tiny_spider.core.req_webspider.req_preprocessor import ReqPreprocessor
from tiny_spider.core.req_webspider.req_recevier import ReqReceiver
from tiny_spider.core.req_webspider.msg_processor import MsgProcessor


@singleton
class WebSpider:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.__instance = 0

    def start(self):
        if self.__instance:
            print("Spider is already running...")
        else:
            print("Spider is already starting...")
            self.__instance = 1
            cn_logger = Logger('c')
            cn_logger.execute()

            mp = MsgProcessor('127.0.0.1')
            mp.send_node_msg(Global.get_node_active_status())

            rp = ReqReceiver('127.0.0.1')
            rp.start()

            rc = ReqPreprocessor()
            rc.start()

            rd = ReqDownloader()
            rd.start()
