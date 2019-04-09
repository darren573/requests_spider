import requests

#  保存图片
response = requests.get("https://www.baidu.com/img/bd_logo1.png")

with open("a.png", "wb") as f:
    f.write(response.content)
