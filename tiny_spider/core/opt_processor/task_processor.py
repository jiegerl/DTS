import os
import struct

from tiny_spider.net.tcp_manager import TCPManager


class TaskProcessor:

    @staticmethod
    def submit_task(task_path=None):
        tm = TCPManager()
        s = tm.get_cmd_submitter_connect()
        struct.calcsize('128sl')
        file_head = struct.pack('128sl', os.path.basename(task_path).encode('utf8'), os.stat(task_path).st_size)
        s.send(file_head)

        fo = open(task_path, 'rb')
        while True:
            file_data = fo.read(1024)
            if not file_data:
                break
            s.send(file_data)
        fo.close()
        s.close()

    @staticmethod
    def cancel_task(task_id):
        pass

    @staticmethod
    def pause_task(task_id):
        pass

    @staticmethod
    def resume_task(task_id):
        pass
