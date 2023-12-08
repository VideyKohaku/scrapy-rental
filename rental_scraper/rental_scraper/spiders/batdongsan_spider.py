import scrapy


class BatdongsanSpiderSpider(scrapy.Spider):
    name = "batdongsan_spider"
    allowed_domains = ["batdongsan.com.vn"]
    start_urls = ["https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro?cIds=51,326"]

    def parse(self, response):
        pass
