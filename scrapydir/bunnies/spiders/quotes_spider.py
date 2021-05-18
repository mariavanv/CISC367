import scrapy


class BunniesSpider(scrapy.Spider):
    name = "bunnies"

    def start_requests(self):
        urls = [
            'import scrapy'


class BunniesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://www.raising-rabbits.com/all-rabbit-breeds.html",
        
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'bunnies-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
