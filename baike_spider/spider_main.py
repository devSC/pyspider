#coding:utf8

from baike_spider import url_manager, html_downloader, html_outputer, html_parser

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):

        count = 1

        # 添加 root_url
        self.urls.add_new_url(root_url)
        #1. 是否有待爬url
        while self.urls.has_new_url():
           try:
               # 2. 拿到url
               new_url = self.urls.get_new_url()
               print('craw %d : %s' % (count, new_url))
               # 3. 下载内容
               html_cout = self.downloader.download(new_url)
               # 4. 解析内容
               new_urls, new_data = self.parser.parse(new_url, html_cout)
               # 4.1 是否有新的URL
               self.urls.add_new_urls(new_urls)
               # 5. 将解析的内容添加进Outputer
               self.outputer.collect_data(new_data)

               if count == 1000:
                   break

               count = count + 1
           except ValueError as e:
               print('craw failed:', e)

        #end: 输出所有内容
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
