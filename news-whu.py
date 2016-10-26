#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spider.settings")
import django
django.setup()
from lxml import etree
from ziqiang.models import Newssite
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

url='http://news.whu.edu.cn/'
html_home = requests.get(url).content #获取主页源代码

content_url = re.findall('  <li><a href="(.*?)" target="_blank" title="',html_home,re.S) #获取主页源代码上的标题链接

for each in content_url:
    content_url_final = url + each
    print content_url_final
    # Newssite.objects.get_or_create(url=content_url_final) #将链接写入数据库
    html_part = requests.get(content_url_final).content #获取每个链接的网页源代码

    selector = etree.HTML(html_part)
    title_news = selector.xpath('//*[@id="page_main"]/div[3]/div/div[2]/div[1]/form/div[2]/text()')[0] #获取标题
    content_news = selector.xpath('//*[@id="page_main"]/div[3]/div/div[2]/div[1]/form/div[6]/p/span/text()') #获取内容
    content_news2 = ''.join(content_news) #将多条内容列表转化为字符串
    print title_news
    print content_news2
    Newssite.objects.get_or_create(title=title_news, content=content_news2, url=content_url_final)
