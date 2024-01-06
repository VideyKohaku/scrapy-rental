# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



# this is where we can do the cleaning, formatting, validating, store data to database, etc.
class RentalScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()

        # format phone number
        phone_value = adapter.get('owner_contact')
        print('phone_value:', phone_value)

        return item


