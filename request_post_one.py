import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",

}

post_data = {
    "kw": "早上好",
    # "from": "zh",
    # "to": "en",
}

post_url = "https://fanyi.baidu.com/sug"

response = requests.post(post_url, data=post_data)
print(response.content.decode())
