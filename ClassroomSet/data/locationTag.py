#coding:utf-8
from selenium.webdriver.common.by import By

#定位方法与路径

location = {
    #选择框类型
    '用户名':[By.NAME,'username'],
    '密码':[By.NAME,'password'],
    '登录按键':[By.TAG_NAME,'button'],
    '课堂目录':[By.XPATH,'//div[@id="app"]/div/div[1]/div[1]/div/ul/div/li[2]/div'],
    '微课堂列表':[By.LINK_TEXT,'微课堂列表'],
    '添加课程按键':[By.XPATH,'//div[@id="app"]/div/div[2]/section/div/div[1]/button[2]'],
    '课程类别选择框':[By.XPATH,'//div[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[1]/input'],
    '选择课程类别':[By.XPATH,'/html/body/div[3]/div[1]/div[1]/ul/li[1]'],
    '区域选择框':[By.XPATH,'//div[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[3]/div[1]/div/div/div[1]/input'],
    '选择区域':[By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[5]'],
    '团队选择框':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/input'],
    '选择团队':[By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]'],
    '讲师选择框':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[3]/div[2]/div/div[1]/div[1]/input'],
    '选择讲师':[By.XPATH,'/html/body/div[6]/div[1]/div[1]/ul/li'],
    '管理员选择框':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/input'],
    '选择管理员':[By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li'],
    '关联课件选择框':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[4]/div[3]/div/div/div[1]/input'],
    '选择课件':[By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[1]'],
    '课程开始时间':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[1]/div/div[1]/div/input'],
    '课程结束时间':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[1]/div/div[3]/div/input'],
    '报名开始时间':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[2]/div/div[1]/div/input'],
    '报名结束时间':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[2]/div/div[3]/div/input'],
    '图片上传':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[3]/div/div/div[1]/div[1]/input'],
    '下一步按键':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div[2]/div/button[2]/span'],
    '提交按键':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div[2]/div/button[2]/span'],
    '确认提交按键':[By.XPATH,'/html/body/div[2]/div/div[3]/button[2]'],
    #输入框类型
    '课程名称':[By.XPATH,'//div[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[1]/div/div/div/input'],
    '课程主题':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[3]/div[3]/div/div/input'],
    '排序':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div/input'],
    '最大可报名数':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/input'],
    '浏览人数':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[3]/div/div/div/input'],
    '在线人数':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[4]/div/div/div/input'],
    '报名人数':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[5]/div/div/div/input'],
    '课程单价':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[6]/div/div/div/input'],
    '课程概要':[By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/div/div/div/textarea'],
    '课程正文':{
        '插入图片按键':[By.XPATH,'//*[@id="mceu_21-button"]/i'],
        '图片url地址输入框':[By.XPATH,'//*[@id="mceu_55-inp"]'],
        '确定按键':[By.XPATH,'//*[@id="mceu_63-button"]'],
    },
}
#更改团队,创建对外数据
# location['选择团队'] = [By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[2]']

#输入的参数
inputParam ={
    "课程开始时间":"2020-04-10 10:54:00",
    "课程结束时间":"2020-04-10 10:55:00",
    "报名开始时间":"2019-04-10 10:54:00",
    "报名结束时间":"2020-04-10 10:54:00",
    'imagepath':r'D:\installdata\python3\jiaoben\otherfile\1.jpg',#图片地址
}

# with open(r'C:\Users\ASUS\Desktop\课程填写项.txt', encoding='utf-8') as kec:
#     param = kec.readlines()
#     print(param)
# print(param[0])

# zhangh = 'motian'
# mima = 'wht123456'