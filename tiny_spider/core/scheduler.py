from tiny_spider.base.logger import Logger
from tiny_spider.base.decorator import singleton
from tiny_spider.core.task_scheduler.msg_processor import MsgProcessor
from tiny_spider.core.task_scheduler.task_manager import TaskManager
from tiny_spider.core.task_scheduler.task_separator import TaskSeparator
from tiny_spider.core.task_scheduler.task_dispatcher import ReqDispatcher


@singleton
class Scheduler:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.__instance = 0

    def start(self):
        if self.__instance:
            print("Scheduler is already running...\n")
        else:
            print("Scheduler is already starting...\n")
            self.__instance = 1
            sn_logger = Logger('s')
            sn_logger.execute()

            mp = MsgProcessor()
            mp.start()

            tm = TaskManager()
            tm.start()

            ts = TaskSeparator()
            ts.start()

            r = ReqDispatcher()
            r.start()
