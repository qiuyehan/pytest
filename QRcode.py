#coding:utf-8
from MyQR import myqr


#二维码跳转地址
url = 'https://u.wechat.com/EB9O1xdmfxzypCsVxvgzupY'
#需要与二维码结合的图片地址
fileUrl = 'myImg.jpg'
#生成二维码的名字
save_name = 'wo.png'
#保存图片的路径
save_dir = 'F:\\'
myqr.run(words=url,picture=fileUrl,colorized=True,save_name=save_name,save_dir=save_dir)