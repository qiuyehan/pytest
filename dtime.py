#coding:utf-8
# import datetime
# now = datetime.datetime.now()
# s = now.strftime('%Y---%m-%d %H-%M-%S')
# y = '2018=10=10 23:23:22'
# m = datetime.datetime.strptime(y,'%Y=%m=%d %H:%M:%S')
# print(s)
import requests,json

url = r"https://passport.cnblogs.com/user/signin"
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Content-Type":"application/json; charset=utf-8"
}
# data ={}
# json = json.loads(data)
r = requests.session()
r = r.get(url,headers=header,verify=False)
print r.cookies

coe = requests.cookies.RequestsCookieJar()
coe.set(".CNBlogsCookie","B6C6F7DE26AA7339AF16B614BDF9FB9FF4D9C49B8DA0949AEC208DA44950345A1E11C74DA405FD515BC01A00DEA2DFAAECFFEFF4FDFF3F7C37F4E7EF04AC12FCDF7141E2AD64970E85744863BD0E1AEFAD3D747954B93645C008155B7E90692917C7864C",domain=".cnblogs.com",path="/")
coe.set(".Cnblogs.AspNetCore.Cookies","CfDJ8JcopKY7yQlPr3eegllP76OqGEUYr1ec07KNwZTsYTB1kdgak8DcUfrGVVhh2ZGNZQpAx8jRlP9UNDbn0ia-9AHWI0U2ghhZGmFPURFWSMWa7VbvwyMDTUcxYwQIMojATDVj-nrFRyaM_LcHPKS9hDEjUvss0PTIYJR3lbPPLSRTY66n1E0SaQCUq-jWjZA9nx2-QCFmTC-Z667UHhd6ok887w4PY1D3x1bxaalNk78iqwt0pbGRDFo4Z98i_lbaWrNZSLDNO4SnnuMhKJcKsJBwj7QrfPRZmGtjasA9KdwfvpF6TvZJ26aq2W3HcUlKgA",domain=".cnblogs.com",path="/"
)
r.cookies.update(coe)

print r.cookies
# r = requests.get(url)
# print r.url
