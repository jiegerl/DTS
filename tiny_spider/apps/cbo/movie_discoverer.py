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
import urllib.request


class MovieDiscoverer:

    def __init__(self, list_years, list_pages):
        self.__list_urls = list()
        template_url = "http://www.cbooo.cn/Mdata/getMdata_movie?area=50&year=%s&initial=\%E5\%85\%A8\%E9\%83\%A8&pIndex=%s"
        for year in list_years:
            for page in list_pages:
                url = template_url % (year, page)
                print(url)
                self.__list_urls.append(url)

    def execute_discover(self):
        # 从urlList里面取出url并获取信息
        for url in self.__list_urls:
            response = urllib.request.urlopen(url)
            json_data = response.read()
            for i in json.loads(json_data, encoding='utf-8')['pData']:
                print(i['MovieName'], i['releaseYear'], i['ID'], i['BoxOffice'])
                with open("Movies", 'a') as f:
                    # 保存到本地路径的"Movies"文件中
                    writeString = 'MovieName: %s\tID: %s\tReleaseYear: %s\tBoxOffice: %s\n' % (
                        i['MovieName'], i['ID'], i['releaseYear'], i['BoxOffice'])
                    f.write(writeString.encode('utf-8'))