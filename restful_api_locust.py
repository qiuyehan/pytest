#coding:utf-8
from locust import HttpLocust,TaskSet,task

"""通过性能测试工具locust对公司接口进行压力测试
    locust是基于python开发的开源工具"""

form_data = {'query':'18112345678',
             'unionId':'oFmoe1FV_aSi-_SPOIcArtjOaOEA',
             'userId':'',
             'userType':'',
             'pageSize':5,
             'type':'1',
             'pageNo':1,
             'customerId':'72b948cbcb03473f83e696093f1910eb'}
header = {'Content-Type':[{"key":"Content-Type","name":"Content-Type","value":"application/x-www-form-urlencoded","description":"","type":"text"}]}


class userBehavior(TaskSet):
    """用于描述用户的行为"""

    # def on_start(self):
    #     pass
    #此方法类似于unittest中的set_up方法。每次执行其他方法时，都会先执行这个

    @task   #装饰该方法为一个事物
    def test_user(self):
        self.client.post('/v1/mtzx/clerk/ticketOrders',form_data)
        #用于指定请求的路径


class websiteUser(HttpLocust):
    """用于设置性能测试"""
    task_set = userBehavior #指向定义用户行为类
    min_wait = 3000 #执行事物之间用户等待时间的下界（ms)
    max_wait = 6000 #执行事物之间用户等待时间的上界（ms)
    host = 'http://47.107.124.228:8083/mtzx'    #被测试的主机地址

