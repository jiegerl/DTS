#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: tiny_spider.py
@time: 2018/2/19/019 12:27
@desc:
"""

from abc import ABCMeta, abstractclassmethod


class TinySpider(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.spider = 'TinySpider'
        pass

    @abstractclassmethod
    def init_sys(self, str_conf_fp):
        """
        init system and check out if it can work
        :param str_conf_fp: config file path(XML)
        :return: dict includes system info
        """
        pass

    @abstractclassmethod
    def load_req(self, json_array_req=None):
        """
        create requests to download html
        :param json_array_req: target request json array
        :return: target url array
        """
        pass

    @abstractclassmethod
    def init_spider(self, dict_args=None):
        """
        prepare for spider
        :param dict_args: args for init
        :return:obj for spider
        """
        pass

    @abstractclassmethod
    def exec_spider(self, json_array_req, obj=None):
        """
        download html
        :param json_array_req: request json array
        :param obj: obj for spider, such as selenium browser
        :return:target movie response json array
        """
        pass

    @abstractclassmethod
    def exit_sys(self):
        """
        someday may be used
        :return:
        """
        pass

    def __str__(self):
        return str(self.spider)

    def __repr__(self):
        return repr(self.spider)
