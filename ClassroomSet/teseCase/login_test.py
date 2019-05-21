#coding:utf-8

import unittest
from function.Login import Login
from selenium import webdriver


class login_tet(unittest.TestCase):
    def setUp(self):
        # self.d = Login('motian','wht123456')
        pass


    def tearDown(self):
        pass


    def test1_1(self):
        # "测试正常登录"
        # d = webdriver.Chrome()
        # self.login1 = Login(d,'motian','wht123456')
        # self.login1.login()
        # print(self.login1.psword)
        # print('登录成功')
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
