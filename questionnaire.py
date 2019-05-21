#coding:utf-8

"""实现简单的问卷自动填写并提交"""

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://search.mtzxgf.com/index02.html?pqbcfwyj")
driver.implicitly_wait(10)

for data in range(1,2):

    #勾选页面问题
    i = 1
    while i<=40:
        js = 'document.getElementById("item%s").click();'%i
        driver.execute_script(js)
        i= i+4

    #填写问卷填写人资料
    driver.find_element_by_id("preparerName").send_keys(data)
    # driver.find_element_by_id("cityName").send_keys(data)
    # driver.find_element_by_id("positionName").send_keys(data)
    driver.find_element_by_id("groupNo").send_keys(1)

    driver.find_element_by_partial_link_text('提 交').click()
    print ("提交%s问卷成功"%data)
    sleep(3)
    # driver.find_element_by_xpath("//div[@id='popApplySuccess']/div/div/a").click()
    # driver.switch_to_alert().accept()
    # driver.quit()
    sleep(3)


