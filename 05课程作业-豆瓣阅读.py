"""
 网址：https://movie.douban.com/review/14115015/?from=gallery

"""
import requests
#=====================================================================================================
"""
# url = "https://movie.douban.com/review/14115015/?from=gallery"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
# response = requests.get(url, headers=headers)
# html = response.content.decode('utf-8')
# # print(html)
# with open('douban.html', 'w', encoding='utf8') as f:
#     f.write(html)
"""
#=====================================================================================================
url = 'https://movie.douban.com/review/14122109/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    #可以继续添加请求头refer
    }
response = requests.get(url, headers=headers)
con = response.content.decode('utf8')
# print(con)
with open('豆瓣电影影评.html', 'w', encoding='utf8') as f:
    f.write(con)