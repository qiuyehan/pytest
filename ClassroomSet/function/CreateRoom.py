#coding:utf-8
from time import sleep

from data.locationTag import location, inputParam
from function.Login import Login
from selenium.webdriver.common.by import By
from selenium import webdriver


class CourseFormInput(Login):
    """
    clickCourseList:进入微课堂列表页
    tianJiaCourse:点击添加微课堂，在表单输入部分数据。需提供课程名称与课程主提参数
    formInput6:填写表单输入框6项。需要提供6个输入框的数据参数
    setTime:设置时间
    inputImage:上传封面图片
    ckNextStep:点击下一步
    courseIusm:填写课程概述与课程正文。如不提供课程正文插入图片地址，则使用默认图片
    """

    def clickCourseList(self):
        """点击'微课堂列表'，进入列表页面"""

        self.d.find_element(*location['课堂目录']).click()  # 点击微课堂目录
        self.d.find_element(*location['微课堂列表']).click()  # 点击微课堂列表

    def tianJiaCourse(self,courseName='ces',theme='test'):
        """在微课堂列表点击添加按键，并在表单中输入数据 courseName=课程名称 theme=课程主题 """

        # 在表单中填写信息
        self.d.find_element(*location['添加课程按键']).click()  # 点击添加按键

        self.d.find_element(*location['课程名称']).clear()
        self.d.find_element(*location['课程名称']).send_keys(courseName)  #输入课程名称

        self.d.find_element(*location['课程类别选择框']).click()    #选择课程类别
        sleep(0.5)    #必须强制等待，不然元素定位出错。有些元素只有等前面的元素操作后才会显示出来
        self.d.find_element(*location['选择课程类别']).click() #点击类别（商学）

        self.d.find_element(*location['区域选择框']).click()    #选择区域框
        sleep(0.5)
        self.d.find_element(*location['选择区域']).click()#点击区域（华南）

        self.d.find_element(*location['团队选择框']).click()#团队选择框
        sleep(0.5)
        self.d.find_element(*location['选择团队']).click()   #选择团队

        self.d.find_element(*location['讲师选择框']).click() #讲师选择框
        sleep(0.5)
        self.d.find_element(*location['选择讲师']).click()  #选择讲师

        self.d.find_element(*location['管理员选择框']).click()#管理员选择框
        sleep(0.5)
        self.d.find_element(*location['选择管理员']).click()  #选择管理员

        self.d.find_element(*location['课程主题']).clear()#输入课程主题
        self.d.find_element(*location['课程主题']).send_keys(theme)

        self.d.find_element(*location['关联课件选择框']).click()#关联课件选择框
        sleep(0.5)
        self.d.find_element(*location['选择课件']).click()   #选择关联课件

    def formInput6(self,sequencing,MaxenlistNum,lookNumber,noLineNum,enlisNum,price):
        """微课堂排序/最大课报名数/浏览人数/在线人数/报名人数/课程单价设置 """

        paramlist = [sequencing,MaxenlistNum,lookNumber,noLineNum,enlisNum,price]
        #最后6个输入框定位输入
        goto1 = location['排序']   #排序
        goto2 = location['最大可报名数']   #最大可报名数
        goto3 = location['浏览人数']  #浏览人数
        goto4 = location['在线人数']   #在线人数
        goto5 = location['报名人数']   #报名人数
        goto6 = location['课程单价']   #课程单价
        goto = [goto1,goto2,goto3,goto4,goto5,goto6]
        i = 0
        for gotodw in goto:
            self.d.find_element(gotodw[0],gotodw[1]).clear()
            if gotodw[1] != goto6[1]:
                self.d.find_element(gotodw[0],gotodw[1]).send_keys(str(paramlist[i]))
                i += 1
            else:
                self.d.find_element(gotodw[0],gotodw[1]).send_keys(str(paramlist[5]))

    def setTime(self):
        """微课堂报名时间与开始时间设置"""

        self.d.find_element(*location['课程开始时间']).click()    #课程开始时间选择
        sleep(0.5)
        self.d.find_element(*location['课程开始时间']).send_keys(inputParam['课程开始时间'])
        sleep(0.5)
        self.d.find_element(By.XPATH,'/html/body/div[9]/div[2]/button[2]/span').click() #确定选择按键

        self.d.find_element(*location['课程结束时间']).click() #课程结束时间选择
        sleep(0.5)
        self.d.find_element(*location['课程结束时间']).send_keys(inputParam['课程结束时间'])
        sleep(0.5)
        self.d.find_element(By.XPATH,'/html/body/div[10]/div[2]/button[2]/span').click()    #确定选择按键

        self.d.find_element(*location['报名开始时间']).click()   #报名开始时间选择
        sleep(0.5)
        self.d.find_element(*location['报名开始时间']).send_keys(inputParam['报名开始时间'])
        sleep(0.5)
        self.d.find_element(By.XPATH,'/html/body/div[11]/div[2]/button[2]/span').click()

        self.d.find_element(*location['报名结束时间']).click()    #报名结束时间
        self.d.find_element(*location['报名结束时间']).send_keys(inputParam['报名结束时间'])
        sleep(0.5)
        self.d.find_element(By.XPATH,'/html/body/div[12]/div[2]/button[2]/span').click()

    def inputImage(self):
        """微课堂封面图片上传"""

        #上传图片
        imagepath = r'D:\installdata\python3\jiaoben\otherfile\ClassroomSet\data\1.jpg'
        self.d.find_element(*location['图片上传']).send_keys(imagepath)

    def ckNextStep(self):
        """微课堂列表填写，点击下一步"""

        #点击下一步
        self.d.find_element(*location['下一步按键']).click()


    def courseIusm(self,introduce,imagepath2=r'https://sf3-ttcdn-tos.pstatp.com/obj/ad-tetris-site/file/1552302815967/60087fde31e2f28707947db22c85dacb'):
        """填写课程概要信息,可以指定使用正文图片，不输入则使用默认图片"""

        #课程概要
        self.d.find_element(*location['课程概要']).clear()
        self.d.find_element(*location['课程概要']).send_keys(introduce)

        #在正文内容中插入图片

        self.d.find_element(*location['课程正文']['插入图片按键']).click()
        sleep(0.5)
        self.d.find_element(*location['课程正文']['图片url地址输入框']).click()
        sleep(0.5)
        self.d.find_element(*location['课程正文']['图片url地址输入框']).send_keys(imagepath2)
        sleep(0.5)
        self.d.find_element(*location['课程正文']['确定按键']).click()

        #暂时不需要在正文图片后面加上文字

        #点击确定，生成新的课堂
        self.d.find_element(*location['提交按键']).click()
        self.d.find_element(*location['确认提交按键']).click()

if __name__ == '__main__':
    with open(r'C:\Users\ASUS\Desktop\课程填写项.txt', encoding='utf-8') as kec: #读取文件中的参数，根据文件来填入关键参数
        param = kec.readlines()

        if location['选择团队']==[By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[2]']: #判断是测试课程，还是正式课程。据此来更改价格
            jiage = 50.0
        else:
            jiage = 0.01

        zhangh = ''
        mima = ''
        d = webdriver.Chrome()
        a = CourseFormInput(zhangh,mima,d)  #账号密码,运行时填入
        a.login()
        a.clickCourseList()
        a.tianJiaCourse(courseName=param[0],theme=param[1])  #需要传入课程名称与主题
        a.formInput6(1,100000,param[2],0,param[3],jiage)
        a.setTime()
        a.inputImage()
        a.ckNextStep()
        a.courseIusm(param[4])      #需要填写课程概要信息,也可以输入正文的图片路径
