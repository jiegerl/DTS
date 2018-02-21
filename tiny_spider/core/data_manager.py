#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: data_manager.py
@time: 2018/2/21/021 15:49
@desc: manage the task, request, response and node data in memory
"""
from tiny_spider.base.common import Global
from tiny_spider.base.decorator import singleton


@singleton
class DataManager:
    def __new__(cls):
        cls.__data_node_set = dict()
        cls.__data_task_set = dict()
        cls.__data_req_set = dict()
        cls.__data_res_set = dict()
        return object.__new__(cls)

    def __init__(self):
        pass

    def get(self, data_type, data_id):
        if data_type == Global.get_data_task():
            dict_data = self.__data_task_set
        elif data_type == Global.get_data_req():
            dict_data = self.__data_req_set
        elif data_type == Global.get_data_res():
            dict_data = self.__data_res_set
        elif data_type == Global.get_data_node():
            dict_data = self.__data_node_set
        else:
            return None

        if data_id in dict_data.keys():
            return dict_data[data_id]
        else:
            return None

    def set(self, data_type, data_obj):
        if data_type == Global.get_data_task():
            dict_data = self.__data_task_set
            data_id = data_obj.task_id
        elif data_type == Global.get_data_req():
            dict_data = self.__data_req_set
            data_id = data_obj.req_id
        elif data_type == Global.get_data_res():
            dict_data = self.__data_res_set
            data_id = data_obj.req_id
        elif data_type == Global.get_data_node():
            dict_data = self.__data_node_set
            data_id = data_obj.node_ip
        else:
            return -1
        dict_data[data_id] = data_obj
        return 0
