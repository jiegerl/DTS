from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager


@singleton
class NodeManager:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        q = QueueManager()
        node_type = Global.get_node_all_type()
        self.__node_queue = q.get(node_type).queue
        self.__node_set = dict()
        self.__node_cnt = 0

    @property
    def node_queue(self):
        return self.__node_queue

    def get(self, node_ip):
        if node_ip in self.__node_set.keys():
            return self.__node_set[node_ip]
        else:
            return None

    def set(self, node):
        node_ip = node.node_ip
        self.__node_queue.put(node)
        self.__node_set[node_ip] = node


class LocalNode:
    def __init__(self, node_ip, node_status):
        self.__node_ip = node_ip
        self.__node_status = node_status

    @property
    def node_ip(self):
        return self.__node_ip

    @property
    def node_status(self):
        return self.__node_status
