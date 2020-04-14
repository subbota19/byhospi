from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_byhospi.items import ScrapyByhospiItem
import re, numpy, pandas as pd

pd_obj = pd.DataFrame()

dict_for_relationship = {'1': 'Брестская область', '2': 'Гомельская область', '3': 'Гродненская область',
                         '4': 'Витебская область', '5': 'Минская область', '6': 'Могилевкая область'}
list_with_regular_expression = [r'Брест+', r'Гомель+', r'Гродн+', r'Витебск+', r'Минск+', r'Могил+']


def create_fk(obj):
    values = obj['location'].unique()
    values = pd.Series(numpy.arange(1, len(values) + 1), values)
    obj['region'] = obj['location'].apply(values.get)


class HospitalSpider(CrawlSpider):
    name = 'hospi'
    allowed_domain = ['med-tutorial.ru']
    start_urls = ['https://med-tutorial.ru/clinics/country-cat/47/248/']
    rules = [Rule(
        LinkExtractor(allow=r'^({}[\d]+/)$'.format(start_urls[0])),
        callback='parse_items', follow=True)]

    def parse_items(self, response):
        global pd_obj
        for res in response.selector.xpath('//td[@valign="top"]/table[@border="0"]/tr'):
            if res.xpath('td/a/h4/text()').get() is None:
                continue
            add_param = res.xpath('td/div/i/text()')
            list_with_data = []
            for index, regular_ex in enumerate(list_with_regular_expression,1):
                if re.findall(regular_ex, add_param.get()):
                    list_with_data += [add_param.get()[3:], int(index)]
                    break
            else:
                continue
            list_with_data.append(res.xpath('td/a/h4/text()').get())
            for i in res.xpath('td[@class="ser"][./b/text()="Телефон:"]'):
                for j in i.xpath('a[@class="context_search"]/text()'):
                    list_with_data.append(j.get())
                    break
            pd_obj = pd_obj.append(dict(zip(ScrapyByhospiItem.fields, list_with_data)), ignore_index=True)
        pd_obj.to_csv('hospital.csv')
