import json
import logging
import threading
import time

from tiny_spider.base.common import Global
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.net.tcp_manager import TCPManager


class ReqReceiver(threading.Thread):
    def __new__(cls, *args, **kwargs):
        q = QueueManager()
        cls.__request_queue = q.get(Global.get_req_crawling_type())
        return object.__new__(cls)

    def __init__(self, node_ip):
        threading.Thread.__init__(self)
        self.__req_queue = self.__request_queue.queue
        self.__node_ip = node_ip

    def run(self):
        logging.info("requests receiver started!")
        s = TCPManager().set_dispatcher_connect()
        while True:
            sock, addr = s.accept()
            t = threading.Thread(target=self.receive_request, args=(sock, addr))
            t.start()

    def receive_request(self, sock, addr):
        json_req = sock.recv(1024)
        if not json_req:
            logging.info("received empty request %s" % json_req)
        dict_req = json.loads(json_req.decode('utf8'))
        self.__req_queue.put(dict_req)
        logging.info("received request %s from %s" % dict_req, addr)
