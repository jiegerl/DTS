import json
import threading

import logging

from tiny_spider.core.data_manager import DataManager
from tiny_spider.net.tcp_manager import TCPManager
from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager


@singleton
class ReqDispatcher(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__req_local_queue = q.get(Global.get_queue_req())
        cls.__node_local_queue = q.get(Global.get_queue_node())
        d = DataManager()
        cls.__data_req_set = d.get(Global.get_data_req())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__req_queue = self.__req_local_queue.queue
        self.__node_queue = self.__node_local_queue.queue
        self.__req_set = self.__data_req_set

    def run(self):
        logging.info("request dispatcher started!")
        while True:
            self.dispatch_req()

    def dispatch_req(self):
        # initial data
        req = self.__req_queue.get()
        dict_req = dict()
        dict_req["task_id"] = req.task_id
        dict_req["req_id"] = req.req_id
        dict_req["req_type"] = req.req_type
        dict_req["urls_count"] = req.urls_count
        dict_req["urls_args"] = req.urls_args
        json_req = json.dumps(dict_req)
        # node select
        node_queue = self.__node_queue
        node = node_queue.get()
        # tcp connect
        s = TCPManager().get_dispatcher_connect(node.node_ip)
        s.send(json_req.encode("utf8"))
        json_ret = s.recv(1024)
        logging.info("received return data %s\n" % json_ret)
        if not json_ret:
            # the response from web spider is empty
            logging.info("received empty return data\n")
        else:
            # handle the response from web spider
            obj_req = self.__req_set[req.req_id]
            dict_ret = json.loads(json_ret.decode('utf8'))
            if dict_ret['req_status'] == Global.get_status_crawling():
                obj_req.req_status = Global.get_status_collecting()
                logging.info("dispatched req %s to %s success\n" % (req.req_id, node.node_ip))
            else:
                obj_req.req_status = Global.get_status_uncompleted()
                logging.error("dispatched req %s to %s fail\n" % (req.req_id, node.node_ip))
        # nodes in turns
        node_queue.put(node)
