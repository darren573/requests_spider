import requests
import json
import re


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/f?kw=" + tieba_name + "&pn=0"
        self.part_url = "http://tieba.baidu.com"
        self.headers = {
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
        }

    def save_content_list(self, content_list):
        file_path = self.tieba_name + ".txt"
        with open(file_path, "a", encoding="utf-8") as f:
            # 遍历列表 分别写入
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")

    def parse_url(self, url):
        print(url)
        toggle = False
        curr_pagen = int(re.findall(r'&pn=(\d+)', url)[0])
        # 构造下一页url
        next_pagen = re.sub(r'&pn=(\d+)', r'&pn={}'.format(curr_pagen + 50), url)
        # 发送请求，获取响应
        response = requests.get(url, headers=self.headers, timeout=20)
        html_str = response.content.decode()
        # 使用正则提取全部img_url
        img_url_list = re.findall('bpic *= *"([^"]+)', html_str)
        # 提取"/p/6086393083" title="感觉自己萌萌哒" target="_blank" class="j_th_tit ">感觉自己萌萌哒
        title_list = re.findall('<a rel=\"noreferrer\" href=(.*?)</a>', html_str)
        content_list = []
        for title in title_list:
            toggle = True
            item = {}
            # 提取title内容
            title_temp = re.search(">(.*?)<", title + "<")
            item["title"] = list(title_temp.groups())[0]
            # 提取href内容
            href_temp = re.search("\"(.*?)\"", title)
            item["href"] = self.part_url + list(href_temp.groups())[0]  # 我们得到的img_url是这样的/p/6052917512,所以此处要拼接
            print(item["href"])
            # 提取img_url内容
            item["img_list"] = [img_url for img_url in img_url_list][0]
            # 把得到的数据添加到一个列表里面
            content_list.append(item)

        self.save_content_list(content_list)
        return toggle, next_pagen

    def run(self):
        toggle, next_url = self.parse_url(self.start_url)
        while toggle:
            toggle, next_url = self.parse_url(next_url)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("校花")
    tieba_spider.run()
