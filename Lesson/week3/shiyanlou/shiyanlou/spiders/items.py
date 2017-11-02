import scrapy

class CourseItem(scrapy.Item):

    """

    """

    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()

