#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: conf.py
@time: 2018/3/5/005 22:00
@desc:
"""


class Configure:

    def __init__(self):

        self.__sdl_ip = None

        self.__dsp_port = None
        self.__msg_port = None
        self.__rdc_port = None
        self.__cmd_port = None

    @property
    def sdl_ip(self):
        return self.__sdl_ip

    @sdl_ip.setter
    def sdl_ip(self, sdl_ip):
        self.__sdl_ip = sdl_ip

    @property
    def dsp_port(self):
        return self.__dsp_port

    @dsp_port.setter
    def dsp_port(self, dsp_port):
        self.__dsp_port = dsp_port

    @property
    def msg_port(self):
        return self.__msg_port

    @msg_port.setter
    def msg_port(self, msg_port):
        self.__msg_port = msg_port

    @property
    def rdc_port(self):
        return self.__rdc_port

    @rdc_port.setter
    def rdc_port(self, rdc_port):
        self.__rdc_port = rdc_port

    @property
    def cmd_port(self):
        return self.__cmd_port

    @cmd_port.setter
    def cmd_port(self, cmd_port):
        self.__cmd_port = cmd_port