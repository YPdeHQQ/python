#带参数的get请求

# 错误的
# import requests
# url = "https://www.baidu.com"
# kw = {
#     "wd":"英雄联盟"
# }
# response = requests.get(url, params=kw)
# #解码中文字
# content = response.content.decode('utf-8')
# print(content)

# ========================================================================================



import requests

# https://www.baidu.com/s?wd=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&value=1
# https://www.baidu.com/s?wd=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F
# url = "https://www.baidu.com/s?"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
#     "Host":"www.baidu.com"
# }
# params = {
#     "wd":"英雄联盟",
#     # "value":"1"
# }
# response = requests.get(url, params=params, headers=headers)
# # con = response.status_code

# print(response.url)

# =============================================================================================================
url_link = "https://www.baidu.com/s"
text = input("请输入要搜索信息：")
params = {"wd":text}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Host":"www.baidu.com"
}
response = requests.get(url_link, headers=headers, params=params)
print(response.request.url)