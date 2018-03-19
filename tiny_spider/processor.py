from celery import Celery
from celery.utils.log import get_task_logger

from tiny_spider.apps.cbo.movie_discoverer import MovieDiscoverer
from tiny_spider.base import constant
from tiny_spider.model.data import Response

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
logger = get_task_logger(__name__)


@app.task(bind=True)
def cbo_download_page(self, obj_req):
    list_urls = list()
    list_fail_urls = list()
    if obj_req.req_type == '0':  # cbo movie discoverer
        cbo_discoverer = MovieDiscoverer()
        res = cbo_discoverer.init_sys("conf/config.ini")
        if res == -1:
            return -1
        list_urls = cbo_discoverer.load_req(obj_req.urls_args)
        list_fail_urls = cbo_discoverer.exec_spider(list_urls)
    pages_count = len(list_urls) - len(list_fail_urls)
    obj_res = Response()
    obj_res.task_id = obj_req.task_id
    obj_res.req_id = obj_req.req_id
    obj_res.req_status = constant.STATUS_COMPLETE_KEY
    obj_res.pages_count = pages_count
    obj_res.pages_args = dict()
    return len(list_fail_urls)
