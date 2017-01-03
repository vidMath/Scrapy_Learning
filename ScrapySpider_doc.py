import scrapy


class QuotesSpider(scrapy.Spider):
    name = "doc_list"
    start_urls = [
        'https://doc.scrapy.org/en/master/',
    ]

    def parse(self, response):
        #Selector(response=response).css('div.wy-menu.wy-menu-vertical')
        for h1,h2 in zip(response.css('p.caption'), response.css('ul')):
            yield {
                'Heading ': h1.css('span.caption-text::text').extract_first(),
				'Subheading ': h2.css(' li.toctree-l1 a.reference.internal::text').extract()
				#'Subheading 1': h1.css('ul li.toctree-l1 a.reference.internal::text').extract(),
			}    		
           