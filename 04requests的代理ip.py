import requests

url = "http://httpbin.org/get"
proxy = {
    "HTTP":"112.120.34.23:9999"

}
response = requests.get(url, proxies=proxy)
# content = response.content.decode('utf8')
# html = response.encoding = response.apparent_encoding #解码方式二:apparent_encoding备用编码方案
response.encoding = 'utf-8'  #解码方式三:encoding直接指定编码
# response.status_code
print(response.status_code) #打印状态码
# print(content) #打印测试信息
# print(response)   #<Response [200]>
print(response.text) #打印结果信息

'''
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.25.1",
    "X-Amzn-Trace-Id": "Root=1-61d84570-0a56c5f4775880e505085110"
  },
  "origin": "113.77.131.171",
  "url": "http://httpbin.org/get"
}
'''