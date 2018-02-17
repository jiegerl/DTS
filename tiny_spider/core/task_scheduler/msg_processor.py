import json
import time
import threading

import logging

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.node_manager import NodeManager, LocalNode
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.net.udp_manager import UDPManager


@singleton
class MsgProcessor(threading.Thread):
    def __new__(cls):
        q = QueueManager()
        cls.__node_msg = q.get(Global.get_msg_node())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__node_msg_queue = self.__node_msg.queue

    def run(self):
        logging.info('message receiver for scheduler started!')
        s = UDPManager().set_scheduler_msg_connect()
        t = threading.Thread(target=self.receive_message, args=(s,))
        t.start()

    def receive_message(self, sock):
        while True:
            json_data, addr = sock.recvfrom(1024)
            logging.info('received message[%s]' % json_data.decode('utf8'))
            dict_data = json.loads(json_data.decode('utf8'))
            dict_msg = dict()
            dict_msg['ip'] = addr
            dict_msg['msg'] = dict_data
            msg_type = dict_data['message_type']
            if msg_type == Global.get_msg_node():
                self.__node_msg_queue.put(dict_msg)
                self.process_node_message()
                logging.info('processed message[%s]' % dict_msg)
            else:
                logging.error('skipped message[%s]' % dict_msg)
            time.sleep(5)

    def process_node_message(self):
        dict_msg = self.__node_msg_queue.get()
        msg = dict_msg['msg']
        node_ip = msg['node_ip']
        node_status = msg['node_status']
        node = LocalNode(node_ip, node_status)
        nm = NodeManager()
        nm.set(node)
