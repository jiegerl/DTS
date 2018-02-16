import getopt
import sys

from tiny_spider.core.opt_processor.task_processor import TaskProcessor
from tiny_spider.core.scheduler import Scheduler
from tiny_spider.core.webspider import WebSpider


class CmdProcessor:
    def __init__(self, argv):
        self.__argv = argv

    def process_cmd(self):
        try:
            opts, args = getopt.getopt(self.__argv, "hs:c:p:r:n:")

        except getopt.GetoptError:
            print('unknown args!')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print("Usage:")
                print("opt_processor.py -s <taskfile>")
                print("opt_processor.py -c <taskid>")
                print("opt_processor.py -p <taskid>")
                print("opt_processor.py -r <taskid>")
                sys.exit(0)
            elif opt == "-s":  # submit
                task_file_path = arg
                TaskProcessor.submit_task(task_file_path)
            elif opt == '-p':  # pause
                task_id = arg
                TaskProcessor.pause_task(task_id)
            elif opt == '-c':  # cancle
                task_id = arg
                TaskProcessor.cancel_task(task_id)
            elif opt == '-r':  # resume
                task_id = arg
                TaskProcessor.resume_task(task_id)
            elif opt == '-n':
                node_type = arg
                if node_type == 's':
                    t = Scheduler()
                    t.start()
                elif node_type == 'c':
                    w = WebSpider()
                    w.start()
                else:
                    print('unknown args!')
            else:
                print('unknown args!')
