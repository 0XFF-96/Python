# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine


class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        item['students'] = int(item['students'])

#    Course(
#            name = item['name']
#            type = item['type']

        self.session.add(Course(**item))
        return item



    def open_spider(self, spider):
        """
        when open the spider , connect to seesion database

        """

        Session = sessionmaker(bind=engine)

        self.session = Session()


    def close_spider(self, spider):

        """
        when spider close , commit session, 
        """

        self.session.commit()
        self.session.close()


