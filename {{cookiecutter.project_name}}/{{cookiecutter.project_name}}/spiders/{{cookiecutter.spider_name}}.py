# -*- coding: utf-8 -*-
import scrapy
from ..items import PageItem
import re


class PageSpider(scrapy.Spider):
    name = '{{cookiecutter.spider_name}}'
    allowed_domains = ['www.example.com']
    start_urls = ['http://www.example.com/{}.html'.format(i) for i in reversed(range(12345))]

    def parse(self, response):
        print(response)
