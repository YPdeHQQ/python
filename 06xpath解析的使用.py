"""
nodename	选取此节点的所有子节点	div	选取div下的所有标签
//	从全局节点中选择节点，任意位置均可	//div	选取整个HTML页面的所有div标签
/	选取某个节点下的节点	//head/title	选取head标签下的title标签
@	选取带某个属性的节点	//div[@id]	选择带有id属性的div标签
.	当前节点下	./span	选择当前节点下的span标签【代码中威力强大】

===================================================================================================
//head/meta[1]                 选择所有head下的第一个meta标签
//head/meta[k]                 选择所有head下的第k个meta标签         
//head/meta[last()]	           选择所有head下的最后一个meta标签
//head/meta[position()<3]	   选择所有head下的前两个meta标签
//div[@id]	                   选择带有id属性的div标签
//div[@id='u1']	               选择所有拥有id=u1的div标签

=========================================================================================================
3.通配符
通配符	         描述	         示例	             结果
*	匹配任意节点	//div[@id='u1']/*	       选择所有拥有id=u1的div标签下的所有节点
@*	匹配节点中的任何属性	 //meta[@*]         选择所有拥有属性的meta标签
                           //a[@*]            选择所有拥有属性的meta标签

————————————————
版权声明：本文为CSDN博主「Python伊甸园」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42830697/article/details/102669236
————————————————————————————————————————————————————————————————————————————————————————————————————
"""

import requests
from lxml import etree
# 链接：https://www.baidu.com
url = "https://www.baidu.com"
response = requests.get(url)
response.encoding = response.apparent_encoding
# print(response.text)
html = response.text
tree = etree.HTML(html)
# 获取百度title
# baidu_title = tree.xpath('//title')#返回[<Element title at 0x1a1c43a89c0>]
baidu_title = tree.xpath('//title/text()')# 返回['百度一下，你就知道']
print(baidu_title)

# 获取div下ul的li标签元素
baidu_info = tree.xpath('//ul[@id="hotsearch-content-wrapper"]/li/text()')
print(baidu_info)

