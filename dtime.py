#coding:utf-8
import datetime
now = datetime.datetime.now()
s = now.strftime('%Y---%m-%d %H-%M-%S')
y = '2018=10=10 23:23:22'
m = datetime.datetime.strptime(y,'%Y=%m=%d %H:%M:%S')
print s