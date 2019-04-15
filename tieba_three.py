import requests
import json
from lxml import etree
import re


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/f?&kw=" + tieba_name + "&pn=0"
        self.part_url = "http://tieba.baidu.com"
        self.headers = {
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//code[@id='pagelet_html_frs-list/pagelet/thread_list']")[0]
        s = etree.tostring(div_list).decode()
        a = re.findall('<!--([\s\S]*)-->', s)[0]
        a = a.replace('\n', '')
        a = a.replace('\r', '')
        e = etree.HTML(a)
        title = e.xpath("//a[@class='j_th_tit ']/@title")
        href = e.xpath("//a[@class='j_th_tit ']/@href")

        content = []
        for i in range(0, len(title)):
            item = {}
            item["title"] = title[i]
            item["href"] = self.part_url + href[i]
            content.append(item)
        print(content)

        content_list = []
        for i in content:
            item["img_list"] = self.get_img_list(i["href"], [])
            content_list.append(item)
        print(content_list)

        # 提取下一页url
        next_url = self.part_url + html.xpath("//a[text()='下一页']/@href")[0] if len(
            html.xpath("//a[text()='下一页']/@href")) > 0 else None

        return content_list, next_url

    def get_img_list(self, detail_url, total_img_list):
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        if img_list:
            total_img_list.extend(img_list)
            detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
            if len(detail_next_url) > 0:
                detail_next_url = self.part_url + detail_next_url[0]
                return self.get_img_list(detail_next_url, total_img_list)

        return total_img_list

    def save_content_list(self, content_list):
        file_path = self.tieba_name + ".txt"
        with open(file_path, "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要逻辑
        next_url = self.start_url
        while next_url is not None:
            # 1. start_url
            # 2. 发送请求，获取响应
            html_str = self.parse_url(self.start_url)
            # 3.提取数据，提取下一页url地址
            content_list, next_url = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)
            # 5.请求下一页url地址，进入循环2-5


if __name__ == '__main__':
    tieba_spider = TiebaSpider("校花")
    tieba_spider.run()
