import scrapy


class ItemscraperSpider(scrapy.Spider):
    name = "ItemScraper"
    allowed_domains = ["www.ebay.com"]
    URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=logitech+g502&_sacat=0"
    
    def start_requests(self):
        yield scrapy.Request(url=self.URL,callback=self.parse,headers=
                             {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"})
    
    
    def parse(self, response):

        products = response.xpath("(//div[@class='s-item__wrapper clearfix'])[position() > 1]")

        for product in products:
            product_url = product.xpath(".//div[1]/div/a/@href").get()
            product_image_url = product.xpath(".//div[1]/div/a/div/img/@src").get()
            title = product.xpath(".//div[2]/a/div/span/text()").get()
            status = product.xpath(".//div[2]/div[1]/span/text()").get()
            price = product.xpath(".//div[2]/div[@class='s-item__details clearfix']/div[1]/span[@class='s-item__price']/text()").get()
            shipping = product.xpath(".//div[2]/div[@class='s-item__details clearfix']/div/span[@class='s-item__shipping s-item__logisticsCost']/text()").get()
            location = product.xpath(".//div[2]/div[@class='s-item__details clearfix']/div/span[@class='s-item__location s-item__itemLocation']/text()").get()
            location = location.split(" ")[1:]
            location = " ".join(location)
            rating = product.xpath(".//div[2]/div[@class='s-item__reviews']/a/div/span/text()").get()

            yield {
                'Product Title': title,
                'Product Status': status,
                'Product Price': price,
                'Shippping fees': shipping,
                'Product Location': location,
                'Product Rating': rating,
                'Product URL': product_url,
                'Product Image URL': product_image_url
            }
        next_page = response.xpath("//a[@class='pagination__next icon-link']/@href").get()
        page = 1
        if next_page:
            print(next_page)
            
            
            yield scrapy.Request(url=next_page, callback=self.parse,  headers={   

                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/88.0.4324.96 Chrome/88.0.4324.96 Safari/537.36"
            })
        """def start_requests(self):
        # Open and read the locally downloaded HTML page
        with open(self.file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Yield a Scrapy Request with the HTML content
        yield scrapy.Request(url='file://localhost/' + self.file_path, body=html_content, callback=self.parse)"""