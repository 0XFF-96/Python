import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    @property
    def start_urls(self):

         url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'

         return (url_tmpl.format(i) for i in range(1, 23))

    def parse(self, response):

         for course in response.css('div.course-body'):

                yield{
                         'name': course.css('div.course-name::text').extract_first(),
                                         'description': course.css('div.course-desc::text').extract_first(),
                                                         'type': course.css('div.course-footer span.pull-right::text').extract_first(),
                                                                         'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
                                                      }
