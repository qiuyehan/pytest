#coding:utf-8
from data.locationTag import location
from selenium import webdriver


class jilie():
    "所有类的基类，封装导入跟调用驱动等代码"
    def __init__(self):
        self.d = webdriver.Chrome()
        self.url = r'https://xcx.mtzxgf.com.cn/#/customerManage/customerIndex'



class Login():
    """登录首页"""
    def __init__(self,name,psword,d):
        self.d = d
        # super().__init__()
        self.url = r'https://xcx.mtzxgf.com.cn/#/customerManage/customerIndex'


        self.name = name
        self.psword = psword


    def login(self):
        # self.d = webdriver.Chrome()
        self.d.get(self.url)
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.find_element(*location[u'用户名']).click()
        self.d.find_element(*location[u'用户名']).send_keys(self.name)
        self.d.find_element(*location[u'密码']).send_keys(self.psword)
        self.d.find_element(*location[u'登录按键']).click()



if __name__ == '__main__':
    d = webdriver.Chrome()
    zhangh = 'motian'
    mima = 'wht123456'
    a = Login(zhangh,mima,d)
    a.login()

#如果要执行登录后在做其他操作，可以把登录类的实例化对象，当作参数，传入其他函数中，通过调用继承一个驱动来实现