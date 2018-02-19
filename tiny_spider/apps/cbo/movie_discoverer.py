#!/usr/bin/env python
# encoding: utf-8
"""
@author: Jgirl
@contact: 841917374@qq.com
@software: pycharm
@file: movie_discoverer.py
@time: 2018/2/18/018 23:26
@desc:
"""
import json
import configparser
import urllib.request

from tiny_spider.apps.tiny_spider import TinySpider


class MovieDiscoverer(TinySpider):

    def __init__(self):
        super().__init__()
        self.__outfile_path = ''

    def init_sys(self, str_conf_fp):
        conf = configparser.ConfigParser()
        conf.read(str_conf_fp)
        self.__outfile_path = conf.get('cbo_file', 'outfile_path')
        if self.__outfile_path is '':
            return -1
        else:
            return 0

    def load_req(self, dict_req=None):
        list_urls = list()
        if dict_req is not None:
            template_url = dict_req['template_url']
            year_from = dict_req['from_year']
            year_to = dict_req['to_year']
            page_from = dict_req['from_page']
            page_to = dict_req['to_page']

            list_years = range(int(year_from), int(year_to))
            list_pages = range(int(page_from), int(page_to))
            for year in list_years:
                for page in list_pages:
                    url = template_url % (year, page)
                    list_urls.append(url)
        return list_urls

    def init_spider(self, dict_args=None):
        pass

    def exec_spider(self, list_urls, obj=None):
        template_movie_info = 'MovieName: %s\tID: %s\tReleaseYear: %s\tBoxOffice: %s\n'
        list_fail_urls = list()
        for url in list_urls:
            response = urllib.request.urlopen(url)
            json_data = response.read()
            dict_data = json.loads(json_data, encoding='utf-8')
            if 'pData' not in dict_data.keys():
                list_fail_urls.append(url)
                continue
            for i in dict_data['pData']:
                list_movie_info = list()
                if 'MovieName' not in i.keys():
                    continue
                else:
                    list_movie_info.append(i['MovieName'])
                if 'releaseYear' not in i.keys():
                    continue
                else:
                    list_movie_info.append(i['releaseYear'])
                if 'ID' not in i.keys():
                    continue
                else:
                    list_movie_info.append(i['ID'])
                if 'BoxOffice' not in i.keys():
                    continue
                else:
                    list_movie_info.append(i['BoxOffice'])
                tuple_movie_info = tuple(list_movie_info)
                with open(self.__outfile_path, 'a') as f:
                    # 保存到本地路径的"Movies"文件中
                    str_movie_info = (template_movie_info % tuple_movie_info)
                    f.write(str_movie_info)
        return list_fail_urls

    def exit_sys(self):
        pass
