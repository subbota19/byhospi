import scrapy


class ScrapyByhospiItem(scrapy.Item):
    full_address = scrapy.Field()
    location = scrapy.Field()
    name = scrapy.Field()
    number_phone = scrapy.Field()
