#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: node.py
@time: 2018/3/4/004 21:45
@desc:
"""


class LocalNode:

    def __init__(self, node_ip, node_status):
        self.__node_ip = node_ip
        self.__node_status = node_status

    @property
    def node_ip(self):
        return self.__node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        self.__node_ip = node_ip

    @property
    def node_status(self):
        return self.__node_status

    @node_status.setter
    def node_status(self, node_status):
        self.__node_status = node_status


class SchedulerNode(LocalNode):

    def __init__(self, node_ip, node_status):
        super(SchedulerNode, self).__init__(node_ip, node_status)


class WebSpiderNode(LocalNode):
    def __init__(self, node_ip, node_status):
        super(WebSpiderNode, self).__init__(node_ip, node_status)
