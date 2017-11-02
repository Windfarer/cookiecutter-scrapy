# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import Integer, DateTime, Date, String, Text, Float
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import JSON

DB_URI = os.getenv("DB_URI")

BaseModel = declarative_base()


class Page(BaseModel):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    url = Column(String(1024), index=True)
    content = Column(MEDIUMTEXT)


class PagePipeline(object):
    def __init__(self):
        engine = create_engine(DB_URI, echo=False, pool_size=100, pool_recycle=3600)
        self.DBSession = sessionmaker(bind=engine)
        BaseModel.metadata.create_all(engine)
    def process_item(self, item, spider):
        session = self.DBSession()
        try:
            p = Page(**item)
            session.add(p)
            session.commit()
        except Exception as e:
            session.rollback()
        session.close()
        return item
