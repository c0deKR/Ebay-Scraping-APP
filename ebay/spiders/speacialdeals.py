import scrapy
from scrapy_splash import SplashRequest

class SpeacialdealsSpider(scrapy.Spider):
    name = "speacialdeals"
    allowed_domains = ["www.ebay.com"]
    script='''
            function main(splash,args)
            
                assert(splash:go(args.url))
                assert(splash:wait(2))
                local all_html_pages = {}
                local previous_html = nil
                
                while true do
                    -- Get the current HTML content of the page
                    local current_html = splash:html()
                    
                    -- Check if the HTML content has changed
                    if current_html ~= previous_html then
                        table.insert(all_html_pages, current_html)
                        previous_html = current_html
                    end
                    
                    -- Scroll down the page
                    splash:runjs("window.scrollBy(0,1500);")
                    assert(splash:wait(2)) -- Adjust the wait time as needed
                    
                    -- Check if you've reached the bottom of the page
                    local is_end_of_page = splash:evaljs("window.innerHeight + window.scrollY >= document.body.scrollHeight")
                    
                    if is_end_of_page then
                            button  = splash:select('button[class*="load-more-btn btn btn--secondary"]')
                            if button == nil then
                            break
                            else
                            button:mouse_click()
                            assert(splash:wait(1))
                            end
                    end
                end
                local num_pages = #all_html_pages
                
                return {
                    all_html_pages = all_html_pages,
                        num_pages = num_pages,
                        png = splash:png()
                }
            end
            '''

    def start_requests(self):
        yield scrapy.Request(url='https://www.ebay.com/globaldeals',callback=self.crawl,headers=
                             {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
                                 
                             })
    def crawl(self,response):
        for i in range(4,19):
            category = response.xpath(f"(//h2)[{i}]/@id").get()
            print(category)
            category_url = response.xpath(f"(//h2)[{i}]/following::div[1]/div[3]/div[2]/div/div/a/@href").get()
            yield scrapy.Request(url=category_url,callback=self.splashRequest,headers=
                             {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
                                 
                             },meta={'category':category})
    def splashRequest(self,response):
        print(f' here is the link from here {response.url}')
        yield SplashRequest (url=response.url,
                            callback=self.parse,
                            endpoint='execute',
                            meta={'category':response.meta.get('category')},
                            args={'lua_source':self.script,'timeout':3600},
                            splash_headers={
                                'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
                            })
    def parse(self, response):

        # Many html pages will be returned here

        all_html_pages = response.data['all_html_pages']
        for html_page in all_html_pages:
            print(html_page.body)

        """products = response.xpath("//div[@id='spokeResultSet']/div/div/div/div")

        for product in products:

            yield {
                'Category': response.meta.get('category'),
                'Title': product.xpath(".//div/a/h3/@title").get(),
                'Image': product.xpath(".//a/div/div/img/@src").get(),
                'Price': product.xpath(".//div/div[@itemscope='itemscope']/span[@itemprop='price']/text()").get(),
                'Original Price': product.xpath(".//div/div[@class='dne-itemtile-original-price']/span[1]/span[1]/text()").get(),
                'Discount': product.xpath(".//div/div[@class='dne-itemtile-original-price']/span[1]/span[3]/text()").get(),
                'Link' : product.xpath(".//div/a/@href").get(),
            }
"""