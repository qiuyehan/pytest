#coding:utf-8

import re
import requests

"""正则表达式练习"""

# pattern = "https://www.qiushibaike.com/"      糗事百科网址

a = '-Hi, I am Shirley Hilton. I am his wife.'
p = r'\b[Hh]i\b'        #正则表达式一定要是字符串，不能有转义字符，如有必须把它变为普通字符
# p = re.compile(p)

sui = re.findall(p,a)
# sui = re.search(p,a)
print(sui)
print("-"*10)

# d = '-3.456,23k4,53,6 -0.01'
# y = r'\b\d+\b'
# print(re.findall(y,d))
#匹配结果是['3', '456', '53', '6', '0', '01']
#\b的定义：\b在正则表达式中表示单词的开头或结尾，空格、标点、换行都算是单词的分割
#而“\b”自身又不会匹配任何字符，它代表的只是一个位置。所以单词前后的空格标点之类不会出现在结果里。

#我的体会，[-.]等等都会被当成单词的分割。所以匹配的时候才会出现这中结果

""" 
1、长度为8-10的用户密码（以字母开头、数字、下划线）
2、验证输入只能是汉字
3、电子邮箱验证
4、URL地址验证
5、电话号码的验证
6、简单的身份证号验证
"""

d = """-3.456,23k4,53,6 -0.01 0 30
    UM_distinctid=16a0a960cbd4d5-0420b7ddb8fec6-3b60450b-1fa400-16a0a960cbe7a8
	_gid=GA1.2.1259536047.1555551692 7ddb8fec b7ddb8fe -0420b7d cbe7a8154 iii3453ikh 
	974697133@qq.com 
	18201837008@163.com  546@alibb.com 11@ing.uin 
	https://www.cnblogs.com/wordblog/p/6821329.html
	http://47.107.124.228:8083/mtzx/v1/mtzx/goods/getMediaDetail
	http:..
	http://
	http//:ien
	bbbba
	1111.yen.com
	2222.cn
	ying.org
	"""

# y = r'http://[\w-]+\.com/.*?'
# y = r'http://([\w-]+\.)+[\w]+(/[\w./?%&=]*)?'
y = r"http\S*?\.(com|cn"
# y = r"(h(bb|tt)){1}"
print(re.findall(y,d))


