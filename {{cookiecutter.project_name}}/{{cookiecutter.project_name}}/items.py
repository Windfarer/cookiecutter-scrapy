# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader import ItemLoader
from datetime import datetime
from scrapy.loader.processors import TakeFirst, Identity, MapCompose


def parse_date(data):
    try:
        rv = datetime(*[int(i) for i in re.findall('\d+', data)])
    except Exception:
        rv = None
    return rv

def parse_int(data):
    try:
        rv = int(re.search('\d+', data).group(0))
    except Exception:
        rv = None
    return rv


class PageItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    release_date = scrapy.Field(input_processor=MapCompose(parse_date))
