# 人人网的登录


import requests

# url = "http://www.renren.com"
url = "http://www.renren.com/Plogin.do"    #在网页源代码元素中向上查找到from表单中的地址才是真实的，action元素后
headers = {
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

# post请求中formdata参数中添加
#登录的账号密码
data = {
    "email":"12345678@qq.com",
    "password":"qwer123456",
}
# 模拟登录 session会话
# 初始化session对象
session = requests.session()
session.post(url, data=data, headers=headers)

# 登录成功
# 事先登录好的地址
response = session.get("http://www.renren.com/xxxxx")
content = response.content.decode('utf-8')

# 写入html文件
with open('renren.html', 'w', encoding='utf-8')as f:
    f.write(content)