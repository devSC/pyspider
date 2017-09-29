#coding:utf8
import re

from bs4 import BeautifulSoup

from urllib import parse


class HtmlParser(object):
    def parse(self, page_url, html_coutent):
        if page_url is None or html_coutent is None:
            return
        soup = BeautifulSoup(html_coutent, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/[\w\d]+'))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _set_node_title(self, node, data):
        title = node.get_text()
        if title is not None:
            data['title'] = title

    def _set_node_summary(self, node, data):
        summary = node.get_text()
        if summary is not None:
            data['summary'] = summary

    def _get_new_data(self, page_url, soup):
        res_data = {}
        #url
        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_= 'lemmaWgt-lemmaTitle-title')
        if title_node is not None:
            title_h1_node = title_node.find('h1')
            if title_h1_node is not None:
                self._set_node_title(title_h1_node, res_data)

            else:
                self._set_node_title(title_node, res_data)

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = 'lemma-summary')
        if summary_node is not None:
            summary_div = summary_node.find('div', class_ = 'para')
            if summary_div is not None:
                self._set_node_summary(summary_div, res_data)

            else:
                self._set_node_summary(summary_node, res_data)


        return res_data
