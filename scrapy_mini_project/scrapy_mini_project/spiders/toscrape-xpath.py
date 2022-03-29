import scrapy


class QuotesSpideriXPath(scrapy.Spider):
    name = "toscrape-xpath"

    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for index, quote in enumerate(response.xpath('//div[contains(@class, "quote")]')):
            yield {
                'tags'   : quote.xpath('div[contains(@class, "tags")]//a/text()').extract(),
                'text'   : quote.xpath('span/text()').extract_first(),
                'author' : quote.xpath('span//small/text()').extract_first()
            }


        resp = response.xpath('//li[contains(@class, "next")]//a/@href').extract_first()

        if resp is not None :
            resp = response.urljoin(resp)
            yield scrapy.Request(resp, callback=self.parse)
