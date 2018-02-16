import json
import logging
import threading

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.net.udp_manager import UDPManager


@singleton
class MsgProcessor(threading.Thread):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, node_ip):
        threading.Thread.__init__(self)
        self.__node_ip = node_ip

    @property
    def node_ip(self):
        return self.__node_ip

    def run(self):
        self.send_node_msg(Global.get_node_active_status())

    def send_node_msg(self, node_status):
        s = UDPManager().get_scheduler_msg_connect()
        dict_msg = dict()
        dict_msg['message_type'] = Global.get_msg_node()
        dict_msg['node_ip'] = self.__node_ip
        dict_msg['node_status'] = node_status
        json_msg = json.dumps(dict_msg)
        s.sendto(json_msg.encode('utf8'), s.getpeername())
