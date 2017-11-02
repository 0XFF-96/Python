# -*- coding: utf-8 -*-
import scrapy
from  shiyanlou2.items import CourseItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'
#     allowed_domains = ['shiyanlou.com']
# start_urls = ['http://shiyanlou.com/']

    def start_urls(self):

        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1,23))


    def parse(self, response):
    
        for course in response.css('div.course-body'):

            item = CourseItem({

                'name':course.css('div.course-name::text').extract_first(),
           
                'description':course.css('div.course-desc::text').extract_first(),

                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
                })
            yield item 

