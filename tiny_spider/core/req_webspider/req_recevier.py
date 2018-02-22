import json
import logging
import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.model.data import Request
from tiny_spider.net.tcp_manager import TCPManager


@singleton
class ReqReceiver(threading.Thread):
    def __new__(cls, *args, **kwargs):
        q = QueueManager()
        cls.__request_queue = q.get(Global.get_queue_req())
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
        obj_req = Request()
        obj_req.task_id = dict_req['task_id']
        obj_req.req_id = dict_req['req_id']
        obj_req.req_type = dict_req['req_type']
        obj_req.urls_count = dict_req['urls_count']
        obj_req.urls_args = dict_req['urls_args']
        self.__req_queue.put(obj_req)
        dict_ret = dict()
        dict_ret['req_status'] = Global.get_status_crawling()
        json_ret = json.dumps(dict_ret)
        sock.send(json_ret.encode('utf8'))
        sock.close()
        logging.info("received request %s from %s" % (dict_req, addr))
