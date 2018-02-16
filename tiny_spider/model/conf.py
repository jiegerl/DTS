class Configure:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Configure, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.__dispatch_port = 9999
        self.__reduce_port = 9998
        self.__message_port = 9997

    @property
    def dispatch_port(self):
        return self.__dispatch_port

    @property
    def reduce_port(self):
        return self.__reduce_port

    @property
    def message_port(self):
        return self.__message_port
