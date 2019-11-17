# -*- coding: utf-8 -*-
# http://sooyoung32.github.io/dev/2016/02/07/scrapy-tutorial.html
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Spider(scrapy.Spider):
  name = "textCrawler"
  start_urls = ['https://teen.munjang.or.kr/archives/category/write/life']
  # result = {}
  n = 1
  #//*[@id="main"]/div[1]/ul/li[6]/a
  # //*[@id="main"]/div[1]/ul/li[8]/a
  # rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="main"]/div[1]/ul/li/a',)), callback="parse", follow= True),)

  def parse(self, response):
    n = 1
    url = self.start_urls[0]
    yield scrapy.Request(url, callback=self.parse_page)
    for n in range(2, 310):
      url = self.start_urls[0] + '/page/' +str(n)
      yield scrapy.Request(url, callback=self.parse_page)

  def parse_page(self, response):
    # for post in response.xpath('//a'):
    # for post in response.xpath('//div/div[2]/div[1]/a'):
    for post in response.css('[class=post_title] a::attr(href)').extract():
      # print('post: ',post)
    # for post in response.css('.post_title').xpath('//@href'):
    # for post in response.css('.post_title').xpath('//a').get():
      # url = response.urljoin(post)
      # print('url: ', url)
      # yield scrapy.Request(url, callback=self.parse_text)
      # print('post:',post)
    # url = response.urljoin(post.extract())
      yield scrapy.Request(post, callback=self.parse_text)
      
  def parse_text(self, post):
    dic = {}  
    # for post in response:
      # item = post.xpath('//p/text()').extract()//*[@id="uniform-breadcrumb"]/div/span
      # title = post.xpath('//header/h1/text()').extract()
    print(post)
    title = post.css('.entry-title::text').extract()
    if "장원" or "공지" in title[0]:
      return
    # item = post.xpath('//p/text()').extract()
    item = post.xpath('//p/text()').re('(\w+)')
    print(title)
    string = " ".join(item)
    print(string)
    # print(type(title))
    # print(type(string))
    # self.result[post] = item
    # yield dic
    self.n+=1
    # if self.n== 3 :
      # break
    dic['title'] = title[0]
    dic['content'] = string

    yield dic
# //*[@id="post-111089"]/div[1]/div/p[3]
# //*[@id="post-111089"]/div[1]/div/p[1]
#       if next_post is not None :
#         next_post = response.urljoin(next_post)
#         yield scrapy.Request(next_post, callback=self.parse_txt)

#     next_page = response.css().extract_first()

#     if next_page is not None:
#       next_page = response.urljoin(next_page)
#       yield scrapy.Request(next_page, callback=self.parse)

#   def parse_text(self, response):
#     for link in response.css('div.s_write'):
#       post_link = response.url


# //*[@id="post-111089"]/div/div[2]/div[1]/a
# //*[@id="post-106393"]/div/div[2]/div[1]/a
# /html/body/div[1]/div[3]/div[2]/div/main/article[1]/div/div[2]/div[1]/a
# //*[@id="post-111089"]/div/div[2]/div[1]/a