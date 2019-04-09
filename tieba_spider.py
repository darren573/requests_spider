import requests


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url = "https://tieba.baidu.com/f?kw=" + tieba_name + "&pn={}"
        self.headers = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

    def get_url_list(self):
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url.format(i * 50))
        # return url_list
        return [self.url.format(i * 50) for i in range(1000)]

    def parse_url(self, url):
        response = requests.get(url, self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        # 构造网址
        url_list = self.get_url_list()
        # 遍历发送请求、获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存
            page_num = url_list.index(url) + 1
            self.save_html(html_str, page_num=page_num)


if __name__ == "__main__":
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()
