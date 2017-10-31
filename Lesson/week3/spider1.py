import scrapy

class shiyanlouCoursesSpider(scrapy.Spider):

    @property
    def start_requests(self):

        url_tmp =' https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
    
        urls = (url_tmp.format(i) for i in range(1,23))

        for url in urls:
            yield crapy.Request(url=url, callback=self.parse)


        
    def parse(self, response):

        # div.course-body

        for course in response.css('div.course-body'):

            # user css  extract course from date
            yield{

                # course name 
                'name':course.css('div.course-name::text').extract_first(),
                #describe the course

                'description':course.css('div.course-desc::text').extract_first(),

                'type':course.css('div.course-footer span.pull-right::text').extract_first(default='')

              #  'students':course.xpath('.//span[contains(@class, "pull-left")]/te
              }

