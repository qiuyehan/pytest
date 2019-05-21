#coding:utf-8
import copy


paword = """	_ga=GA1.2.2049249123.1551147048
	__gads=
		ID=1c4bb8fbb76c3594:T=1551931685:S=ALNI_Ma93dzCeUNIRkOH62RqnStPEEGRgA

	UM_distinctid=16a0a960cbd4d5-0420b7ddb8fec6-3b60450b-1fa400-16a0a960cbe7a8
	_gid=GA1.2.1259536047.1555551692
	
	ASP.NET_SessionId=wprnfw5ikywb3ckwbqvgptqb
	SERVERID=4fea726178f35f0633c3d1a5c08ace19|1555582216|1555582213"""

yi = """	_ga=GA1.2.2049249123.1551147048
	__gads=
		ID=1c4bb8fbb76c3594:T=1551931685:S=ALNI_Ma93dzCeUNIRkOH62RqnStPEEGRgA

	UM_distinctid=16a0a960cbd4d5-0420b7ddb8fec6-3b60450b-1fa400-16a0a960cbe7a8
	CNZZDATA3347352=cnzz_eid%3D1826347091-1554951383-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1554963159
	_gid=GA1.2.1259536047.1555551692
	.CNBlogsCookie=7AE4446CB2561BA796ACD137CC1D483A86BE9190B32E51DFD46DA91EF2DD7EF243AAF13E03E855AE8C0044979FD14E8D503AE58BADD723C88F36D329A45291BA20B7C090EF79F768FCC66E7737448BD538B01BAB9BB6894EAD756AA23F4166C7977E67D3
	.Cnblogs.AspNetCore.Cookies=CfDJ8JcopKY7yQlPr3eegllP76NNBvFKQj03FsoeAWGJgZw7H_G2q10x2pBQRGCfAWxmyXhlMOOX7Nr_W48XC6r3EneBGFN4oAUJ4MTafvOMAsKtPxreZM2Y87i-ZdLGms4L2ufR8uiJOlF8S8vCzz9vCzb0zjPiteaxRlxJWr0_eDrO0LihhTdmfv8FVwAZp0BBQKR-S3mspOKj-JdBBHeNFypQHCINUiPGYit2do2dmFsFStn_0rzToTKvWMuhDAT-hDFxEGuzR9THaXYtYmHK6kAEjT1q7aVt4abmZOH7kl7N1t35FBGLgvQQSsD5aEDCwQ
"""
class paramHandle():
    """1.用于处理接口的xxx-form类型参数，使其更好辨识与处理
       2.用于比较2个字符串是否一致
    """
    def __init__(self,paword):
        self.paword = paword


    def xxx_formData(self):
        #根据换行符切片成list

        paword = self.paword.split('\n')

        return paword


    def tihuan(slef,List):
        """配合map遍历替换List中的制表符\t"""

        old = '\t'
        a = List.replace(old,'')
        return a

    def runFormData(self):
        "作用:字符型数据按换行切片，然后再去除字表符与字符前的多余空格。返回一个干净的list"

        #把依据换行符切片之后的list赋值
        paword = self.xxx_formData()

        #使用map函数对每个list中元素加工，去除\t
        tipList = list(map(self.tihuan,paword))

        newList = [i for i in tipList if i !='']    #去掉空的元素
        # while '' in newList:
        #     print("yes")
        #     newList.remove('')
        #-----错误的方法------
        #删除多余的空值

        # for t in tipList:
        #     if t == '':
        #         tipList.remove(t)
        #         print('t:',t)
        #         # del tipList[i]
        NewList = []
        for t in newList:

            NewList.append(t.strip())
        for i in NewList:

            print('\t',i)
        return NewList

    def compareStr(self,yi):
        """比对参数，如果一致就返回交集，如果不一致则返回不同部分"""
        if self.paword == yi:
            print("True")
            return set([yi])&set([self.paword])
        else:
            print("False")
            return [self.paword].difference([self.yi])

    def jiaoji(self,danList):

        pass
        # return  [self.paword].difference([self.yi])



if __name__ == '__main__':

    A = """
    _ga=GA1.2.2049249123.1551147048;
     __gads=ID=1c4bb8fbb76c3594:T=1551931685:S=ALNI_Ma93dzCeUNIRkOH62RqnStPEEGRgA; 
     UM_distinctid=16a0a960cbd4d5-0420b7ddb8fec6-3b60450b-1fa400-16a0a960cbe7a8; 
     CNZZDATA3347352=cnzz_eid%3D1826347091-1554951383-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1554963159; 
     .CNBlogsCookie=7AE4446CB2561BA796ACD137CC1D483A86BE9190B32E51DFD46DA91EF2DD7EF243AAF13E03E855AE8C0044979FD14E8D503AE58BADD723C88F36D329A45291BA20B7C090EF79F768FCC66E7737448BD538B01BAB9BB6894EAD756AA23F4166C7977E67D3; .Cnblogs.AspNetCore.Cookies=CfDJ8JcopKY7yQlPr3eegllP76NNBvFKQj03FsoeAWGJgZw7H_G2q10x2pBQRGCfAWxmyXhlMOOX7Nr_W48XC6r3EneBGFN4oAUJ4MTafvOMAsKtPxreZM2Y87i-ZdLGms4L2ufR8uiJOlF8S8vCzz9vCzb0zjPiteaxRlxJWr0_eDrO0LihhTdmfv8FVwAZp0BBQKR-S3mspOKj-JdBBHeNFypQHCINUiPGYit2do2dmFsFStn_0rzToTKvWMuhDAT-hDFxEGuzR9THaXYtYmHK6kAEjT1q7aVt4abmZOH7kl7N1t35FBGLgvQQSsD5aEDCwQ; 
     _gid=GA1.2.2075535128.1555999450; _gat=1
    """
    B = """
    _ga=GA1.2.2049249123.1551147048;
     __gads=ID=1c4bb8fbb76c3594:T=1551931685:S=ALNI_Ma93dzCeUNIRkOH62RqnStPEEGRgA; 
     UM_distinctid=16a0a960cbd4d5-0420b7ddb8fec6-3b60450b-1fa400-16a0a960cbe7a8; 
     CNZZDATA3347352=cnzz_eid%3D1826347091-1554951383-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1554963159; 
     .CNBlogsCookie=7AE4446CB2561BA796ACD137CC1D483A86BE9190B32E51DFD46DA91EF2DD7EF243AAF13E03E855AE8C0044979FD14E8D503AE58BADD723C88F36D329A45291BA20B7C090EF79F768FCC66E7737448BD538B01BAB9BB6894EAD756AA23F4166C7977E67D3; .Cnblogs.AspNetCore.Cookies=CfDJ8JcopKY7yQlPr3eegllP76NNBvFKQj03FsoeAWGJgZw7H_G2q10x2pBQRGCfAWxmyXhlMOOX7Nr_W48XC6r3EneBGFN4oAUJ4MTafvOMAsKtPxreZM2Y87i-ZdLGms4L2ufR8uiJOlF8S8vCzz9vCzb0zjPiteaxRlxJWr0_eDrO0LihhTdmfv8FVwAZp0BBQKR-S3mspOKj-JdBBHeNFypQHCINUiPGYit2do2dmFsFStn_0rzToTKvWMuhDAT-hDFxEGuzR9THaXYtYmHK6kAEjT1q7aVt4abmZOH7kl7N1t35FBGLgvQQSsD5aEDCwQ; 
     _gid=GA1.2.2075535128.1555999450; _gat=1
    """
    a = paramHandle(A).runFormData()
    # b = paramHandle(B).runFormData()
    # d = paramHandle(B)
    # d.runFormData()
    # c = a.compareStr(B)
    print("___",a)


