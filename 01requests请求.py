# 1.urllib:[内置库，不需要额外安装，较老了]【使用不方便】
# 2.requests:[需要额外安装]【使用较方便】

# import requests
# url = "https://www.baidu.com"
# response = requests.get(url)
# print(response.content)
# #content 是bytes流数据
# html = response.content.decode("utf-8")
# #decode 是解码
# #encode 是编码
# print(html)

#=====================================================================

# import requests
# url = "https://www.baidu.com"
# response = requests.get(url)
# response.encoding = response.apparent_encoding
# response.apparent_encoding  备用编码

# print(response.text)