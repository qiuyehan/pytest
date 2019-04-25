_ga=GA1.2.750159049.1544235851
	__gads=
		ID=46ca2328557665cf:T=1544235850:S=ALNI_MbDOIjSLNVfXXQsh9Bs1Fi1C55Tsw

	_gid=GA1.2.398885987.1556114222
	ASP.NET_SessionId=nzk0qhipbgbozkav1xs0fu0l
	SERVERID=4fea726178f35f0633c3d1a5c08ace19|1556114607|1556114218


.CNBlogsCookie=B6C6F7DE26AA7339AF16B614BDF9FB9FF4D9C49B8DA0949AEC208DA44950345A1E11C74DA405FD515BC01A00DEA2DFAAECFFEFF4FDFF3F7C37F4E7EF04AC12FCDF7141E2AD64970E85744863BD0E1AEFAD3D747954B93645C008155B7E90692917C7864C; domain=.cnblogs.com; path=/; HttpOnly

Response sent 393 bytes of Cookie data:
.Cnblogs.AspNetCore.Cookies=CfDJ8JcopKY7yQlPr3eegllP76OqGEUYr1ec07KNwZTsYTB1kdgak8DcUfrGVVhh2ZGNZQpAx8jRlP9UNDbn0ia-9AHWI0U2ghhZGmFPURFWSMWa7VbvwyMDTUcxYwQIMojATDVj-nrFRyaM_LcHPKS9hDEjUvss0PTIYJR3lbPPLSRTY66n1E0SaQCUq-jWjZA9nx2-QCFmTC-Z667UHhd6ok887w4PY1D3x1bxaalNk78iqwt0pbGRDFo4Z98i_lbaWrNZSLDNO4SnnuMhKJcKsJBwj7QrfPRZmGtjasA9KdwfvpF6TvZJ26aq2W3HcUlKgA; domain=.cnblogs.com; path=/; HttpOnly

Response sent 70 bytes of Cookie data:
	Set-Cookie: SERVERID=4fea726178f35f0633c3d1a5c08ace19|1556115390|1556114218;Path=/


有些小伙伴有强迫症看到红色的心里就发慌，这里加两行代码可以忽略掉警告，眼不见为净
2.参考代码：
# coding:utf-8
import requests
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = "https://passport.cnblogs.com/user/signin"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
          }
r = requests.get(url, headers=headers, verify=False)
print(r.status_code)
