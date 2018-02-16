#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: task_manager.py
@time: 2018/2/11/011 21:32
@desc:
"""
import logging
import os
import struct
import threading
import xml.sax

from tiny_spider.model.task import Task
from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.net.tcp_manager import TCPManager


@singleton
class TaskManager(threading.Thread):
    _instance = None

    def __new__(cls):
        cls.__task_separating_queue = QueueManager().get(Global.get_task_separating_type())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        q = self.__task_separating_queue.queue
        self.__separating_queue = q

    @property
    def separating_queue(self):
        return self.__separating_queue

    def run(self):
        """
        thread receives task submitted by tcp connection
        :return:
        """
        logging.info("task manager started!")
        t = TCPManager()
        s = t.set_cmd_submitter_connect()
        while True:
            sock, addr = s.accept()
            t = threading.Thread(target=self.submit_task, args=(sock, addr))
            t.start()

    def submit_task(self, sock, addr):
        """

        :param sock:
        :param addr:
        :return:
        """
        new_file_name = ''
        while True:
            file_info_size = struct.calcsize('128sl')
            buf = sock.recv(file_info_size)
            if buf:
                file_name, file_size = struct.unpack('128sl', buf)
                fn = file_name.decode('utf8').strip('\00')
                new_file_name = os.path.join('./', 'new_' + fn)

                data_size = 0
                fp = open(new_file_name, 'wb')

                while not data_size == file_size:   # not fully completed
                    if file_size - data_size > 1024:
                        data = sock.recv(1024)
                        data_size += len(data)
                    else:
                        data = sock.recv(file_size - data_size)
                        data_size = file_size
                    fp.write(data)
                fp.close()
            sock.close()
            break

        t = Task()
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        parser.setContentHandler(t)
        parser.parse(new_file_name)

        self.__separating_queue.put(t)
        logging.info("submitted task %s from %s\n" % t, addr)
