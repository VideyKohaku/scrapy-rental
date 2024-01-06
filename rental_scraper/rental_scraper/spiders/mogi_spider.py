import scrapy
import re
from rental_scraper.items import Rental_Item


class MogiSpiderSpider(scrapy.Spider):
    name = "mogi_spider"
    allowed_domains = ["mogi.vn"]
    start_urls = [
        "https://mogi.vn/ho-chi-minh/thue-phong-tro-nha-tro",
        "https://mogi.vn/ho-chi-minh/thue-can-ho-chung-cu",
        "https://mogi.vn/ho-chi-minh/thue-nha-rieng",
        "https://mogi.vn/ho-chi-minh/thue-nha-mat-pho",
    ]
    page_number = 1


    def start_requests(self):
        # print('self:', self.crawling_page)
        for url in self.start_urls:
            yield scrapy.Request(url)

    # parse list of rentals in a certain NUMBER of page
    def parse(self, response):
        rental_props = response.css("ul.props > *")

        for prop in rental_props:
            prop_info_url = prop.css("li div.prop-info a.link-overlay::attr(href)").get()
            # print(prop_info_url)
            yield scrapy.Request(prop_info_url, callback=self.parse_detail_info, meta={ 'prop_info_url': prop_info_url})

        next_btn = response.css('div.paging ul.pagination li:last-child a[gtm-act="next"]')

        # if next_btn is not None and self.page_number < response.meta.get('crawling_page'):
        if next_btn is not None and self.page_number < int(self.crawling_page):
            next_url = next_btn.css('::attr(href)').get()
            self.page_number += 1
            yield response.follow(next_url, callback = self.parse)



    # get detail info of rental properties
    def parse_detail_info(self, response):
        rental_item = Rental_Item()
        # def extract_number(phone_str):
        #     pattern = r'\b\d*\b'
        #     return re.findall(pattern, phone_str)[2]
        
        general_info = response.css('div.main-info')
        main_info = response.css('div.info-attrs.clearfix > *')

        agent_name_no_link = response.css('div.agent-name::text').get()
        agent_name_link = response.css('div.agent-name a::text').get()
        agent_name = agent_name_link if agent_name_link else agent_name_no_link


        # add to rental_item
        rental_item['title'] = general_info.css('div.title h1::text').get()
        rental_item['address'] = general_info.css('div.address::text').get()
        rental_item['price'] = general_info.css('div.price::text').get()
        rental_item['description'] = response.css('div.info-content-body').xpath('string()').get()
        rental_item['owner_name'] = agent_name
        rental_item['owner_contact'] = response.css('div.agent-contact a::attr(ng-bind)').get()
        rental_item['prop_info_url'] = response.meta.get('prop_info_url')
         
        for info in main_info:
            info_name = info.css('span:nth-of-type(1)::text').get()
            info_value = info.css('span:nth-of-type(2)::text').get()
            if info_name == 'Diện tích sử dụng':
                rental_item['area'] = info_value
            elif info_name == 'Ngày đăng':
                rental_item['post_date'] = info_value
            elif info_name == 'Mã BĐS':
                rental_item['real_estate_code'] = info_value

        yield rental_item