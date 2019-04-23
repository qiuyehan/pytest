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



d = '-3.456,23k4,53,6 -0.01 0 30'
y = r'-\b\d+\.\d*|\b0+\b'
print(re.findall(y,d))


