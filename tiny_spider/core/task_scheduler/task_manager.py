#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: data_manager.py
@time: 2018/2/11/011 21:32
@desc: operation of task from users
"""
import json
import logging
import os
import struct
import threading
import xml.sax

from tiny_spider.core.data_manager import DataManager
from tiny_spider.model.data import Task
from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton
from tiny_spider.core.queue_manager import QueueManager
from tiny_spider.net.tcp_manager import TCPManager


@singleton
class TaskManager(threading.Thread):

    def __new__(cls):
        q = QueueManager()
        cls.__task_local_queue = q.get(Global.get_queue_task())
        d = DataManager()
        cls.__data_task_set = d.get(Global.get_data_task())
        return object.__new__(cls)

    def __init__(self):
        threading.Thread.__init__(self)
        self.__task_queue = self.__task_local_queue.queue
        self.__task_set = self.__data_task_set

    def run(self):
        """
        thread receives task submitted by tcp connection
        :return:
        """
        logging.info("task manager started!")
        t = TCPManager()
        s = t.set_cmd_connect()
        while True:
            sock, addr = s.accept()
            t = threading.Thread(target=self.manage_task, args=(sock, addr))
            t.start()

    def manage_task(self, sock, addr):
        data = ''
        while True:
            json_data = sock.recv(1024)
            if json_data:
                data += json_data
            else:
                break
        sock.close()
        dict_data = json.loads(data)
        if 'op_type' not in dict_data.keys():
            logging.error('invalid operation message.\n ')
        else:
            op_type = dict_data['op_type']
            op_data = dict_data['op_data']
            if op_type == Global.get_op_submit():
                self.submit_task(op_data)
            elif op_type == Global.get_op_cancel():
                self.cancel_task(op_data)
            elif op_type == Global.get_op_pause():
                self.pause_task(op_data)
            elif op_type == Global.get_op_resume():
                self.resume_task(op_data)
            else:
                logging.error('unknown operation %s\n' % op_type)
        logging.info('received task %s from %s' % (data, addr))

    def submit_task(self, task_path):
        """
        accept task submitted by user using tcp connection
        :param task_path: user's task absolute file path
        :return:
        """
        file_name = os.path.basename(task_path)
        file_folder = 'doc/tasks/'
        new_file_path = os.path.join(file_folder, file_name)
        t = Task()
        t.task_id = '0'
        t.task_status = Global.get_status_separating()
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        parser.setContentHandler(t)
        parser.parse(new_file_path)
        self.__task_set[t.task_id] = t
        self.__task_queue.put(t)
        logging.info("submitted task %s from %s\n" % t.task_name)

    def cancel_task(self, op_data):
        pass

    def pause_task(self, op_data):
        pass

    def resume_task(self, op_data):
        pass
