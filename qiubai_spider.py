import requests
from lxml import etree
import json


class QiuBaiSpider:
    def __init__(self):
        self.start_url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.part_url = "http://www.qiushibaike.com"
        self.session = requests.session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

    def get_url_list(self):
        return [self.start_url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        # 通过session请求数据
        # response = self.session.get(url, headers=self.headers)
        return response.content

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        ul_list = html.xpath("//div[@class='recommend-article']/ul/li")
        content_list = []
        for li in ul_list:
            item = {}
            item["title"] = li.xpath(".//div[@class='recmd-right']/a/text()")[0] if len(
                li.xpath(".//div[@class='recmd-right']/a/text()")) > 0 else None
            item["href"] = self.part_url + li.xpath(".//div[@class='recmd-right']/a/@href")[0] if len(
                li.xpath(".//div[@class='recmd-right']/a/@href")) > 0 else None
            item["author"] = li.xpath(".//div[@class='recmd-detail clearfix']/a/span/text()")[0] if len(
                li.xpath(".//div[@class='recmd-detail clearfix']/a/span/text()")) > 0 else None
            item["laugh"] = li.xpath(".//div[@class='recmd-num']/span[1]/text()")[0] if len(
                li.xpath(".//div[@class='recmd-num']/span[1]/text()")) > 0 else None
            item["comment"] = li.xpath(".//div[@class='recmd-num']/span[last()-1]/text()")[0] if len(
                li.xpath(".//div[@class='recmd-num']/span[last()-1]/text()")) > 0 else None
            content_list.append(item)
            if item["title"] == None:
                del item["title"]
                del item["href"]
                del item["author"]
                del item["laugh"]
                del item["comment"]
        return content_list

    def save_content_list(self, content_list):
        with open("糗事百科.txt", "a", encoding="utf-8")as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")

        print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1. start_url_list
        start_url_list = self.get_url_list()
        # 2. 发送请求，获取响应
        for start_url in start_url_list:
            print(start_url)
            html_str = self.parse_url(start_url)
            # 3. 提取数据
            content_list = self.get_content_list(html_str)
            # 4. 保存数据
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiubai_spider = QiuBaiSpider()
    qiubai_spider.run()
