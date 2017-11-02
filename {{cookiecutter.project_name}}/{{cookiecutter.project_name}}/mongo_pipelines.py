# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from mongoengine.errors import NotUniqueError
from mongoengine import Document, StringField, DateTimeField, IntField, ListField
from mongoengine import connect
import os

DB_URI = os.getenv("DB_URI")
connect(host=DB_URI)


class Page(Document):
    title = StringField()
    url = StringField()
    release_date = DateTimeField()
    content = StringField()

    meta = {
        'collection': 'pages',
    }


class PagePipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        try:
            Page(**item).save()
        except NotUniqueError:
            pass
        return item
