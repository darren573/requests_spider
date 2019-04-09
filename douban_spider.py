import requests
import json


class DoubanSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
            "Referer": "https: // m.douban.com / tv / american"
        }
        self.start_temp_list = [  # 使用字典对保存的信息进行国家类别分类保存
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?start={}&count=18&loc_id=108288",
                "country": "US"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_korean/items?start={}&count=18&loc_id=108288",
                "country": "Korean"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?start={}&count=18&loc_id=108288",
                "country": "CN"
            }
        ]

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        print(json_str)
        dict_ret = json.loads(json_str)
        # print(dict_ret)
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"]
        return content_list, total

    def save_content_list(self, content_list, country):
        with open("douban.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                content["country"] = country
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
            print("保存成功")

    def run(self):  # 实现主要逻辑
        for temp_url in self.start_temp_list:
            num = 0
            # 假设有第一页
            total = 100
            while num < total + 18:
                # 1.准备一个起始url
                url = temp_url["url_temp"].format(num)
                # 2. 发送请求，获取响应
                json_str = self.parse_url(url)
                # 3. 提取数据
                content_list, total = self.get_content_list(json_str)
                # 4. 保存
                self.save_content_list(content_list, temp_url["country"])
                # if len(content_list) < 18:
                #     break
                # 5.构造下一页的url地址，进入循环
                num += 18


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
