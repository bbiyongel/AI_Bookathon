# -*- coding: utf-8 -*-
# http://sooyoung32.github.io/dev/2016/02/07/scrapy-tutorial.html
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Spider(scrapy.Spider):
  name = "textCrawler"
  start_urls = ['https://teen.munjang.or.kr/archives/category/write/life']
  n = 1

  def parse(self, response):
    n = 1
    url = self.start_urls[0]
    yield scrapy.Request(url, callback=self.parse_page)
    for n in range(2, 310):
      url = self.start_urls[0] + '/page/' +str(n)
      yield scrapy.Request(url, callback=self.parse_page)

  def parse_page(self, response):
    for post in response.css('[class=post_title] a::attr(href)').extract():
      yield scrapy.Request(post, callback=self.parse_text)

  def parse_text(self, post):
    title = post.css('.entry-title::text').extract()
    if ("장원" or "공지") in title[0]:
      return

    item = post.css('[class=entry-content] p').re('(\w+)')
    string = " ".join(item)

    self.n+=1
    dic['title'] = title[0]
    dic['content'] = string

    print(post)
    print(title)
    print(string)

    yield dic
