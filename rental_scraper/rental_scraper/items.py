# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re

class RentalScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def extract_number(phone_str):
    pattern = r'\b\d*\b'
    return re.findall(pattern, phone_str)[2]

def trim_string(text):
    return text.strip()

class Rental_Item(scrapy.Item):
    name = scrapy.Field
    address = scrapy.Field
    price = scrapy.Field
    area = scrapy.Field
    description = scrapy.Field
    owner_name = scrapy.Field
    owner_contact = scrapy.Field
    post_date = scrapy.Field
    prop_info_url = scrapy.Field