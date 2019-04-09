import re
import requests
import json
from parse_url import parse_url

url = "https://36kr.com/"
html_str = parse_url(url)
for html in html_str:
    html = str(html)
    ret = re.findall("<script>window.initialState=(.*?)</script>", html)
# ret = json.loads(ret)
print(ret)
