#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: queue.py
@time: 2018/2/21/021 22:33
@desc: queue for task and node
"""
import queue


class LocalQueue:
    def __init__(self):
        self.__queue = queue.Queue()

    @property
    def queue(self):
        return self.__queue

    def get(self):
        return self.__queue.get()

    def set(self, obj):
        self.__queue.put(obj)


class TaskQueue(LocalQueue):
    def __init__(self):
        super().__init__()


class ReqQueue(LocalQueue):
    def __init__(self):
        super().__init__()


class ResQueue(LocalQueue):
    def __init__(self):
        super().__init__()


class NodeQueue(LocalQueue):
    def __init__(self):
        super().__init__()
