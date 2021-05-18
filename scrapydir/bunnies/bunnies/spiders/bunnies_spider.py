import scrapy
from scrapy.item import Field, Item

class Bunny(Item):
    name = Field()
    snrWeight = Field()
    bunType = Field()
    color = Field()
    dist = Field()


class BunniesSpider(scrapy.Spider):
    name = "bunnies"

    def start_requests(self):
        urls = [
            'https://www.raising-rabbits.com/all-rabbit-breeds.html',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        #item = Bunny()
        #item["name"] = hxs.select
        page = response.url.split("/")[-2]
        filename = f'bunnies-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
