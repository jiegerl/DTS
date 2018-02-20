import json
import threading

import logging

from tiny_spider.net.tcp_manager import TCPManager
from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.node_manager import NodeManager
from tiny_spider.core.queue_manager import QueueManager


@singleton
class ReqDispatcher(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__req_dispatching_queue = q.get(Global.get_req_dispatching_type())
        cls.__req_dispatched_queue = q.get(Global.get_req_dispatched_type())
        return object.__new__(cls)

    def __init__(self, ip="127.0.0.1"):
        threading.Thread.__init__(self)
        self.__node_ip = ip
        p = self.__req_dispatching_queue
        self.__dispatching_queue = p.queue
        q = self.__req_dispatched_queue
        self.__dispatched_queue = q.queue

    def run(self):
        logging.info("request dispatcher started!")
        while True:
            self.dispatch_req()

    def dispatch_req(self):
        # initial data
        req = self.__dispatching_queue.get()
        dict_req = dict()
        dict_req["task_id"] = req.task_id
        dict_req["req_id"] = req.req_id
        dict_req["req_type"] = req.req_type
        dict_req["urls_count"] = req.urls_count
        dict_req["urls_args"] = req.urls_args
        json_req = json.dumps(dict_req)
        # node select
        node_queue = NodeManager().node_queue
        node = node_queue.get()
        # tcp connect
        s = TCPManager().get_dispatcher_connect(node.node_ip)
        s.send(json_req.encode("utf8"))
        json_ret = s.recv(1024)
        if not json_ret:
            logging.info("received empty return data %s" % json_ret)
        else:
            dict_ret = json.loads(json_ret.decode('utf8'))
            if dict_ret['req_status'] == Global.get_req_crawling_type():
                self.__dispatched_queue.put(req)
                logging.info("dispatched req %s to %s success\n" % (req.req_id, node.node_ip))
            else:
                logging.error("dispatched req %s to %s fail\n" % (req.req_id, node.node_ip))
        # nodes in turns
        node_queue.put(node)
