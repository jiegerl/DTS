class Global:
    __task_separating_type_key = "task_separating"
    __task_separated_type_key = "task_separated"
    __req_dispatching_type_key = "req_dispatching"
    __req_dispatched_type_key = "req_dispatched"
    __req_preparing_type_key = "req_preparing"
    __req_crawling_type_key = "req_crawling"
    __res_crawled_type_key = "res_crawled"
    __msg_received_type_key = 'msg_received'
    __node_active_status = 'node_active'
    __node_inactive_status = 'node_inactive'
    __node_all_type_key = 'node_all'
    __msg_node_type = 'node_message'
    __msg_req_type = 'req_message'

    @staticmethod
    def get_task_separating_type():
        return Global.__task_separating_type_key

    @staticmethod
    def get_task_separated_type():
        return Global.__task_separated_type_key

    @staticmethod
    def get_req_dispatching_type():
        return Global.__req_dispatching_type_key

    @staticmethod
    def get_req_dispatched_type():
        return Global.__req_dispatched_type_key

    @staticmethod
    def get_req_preparing_type():
        return Global.__req_preparing_type_key

    @staticmethod
    def get_req_crawling_type():
        return Global.__req_crawling_type_key

    @staticmethod
    def get_res_crawled_type():
        return Global.__res_crawled_type_key

    @staticmethod
    def get_msg_received_type():
        return Global.__msg_received_type_key

    @staticmethod
    def get_node_active_status():
        return Global.__node_active_status

    @staticmethod
    def get_node_inactive_status():
        return Global.__node_inactive_status

    @staticmethod
    def get_msg_node():
        return Global.__msg_node_type

    @staticmethod
    def get_msg_req():
        return Global.__msg_req_type

    @staticmethod
    def get_node_all_type():
        return Global.__node_all_type_key
