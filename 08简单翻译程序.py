import requests
import json
import hashlib
# 面向对象的方法（封装函数）
class fanyi_spider(object):

    def __init__(self, query_str):
        self.query_str = query_str

        # 涉及到js解码比较复杂
        '''r = c()("6key_cibaifanyicjbysdlove1".concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16);
                return h("/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=".concat(r), {
        '''
        sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1" + self.query_str).encode('utf-8')).hexdigest())[0:16]
        

        url = "http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba"
        self.url = url + '&sign=' + sign
        
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
        }
        # 获取请求体数据
        self.data = self.get_data()


    def get_data_fromurl(self):
        """从服务器获取数据，并解码返回数据"""
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content.decode()


    def get_data(self):
        """获取请求体数据"""
        data = {
            'from': 'auto',
            'to': 'auto',
            'q': self.query_str
        }
        return data
        
    # {"status":1,"content":{"from":"en","to":"zh","out":"\u4f60\u597d","vendor":"ciba","err_no":0,"ttsLan":8,"ttsLanFrom":1}}
    def parse_data(self, json_str):
        dict_data = json.loads(json_str)
        result = dict_data['content']['out']
        print('{}翻译后的结果是:{}'.format(self.query_str, result))


    def run(self):
        # 1.获取url请求头
        # 2.发起请求获取响应
        # 3.提取数据

        json_str = self.get_data_fromurl()

        self.parse_data(json_str)

if __name__ == '__main__':
    query_str = input("请输入要翻译的内容：")
    spidr = fanyi_spider(query_str)
    spidr.run()