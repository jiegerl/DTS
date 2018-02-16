#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: main.py
@time: 2018/2/12/012 9:40
@desc:
"""
import sys

from tiny_spider.core.opt_processor.cmd_processor import CmdProcessor
from tiny_spider.core.scheduler import Scheduler

if __name__ == '__main__':
    t = Scheduler()
    t.start()
