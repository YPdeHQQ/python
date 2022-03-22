import requests



# post 请求与get请求的传递参数是不一样的
response_post = requests.post(url, headers=headers, data=data)
response_get = requests.get(url, headers=headers)