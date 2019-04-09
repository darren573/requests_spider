import requests

proxies = {
    "http": "http://172.20.80.74:80"
}

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
url = "http://www.baidu.com"
r = requests.get(url, proxies=proxies, headers=headers)
print(r)
