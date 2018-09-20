# *_*coding:utf-8 *_*
import re
import urllib

from lxml import etree
class Parser(object):
    def parse(self,content,page_url):
        if content is None:
            return

        new_urls = self.get_new_url(content,page_url)
        new_data = self.get_new_data(content,page_url)
        return new_urls,new_data

    def get_new_url(self, content,page_url):
        tree = etree.HTML(content)
        new_urls = set()
        new_links = tree.xpath("//a/@href")
        if len(new_links) < 0:
            return None
        for new_url in new_links:
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            #print(new_full_url)
            new_urls.add(new_full_url)
        print("获取到"+ str(len(new_urls))+"个新的url:")
        return new_urls

    def get_new_data(self, content,page_url):
        tree = etree.HTML(content)
        title = tree.xpath("//div[@class='picmainer']/h1/text()")
        title = ",".join(title)

        url = tree.xpath("//div[@class='picsbox picsboxcenter']/p/a/img/@src")
        url = ','.join(url)
        print(url)
        data  = {'title':title,'url':url}
        print(data)
        return data