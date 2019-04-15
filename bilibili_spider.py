import requests
from lxml import etree
import json


class BiliBiliSpider:
    def __init__(self):
        self.start_url_temp = "https://s.search.bilibili.com/cate/search?&search_type=video&view_type=hot_rank&order=dm&copy_right=-1&cate_id=26&page={}&pagesize=20&time_from=20190407&time_to=20190414&_=1555247161888"
        self.headers = {
            "Referer": "https://www.bilibili.com/v/kichiku/mad/?spm_id_from=333.92.b_7375626e6176.3",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def get_url_list(self):
        return [self.start_url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url)
        return response.content.decode()

    def get_content_list(self, html_str):
        data_list = json.loads(html_str)
        title_list = data_list['result']

        content_list = []
        for i in (list(title_list)):
            item = {}
            item["tag"] = i['tag']
            item["title"] = i['title']
            item["pic_href"] = i['pic']
            item["description"] = i['description']
            item["arcurl"] = i['arcurl']
            item["author"] = i['author']
            content_list.append(item)

        return content_list

    def save_content_list(self, content_list):
        with open("B站.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")
            print("保存成功")

    def run(self):  # 实现主要逻辑
        # 1. start_url
        start_url_list = self.get_url_list()
        # 2. 发送请求，获取响应
        for start_url in start_url_list:
            html_str = self.parse_url(start_url)
            # 3. 提取数据
            content_list = self.get_content_list(html_str)
            # 4. 保存数据
            self.save_content_list(content_list)


if __name__ == '__main__':
    bilibili_spider = BiliBiliSpider()
    bilibili_spider.run()
