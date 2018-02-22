import json

from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.net.udp_manager import UDPManager


@singleton
class MsgProcessor:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        self.__s_msg_conn = UDPManager().get_scheduler_msg_connect()

    def send_comm_msg(self, dict_msg):
        s = self.__s_msg_conn
        json_res = json.dumps(dict_msg)
        s.sendto(json_res.encode('utf8'), s.getpeername())
        s.close()
        return 0

    def send_node_msg(self, obj_node):
        dict_msg = dict()
        dict_msg['message_type'] = Global.get_msg_node()
        dict_msg['node_ip'] = obj_node.node_ip
        dict_msg['node_status'] = obj_node.node_status
        self.send_comm_msg(dict_msg)
        return 0

    def send_res_msg(self, obj_res):
        dict_msg = dict()
        dict_msg['message_type'] = Global.get_msg_res()
        dict_msg['task_id'] = obj_res.task_id
        dict_msg['req_id'] = obj_res.req_id
        dict_msg['req_status'] = obj_res.req_status
        dict_msg['pages_count'] = obj_res.pages_count
        dict_msg['pages_args'] = obj_res.pages_args
        self.send_comm_msg(obj_res)
        return 0