import json
import logging
import os
import struct


from tiny_spider.base.common import Global
from tiny_spider.net.tcp_manager import TCPManager


class TaskProcessor:
    @staticmethod
    def process_task(op_type, op_data):
        """
        TaskProcessor.process_task(op_type, op_data)

        :param op_type: submit, cancel, pause or resume
        :param op_data: dict data of operation
        :return: 0 if process successfully. -1 represents error, otherwise.
        """
        if op_type == Global.get_op_submit():
            dict_op_msg = TaskProcessor.submit_task(op_data)
            logging.info('submit task %s\n' % dict_op_msg)
        else:
            # except submitting task
            if 'task_id' not in op_data.keys():
                return -1
            task_id = op_data['task_id']
            if op_type == Global.get_op_cancel():
                dict_op_msg = TaskProcessor.cancel_task(task_id)
            elif op_type == Global.get_op_pause():
                dict_op_msg = TaskProcessor.pause_task(task_id)
            elif op_type == Global.get_op_resume():
                dict_op_msg = TaskProcessor.resume_task(task_id)
            else:
                logging.error('unknown operation: %s\n' % op_type)
                return -1

        if dict_op_msg is not None:
            dict_op_msg['op_type'] = op_type
            s = TCPManager().get_cmd_connect()
            json_op_msg = json.dumps(dict_op_msg)
            s.send(json_op_msg.encode('utf-8'))
            json_ret = s.recv(1024)
            if not json_ret:
                # empty response message
                return -1
            else:
                dict_ret = json.loads(json_ret.decode('utf8'))
                if dict_ret['op_status'] == Global.get_status_completed():
                    op_type = dict_ret['op_type']
                    op_data = dict_ret['op_data']
                    logging.info("executed operation %s to task %s success\n" % (op_type, op_data))
                    return 0
                else:
                    logging.error("executed operation %s to task %s fail\n" % (op_type, op_data))
                    return -1
        else:
            return -1

    @staticmethod
    def submit_task(op_data):
        if 'file_path' not in op_data.keys():
            return None
        file_path = op_data['file_path']
        if not os.path.isfile(file_path):
            return None
        if os.path.getsize(file_path) == 0:
            return None
        dict_op_msg = dict()
        dict_op_data = dict()
        dict_op_data['file_path'] = file_path
        dict_op_msg['op_data'] = dict_op_data
        return dict_op_msg

    @staticmethod
    def cancel_task(task_id):
        dict_op_msg = dict()
        dict_op_data = dict()
        dict_op_data['task_id'] = task_id
        dict_op_msg['op_data'] = dict_op_data
        return dict_op_msg

    @staticmethod
    def pause_task(task_id):
        dict_op_msg = dict()
        dict_op_data = dict()
        dict_op_data['task_id'] = task_id
        dict_op_msg['op_data'] = dict_op_data
        return dict_op_msg

    @staticmethod
    def resume_task(task_id):
        dict_op_msg = dict()
        dict_op_data = dict()
        dict_op_data['task_id'] = task_id
        dict_op_msg['op_data'] = dict_op_data
        return dict_op_msg
