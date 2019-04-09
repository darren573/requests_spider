import json
from parse_url import parse_url

url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=android&for_mobile=1&callback=jsonp1&start=0&count=18&loc_id=108288&_=0"
html_str = parse_url(url)
ret = json.loads(html_str)
print(ret)
print(type(ret))
print(html_str)
