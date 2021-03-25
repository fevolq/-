#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.03.24
# Filename:传入账户密码模拟登录的流程

import requests

headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}

#登录网址
login_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'

session = requests.Session()
#先请求一次，来使session中保存cookie
page = session.get(url=login_url,headers=headers).text  #使用session来保存cookie

#登录时需要传入的数据
data = {
    '__VIEWSTATE': 'n3LWrTW4daS6X5Zv0ZqQG47XvmjkSawJJv3TIk958Hhbkgef4UxpQ8vQPr4iyNqW27XcMH7GurwXL43RHlaOjlPmNsO37AHgYoQHAaYgwMPVyOcvQ6pulhlqMR4=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': 'xxxxxx@qq.com',   #登录账户
    'pwd': 'xxxxxx',  #登录密码
    'code': 'np2z', #验证码。动态变化的，需另外设置一个识别验证码的程序
    'denglu':'登录',
}

#传入参数进行登录，获取的是登录成功后的页面源码
response = session.post(url=login_url,data=data,headers=headers)
with open(r'C:\Users\15394\Desktop\登录.html','w',encoding='utf-8') as f:
    f.write(response.text)

#注：此时登录会失败，因为验证码是随机的，而这里只是传入了一个固定的字符串，实际应用中需动态识别验证码。
#注：最好还要验证下其他的请求参数是否是动态变化的，这些动态参数一般会隐藏在前台页面中。
