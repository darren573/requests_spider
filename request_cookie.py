import requests

session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Cookie": "anonymid=ju2av7yn-tj0r69; depovince=HEN; _r01_=1; JSESSIONID=abc9RRe7SPemr5NWMlNNw; ick_login=88d0d7f4-5931-4d4d-9016-d5e0d6832b43; ick=7d1717f9-3582-4e70-8bed-fb08d2324226; wp=1; __utma=151146938.1507190917.1554362728.1554362728.1554362728.1; __utmc=151146938; __utmz=151146938.1554362728.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/SysHome.do; __utmt=1; __utmb=151146938.4.10.1554362728; jebecookies=dc0dddf5-3283-40d2-b664-ec9c3793cbca|||||; _de=B11F3A2DE590F822085556B50229AEB1; p=7e517bf054769ca03115dcd7ccdfa41a8; first_login_flag=1; ln_uact=13938386255; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=16ff33a1a5a7c1bac2f4c6754fb67ad38; societyguester=16ff33a1a5a7c1bac2f4c6754fb67ad38; id=473434718; xnsid=18c19be0; ver=7.0; loginfrom=null; jebe_key=6398ad07-4403-4ad1-a07c-691b0c18802f%7C9346b2c79ab2747ee8946889d9693ed5%7C1554362820548%7C1%7C1554362823025; wp_fold=0"

}

post_data = {"email": "13938386255", "password": "darren573"}
# 使用session发送post请求，cookie保存在session中
session.post(post_url, data=post_data, headers=headers)
# 再使用session请求登陆之后才能访问的网站
r = session.get("http://www.renren.com/970301096/profile", headers=headers)
# 保存界面
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())

# 不使用post请求
r = requests.get("http://www.renren.com/970301096/profile", headers=headers)
# 保存界面
with open("renren2.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}
cookies = "anonymid=ju2av7yn-tj0r69; depovince=HEN; _r01_=1; JSESSIONID=abc9RRe7SPemr5NWMlNNw; ick_login=88d0d7f4-5931-4d4d-9016-d5e0d6832b43; ick=7d1717f9-3582-4e70-8bed-fb08d2324226; wp=1; __utma=151146938.1507190917.1554362728.1554362728.1554362728.1; __utmc=151146938; __utmz=151146938.1554362728.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/SysHome.do; __utmt=1; __utmb=151146938.4.10.1554362728; jebecookies=dc0dddf5-3283-40d2-b664-ec9c3793cbca|||||; _de=B11F3A2DE590F822085556B50229AEB1; p=7e517bf054769ca03115dcd7ccdfa41a8; first_login_flag=1; ln_uact=13938386255; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=16ff33a1a5a7c1bac2f4c6754fb67ad38; societyguester=16ff33a1a5a7c1bac2f4c6754fb67ad38; id=473434718; xnsid=18c19be0; ver=7.0; loginfrom=null; jebe_key=6398ad07-4403-4ad1-a07c-691b0c18802f%7C9346b2c79ab2747ee8946889d9693ed5%7C1554362820548%7C1%7C1554362823025; wp_fold=0"
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(":")}
print(cookies)
r = requests.get("http://www.renren.com/970301096/profile", headers=headers, cookies=cookies)
# 保存界面
with open("renren3.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
