#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: queue.py
@time: 2018/2/21/021 23:08
@desc: manage the queue of task, request, response and node
"""


from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.model.queue import TaskQueue, ReqQueue, ResQueue, NodeQueue, MsgQueue


@singleton
class QueueManager:

    def __new__(cls):
        cls.__queue_set = dict()
        return object.__new__(cls)

    def get(self, queue_type):
        if queue_type in self.__queue_set.keys():
            return self.__queue_set.get(queue_type)
        else:
            if queue_type == Global.get_queue_task():
                q = TaskQueue()
            elif queue_type == Global.get_queue_req():
                q = ReqQueue()
            elif queue_type == Global.get_queue_res():
                q = ResQueue()
            elif queue_type == Global.get_queue_node():
                q = NodeQueue()
            elif queue_type == Global.get_msg_node():
                q = MsgQueue()
            elif queue_type == Global.get_msg_req():
                q = MsgQueue()
            elif queue_type == Global.get_msg_res():
                q = MsgQueue()
            else:
                return None
            self.__queue_set[queue_type] = q
            return q



