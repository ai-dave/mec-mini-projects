import scrapy  


class QuotesSpiderCss(scrapy.Spider):
    name = "toscrape-css"

    start_urls = ['http://quotes.toscrape.com/page/1/']  

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'tags'   : quote.css('div.tags a.tag::text').getall(),
                'text'   : quote.css('span.text::text').get(),
                'author' : quote.css('small.author::text').get()
            }

        resp = response.css('li.next a::attr(href)').get()

        if resp is not None:
            resp = response.urljoin(resp)
            yield scrapy.Request(resp, callback=self.parse)
