import queue

from tiny_spider.base.decorator import singleton


@singleton
class QueueManager:

    def __new__(cls):
        cls.__queue_set = dict()
        return object.__new__(cls)

    def get(self, queue_type):
        if queue_type in self.__queue_set.keys():
            return self.__queue_set.get(queue_type)
        else:
            q = LocalQueue(queue_type)
            self.__queue_set[queue_type] = q
            return q


class LocalQueue:
    def __init__(self, queue_type):
        self.__queue_type = queue_type
        self.__queue = queue.Queue()

    @property
    def queue(self):
        return self.__queue

    @property
    def queue_type(self):
        return self.__queue_type

    def get(self):
        return self.__queue.get()
