#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: data.py
@time: 2018/2/21/021 21:33
@desc:
"""

import xml.sax


class Task(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.CurrentData = ""

        self.__task_id = ""
        self.__task_name = ""
        self.__task_type = ""
        self.__task_path = ""
        self.__task_status = ""

        self.__time_start = ""
        self.__time_stop = ""
        self.__time_collect = ""

        self.__requests_doing = ""
        self.__requests_undone = ""
        self.__requests_redo = ""
        self.__requests_done = ""
        self.__requests_count = ""
        self.__requests_percent = ""

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def task_id(self, task_id):
        self.__task_id = task_id

    @property
    def task_name(self):
        return self.__task_name

    @task_name.setter
    def task_name(self, task_name):
        self.__task_name = task_name

    @property
    def task_type(self):
        return self.__task_type

    @task_type.setter
    def task_type(self, task_type):
        self.__task_type = task_type

    @property
    def task_path(self):
        return self.__task_path

    @task_path.setter
    def task_path(self, task_path):
        self.__task_path = task_path

    @property
    def task_status(self):
        return self.__task_status

    @task_status.setter
    def task_status(self, task_status):
        self.__task_status = task_status

    @property
    def time_start(self):
        return self.__time_start

    @time_start.setter
    def time_start(self, time_start):
        self.__time_start = time_start

    @property
    def time_stop(self):
        return self.__time_stop

    @time_stop.setter
    def time_stop(self, time_stop):
        self.__time_stop = time_stop

    @property
    def requests_undone(self):
        return self.__requests_undone

    @requests_undone.setter
    def requests_undone(self, requests_undone):
        self.__requests_undone = requests_undone

    @property
    def requests_done(self):
        return self.__requests_done

    @requests_done.setter
    def requests_done(self, requests_done):
        self.requests_done = requests_done

    @property
    def requests_doing(self):
        return self.__requests_doing

    @requests_doing.setter
    def requests_doing(self, requests_doing):
        self.__requests_doing = requests_doing

    @property
    def requests_redo(self):
        return self.__requests_redo

    @requests_redo.setter
    def requests_redo(self, requests_redo):
        self.requests_redo = requests_redo

    @property
    def requests_count(self):
        return self.__requests_count

    @requests_count.setter
    def requests_count(self, requests_count):
        self.__requests_count = requests_count

    @property
    def requests_percent(self):
        return self.__requests_percent

    @requests_percent.setter
    def requests_percent(self, requests_percent):
        self.__requests_percent = requests_percent

    def startElement(self, tag_name, attrs):
        self.CurrentData = tag_name

    def endElement(self, tag_name):
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == 'Task_Type':
            self.task_type = content
        elif self.CurrentData == 'Task_Name':
            self.task_name = content
        elif self.CurrentData == 'Task_Path':
            self.task_path = content


class Request:
    def __init__(self):
        self.__task_id = None
        self.__req_id = None
        self.__req_type = None
        self.__req_status = None

        self.__time_start = None
        self.__time_stop = None
        self.__time_counter = None

        self.__urls_count = None
        self.__urls_args = None  # dict

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def task_id(self, task_id):
        self.__task_id = task_id

    @property
    def req_id(self):
        return self.__req_id

    @req_id.setter
    def req_id(self, req_id):
        self.__req_id = req_id

    @property
    def req_type(self):
        return self.__req_type

    @req_type.setter
    def req_type(self, req_type):
        self.__req_type = req_type

    @property
    def req_status(self):
        return self.__req_status

    @req_status.setter
    def req_status(self, req_status):
        self.__req_status = req_status

    @property
    def urls_count(self):
        return self.__urls_count

    @urls_count.setter
    def urls_count(self, urls_count):
        self.__urls_count = urls_count

    @property
    def urls_args(self):
        return self.__urls_args

    @urls_args.setter
    def urls_args(self, urls_args):
        self.__urls_args = urls_args


class Response:
    def __init__(self):
        self.__task_id = None
        self.__req_id = None
        self.__req_status = None

        self.__pages_count = None
        self.__pages_args = None

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def task_id(self, task_id):
        self.__task_id = task_id

    @property
    def req_id(self):
        return self.__req_id

    @req_id.setter
    def req_id(self, req_id):
        self.__req_id = req_id

    @property
    def req_status(self):
        return self.__req_status

    @req_status.setter
    def req_status(self, req_status):
        self.__req_status = req_status

    @property
    def pages_count(self):
        return self.__pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        self.__pages_count = pages_count

    @property
    def pages_args(self):
        return self.__pages_args

    @pages_args.setter
    def pages_args(self, pages_args):
        self.__pages_args = pages_args


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
        super().__init__(node_ip, node_status)


class WebSpiderNode(LocalNode):
    def __init__(self, node_ip, node_status):
        super().__init__(node_ip, node_status)
