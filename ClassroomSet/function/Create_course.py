#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome()
d.get(r'https://xcx.mtzxgf.com.cn/#/customerManage/customerIndex')
d.maximize_window()
d.implicitly_wait(10)

#登录
loginName_location = (By.NAME,'username')
loginPsword_location = (By.NAME,'password')
loginButton = (By.TAG_NAME,'button')

def login(loginName_location,loginPsword_location,loginButton,name='motian',psword='123456'):
    d.find_element(*loginName_location).click()
    d.find_element(*loginName_location).send_keys(name)
    d.find_element(*loginPsword_location).send_keys(psword)
    d.find_element(*loginButton).click()

login(loginName_location,loginPsword_location,loginButton)

#点击微课堂添加按键
d.find_element(By.XPATH,'//div[@id="app"]/div/div[1]/div[1]/div/ul/div/li[2]/div').click()  #点击微课堂目录
d.find_element(By.LINK_TEXT,'微课堂列表').click()   #点击微课堂列表
d.find_element(By.XPATH,'//div[@id="app"]/div/div[2]/section/div/div[1]/button[2]').click()     #点击添加按键

#在添加表单中填写信息

BX = By.XPATH
d.find_element(BX,'//div[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[1]/div/div/div/input').clear()
d.find_element(BX,'//div[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[1]/div/div/div/input').send_keys(u'test(勿购）')  #输入课程名称

d.find_element(BX,'//div[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[2]/div/div/div/div[1]/input').click()    #选择课程类别
# d.find_element(By.XPATH,'//div[@x-placement="bottom-start"]/div[1]div[1]/ul/li[1]').click()
sleep(1)    #必须强制等待，不然元素定位出错。有些元素只有等前面的元素操作后才会显示出来
d.find_element(BX,'/html/body/div[3]/div[1]/div[1]/ul/li[1]').click() #点击类别（商学）

d.find_element(BX,'//div[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[3]/div[1]/div/div/div[1]/input').click()    #选择区域框
sleep(1)
d.find_element(BX,'/html/body/div[4]/div[1]/div[1]/ul/li[5]').click()#点击区域（华南）

d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/input').click()#团队选择框
sleep(1)
d.find_element(BX,'/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()   #选择团队

d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[3]/div[2]/div/div[1]/div[1]/input').click() #讲师选择框
sleep(0.5)
d.find_element(BX,'/html/body/div[6]/div[1]/div[1]/ul/li').click()  #选择讲师

d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/input').click()#管理员选择框
sleep(0.5)
d.find_element(BX,'/html/body/div[7]/div[1]/div[1]/ul/li').click()  #选择管理员

d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[3]/div[3]/div/div/input').clear()#输入课程主题
d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[3]/div[3]/div/div/input').send_keys(u"测试课程")

d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[1]/div[4]/div[3]/div/div/div[1]/input').click()#关联课件选择框
sleep(0.5)
d.find_element(BX,'/html/body/div[8]/div[1]/div[1]/ul/li[1]').click()   #选择关联课件

#最后6个输入框定位输入
goto1 = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div/input'   #排序
goto2 = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[2]/div/div/div/input'   #最大可报名数
goto3 = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[3]/div/div/div/input'   #浏览人数
goto4 = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[4]/div/div/div/input'   #在线人数
goto5 = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[5]/div/div/div/input'   #报名人数
goto6 = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[2]/div[6]/div/div/div/input'   #课程单价
goto = [goto1,goto2,goto3,goto4,goto5,goto6]
for gotodw in goto:
    d.find_element(BX,gotodw).clear()
    if gotodw != goto6:
        d.find_element(BX,gotodw).send_keys(1)
    else:
        d.find_element(BX,gotodw).send_keys(str(0.01))

#时间选择
statrtime = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[1]/div/div[1]/div/input'    #课程开始时间定位
endtime = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[1]/div/div[3]/div/input'      #课程结束时间定位
signuptime = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[2]/div/div[1]/div/input'   #报名开始时间定位
signupend = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[2]/div/div[3]/div/input'    #报名结束时间定位
d.find_element(BX,statrtime).click()    #课程开始时间选择
sleep(0.5)
d.find_element(BX,statrtime).send_keys('2019-04-10 10:54:00')
sleep(0.5)
d.find_element(BX,'/html/body/div[9]/div[2]/button[2]/span').click()

d.find_element(BX,endtime).click() #课程结束时间选择
sleep(0.5)
d.find_element(BX,endtime).send_keys('2020-04-10 10:54:00')
sleep(0.5)
d.find_element(BX,'/html/body/div[10]/div[2]/button[2]/span').click()

d.find_element(BX,signuptime).click()   #报名开始时间选择
sleep(0.5)
d.find_element(BX,signuptime).send_keys('2019-04-10 10:54:00')
sleep(0.5)
d.find_element(BX,'/html/body/div[11]/div[2]/button[2]/span').click()

d.find_element(BX,signupend).click()    #报名结束时间
d.find_element(BX,signupend).send_keys('2020-04-10 10:54:00')
sleep(0.5)
d.find_element(BX,'/html/body/div[12]/div[2]/button[2]/span').click()

#上传图片
imageUp = '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div[3]/div[3]/div/div/div[1]/div[1]/input'
imagepath = r'D:\installdata\python3\jiaoben\otherfile\1.jpg'
d.find_element(BX,imageUp).send_keys(imagepath)

#点击下一步
d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div[2]/div/button[2]/span').click()

#课程概要
d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/div/div/div/textarea').clear()
d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div[1]/div/div/div/textarea').send_keys('测试课程')

#在正文内容中插入图片
imagepath2 = 'https://sf3-ttcdn-tos.pstatp.com/obj/ad-tetris-site/file/1552302815967/60087fde31e2f28707947db22c85dacb'
d.find_element(BX,'//*[@id="mceu_21-button"]/i').click()
sleep(0.5)
d.find_element(BX,'//*[@id="mceu_55-inp"]').click()
sleep(0.5)
d.find_element(BX,'//*[@id="mceu_55-inp"]').send_keys(imagepath2)
sleep(2)
d.find_element(BX,'//*[@id="mceu_63-button"]').click()

#暂时不需要在正文图片后面加上文字


#点击确定，生成新的课堂
d.find_element(BX,'//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div[2]/div/button[2]/span').click()
d.find_element(BX,'/html/body/div[2]/div/div[3]/button[2]').click()


