#coding:utf-8
import unittest
from function.Login import Login
from selenium import webdriver



class TTTi(unittest.TestCase):
    def setUp(self):
        self.d = webdriver.Chrome()
    def tearDown(self):
        pass
    def test_2(self):
        # a = Login(self.d,"motian","wht123456").login()
        # print(a.name)
        self.assertEqual(3,3)



if __name__ == '__main__':
    unittest.main()