class Node:
    def __init__(self, node_ip, node_type, node_status):
        self.__node_ip = node_ip
        self.__node_type = node_type
        self.__node_status = node_status

    @property
    def node_ip(self):
        return self.__node_ip

    @property
    def node_type(self):
        return self.__node_type

    @property
    def node_status(self):
        return self.__node_status


class SchedulerNode(Node):
    def __init__(self, node_ip, node_status, node_type='s'):
        super().__init__(node_ip, node_type, node_status)


class WebSpiderNode(Node):
    def __init__(self, node_ip, node_status, node_type='w'):
        super().__init__(node_ip, node_type, node_status)


class ManagerNode(Node):
    def __init__(self, node_ip, node_status, node_type='m'):
        super().__init__(node_ip, node_type, node_status)
