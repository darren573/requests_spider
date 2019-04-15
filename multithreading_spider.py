from queue import Queue
import threading
import requests
from lxml import etree
import json


class QiuBaiSpider:
    def __init__(self):
        self.start_url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.part_url = "http://www.qiushibaike.com"
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

    def get_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.start_url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_queue.get()
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
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            with open("糗事百科.txt", "a", encoding="utf-8") as f:
                for i in content_list:
                    f.write(json.dumps(i, ensure_ascii=False, indent=2))
                    f.write("\n")
                self.content_queue.task_done()

    def run(self):  # 实现主要逻辑
        thread_list = []
        # 1. start_url_list
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2. 发送请求，获取响应
        for i in range(2):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # 3. 提取数据
        for i in range(2):
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        # 4. 保存数据
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for thread in thread_list:
            thread.setDaemon(True)  # 把子线程设置为守护线程，(即该线程不重要) 主线程结束，子线程结束
            thread.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()  # 让主线程等待阻塞，等待队列的任务完成之后再完成

        print("主线程执行结束")


if __name__ == '__main__':
    qiubai_spider = QiuBaiSpider()
    qiubai_spider.run()
