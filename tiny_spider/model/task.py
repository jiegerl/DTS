import xml.sax


class Task(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.CurrentData = ""

        self.__task_id = ""
        self.__task_name = ""
        self.__task_type = ""
        self.__task_path = ""

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
        pass

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
        self.__req_path = None

        self.__time_start = None
        self.__time_stop = None
        self.__time_counter = None

        self.__urls_count = None
        self.__urls_set = None

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
    def req_path(self):
        return self.__req_path

    @req_path.setter
    def req_path(self, req_path):
        self.__req_path = req_path


class Response:
    def __init__(self):
        self.__task_id = None
        self.__req_id = None

        self.__pages_count = None
        self.__pages_path = None
        self.__pages_set = None


class Url:
    def __init__(self):
        self.__url_type = None
        self.__url_base = None
        self.__url_args = None
