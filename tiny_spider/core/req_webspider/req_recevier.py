import json
import logging
import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.core.req_webspider.msg_processor import MsgProcessor
from tiny_spider.model.task import Request
from tiny_spider.net.tcp_manager import TCPManager


@singleton
class ReqReceiver(threading.Thread):
    def __new__(cls, *args, **kwargs):
        q = QueueManager()
        cls.__request_queue = q.get(Global.get_req_preparing_type())
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
        else:
            dict_req = json.loads(json_req.decode('utf8'))
            obj_req = Request()
            obj_req.task_id = dict_req['task_id']
            obj_req.req_id = dict_req['req_id']
            obj_req.req_type = dict_req['req_type']
            obj_req.req_status = Global.get_req_crawling_type()
            obj_req.urls_count = dict_req['urls_count']
            obj_req.urls_args = dict_req['urls_args']
            self.__req_queue.put(obj_req)
            dict_msg = dict()
            dict_msg['task_id'] = obj_req.task_id
            dict_msg['req_id'] = obj_req.req_id
            dict_msg['req_status'] = obj_req.req_status
            json_msg = json.dumps(dict_msg)
            sock.send(json_msg)
            logging.info("received request %s from %s" % (dict_req, addr))
