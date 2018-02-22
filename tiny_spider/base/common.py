class Global:
    # message type
    __msg_node_type = 'node_message'
    __msg_req_type = 'req_message'
    __msg_res_type = 'res_message'
    # queue type
    __queue_node = 'node_queue'
    __queue_task = 'task_queue'
    __queue_req = 'req_queue'
    __queue_res = 'res_queue'
    # data in memory
    __data_node = 'node_data'
    __data_task = 'task_data'
    __data_req = 'req_data'
    __data_res = 'res_data'
    # operation of task
    __op_submit = 'submitted'
    __op_cancel = 'canceled'
    __op_pause = 'paused'
    __op_resume = 'resumed'
    # status of task
    __status_separating = 'separating'      # being separating
    __status_dispatching = 'dispatching'    # being dispatching
    __status_crawling = 'crawling'          # being crawling
    __status_collecting = 'collecting'      # being collecting
    __status_completed = 'completed'        # complete task
    __status_uncompleted = 'uncompleted'    # complete task error
    # status of node
    __status_active = 'active'              # active node
    __status_inactive = 'inactive'          # inactive node

    @staticmethod
    def get_status_active():
        return Global.__status_active

    @staticmethod
    def get_status_inactive():
        return Global.__status_inactive

    @staticmethod
    def get_status_separating():
        return Global.__status_separating

    @staticmethod
    def get_status_dispatching():
        return Global.__status_dispatching

    @staticmethod
    def get_status_crawling():
        return Global.__status_crawling

    @staticmethod
    def get_status_collecting():
        return Global.__status_collecting

    @staticmethod
    def get_status_completed():
        return Global.__status_completed

    @staticmethod
    def get_status_uncompleted():
        return Global.__status_uncompleted

    @staticmethod
    def get_msg_node():
        return Global.__msg_node_type

    @staticmethod
    def get_msg_req():
        return Global.__msg_req_type

    @staticmethod
    def get_msg_res():
        return Global.__msg_res_type

    @staticmethod
    def get_data_node():
        return Global.__data_node

    @staticmethod
    def get_data_task():
        return Global.__data_task

    @staticmethod
    def get_data_req():
        return Global.__data_req

    @staticmethod
    def get_data_res():
        return Global.__data_res

    @staticmethod
    def get_queue_node():
        return Global.__queue_node

    @staticmethod
    def get_queue_task():
        return Global.__queue_task

    @staticmethod
    def get_queue_req():
        return Global.__queue_req

    @staticmethod
    def get_queue_res():
        return Global.__queue_res

    @staticmethod
    def get_op_submit():
        return Global.__op_submit

    @staticmethod
    def get_op_cancel():
        return Global.__op_cancel

    @staticmethod
    def get_op_pause():
        return Global.__op_pause

    @staticmethod
    def get_op_resume():
        return Global.__op_resume
