import json
import threading

import logging

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.data_manager import DataManager
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.model.data import WebSpiderNode, Response
from tiny_spider.net.udp_manager import UDPManager


@singleton
class MsgProcessor(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__nd_msg_queue = q.get(Global.get_msg_node())
        cls.__rs_msg_queue = q.get(Global.get_msg_res())
        cls.__rq_msg_queue = q.get(Global.get_msg_req())
        cls.__n_queue = q.get(Global.get_queue_node())
        cls.__res_local_queue = q.get(Global.get_queue_res())
        d = DataManager()
        cls.__data_res_set = d.get(Global.get_data_req())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__node_msg_queue = self.__nd_msg_queue.queue
        self.__res_msg_queue = self.__rs_msg_queue.queue
        self.__req_msg_queue = self.__rq_msg_queue.queue
        self.__node_queue = self.__n_queue.queue
        self.__res_queue = self.__res_local_queue.queue
        self.__res_set = self.__data_res_set

    def run(self):
        logging.info('message receiver for scheduler started!')
        s = UDPManager().set_scheduler_msg_connect()
        while True:
            json_data, addr = s.recvfrom(1024)
            t = threading.Thread(target=self.receive_message, args=(json_data, addr))
            t.start()

    def receive_message(self, json_data, addr):
        logging.info('received message[%s]' % json_data.decode('utf8'))
        dict_data = json.loads(json_data.decode('utf8'))
        dict_msg = dict()
        dict_msg['ip'] = addr   # sock
        dict_msg['msg'] = dict_data
        msg_type = dict_data['message_type']
        if msg_type == Global.get_msg_node():
            self.__node_msg_queue.put(dict_msg)
            self.process_node_message()
            logging.info('processed node message[%s]' % dict_msg)
        elif msg_type == Global.get_msg_res():
            self.__res_msg_queue.put(dict_msg)
            self.process_res_message()
            logging.info('processed res message[%s]' % dict_msg)
        else:
            logging.error('skipped message[%s]' % dict_msg)

    def process_node_message(self):
        dict_msg = self.__node_msg_queue.get()
        msg = dict_msg['msg']
        node_ip = msg['node_ip']
        node_status = msg['node_status']
        node = WebSpiderNode(node_ip, node_status)
        nm = DataManager()
        dict_node_set = nm.get(Global.get_data_node())
        dict_node_set[node.node_ip] = node
        self.__node_queue.put(node)

    def process_res_message(self):
        dict_msg = self.__res_msg_queue.get()
        msg = dict_msg['msg']
        obj_res = Response()
        obj_res.task_id = msg['task_id']
        obj_res.req_id = msg['req_id']
        obj_res.req_id = msg['req_status']
        obj_res.pages_count = msg['pages_count']
        obj_res.pages_args = msg['pages_args']
        self.__res_queue.put(obj_res)
        self.__res_set[obj_res.req_id] = obj_res