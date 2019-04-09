import requests

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = {
    "from": "en",
    "to": "zh",
    "query": "hola",
    # "transtype": "realtime",
    # "simple_means_flag": 3,
    # "sign": 372549.85108,
    # "token": "190462db53eb2f8e20020078a101b196"
}
post_url = "https://fanyi.baidu.com/v2transapi"

response = requests.post(post_url, data=data, headers=headers)
print(response.content.decode())
