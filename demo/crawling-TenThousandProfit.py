# -*-coding:utf-8-*-
import urllib.request,time,chardet,json,re
import sys
from bs4 import BeautifulSoup
# 写入Excel表需要使用的库
from openpyxl import Workbook

#reload(sys)
#sys.setdefaultencoding('utf-8')  # 设置系统默认编码
#print (sys.version)  # 打印当前版本信息
#sys.setdefaultencoding('utf-8')

# 配置定义
urlstart = 'http://124.115.228.93/zfrgdjpt/jggs.aspx?qy=00&yxbh=0000001307&type=2'
# 配置定义

setSQLData = []

def loads_jsonp(_jsonp):
        """
        解析jsonp数据格式为json
        :return:
        """
        try:
            return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
        except:
            raise ValueError('Invalid Input')
        
def main():
    # 爬取数据 总页数64,为了练习,就取20页
    data = []
    for i in range(1, 40):
        url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery183067232521048665_1586393453027&fundCode=002936&pageIndex='+str(i)+'&pageSize=20&startDate=&endDate=&_='+str(int(time.time()*1000))
        headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Connection': 'keep-alive','Cookie': 'st_si=68556879118769; st_asi=delete; qgqp_b_id=6f5c44da58e3229f5a5bc3d8650d86aa; EmPaVCodeCo=3fc0b644f0ca483cb3fb4cc027037563; uidal=5622375748462534%e8%82%a1%e5%8f%8bCUw8xH; sid=140453898; vtpst=|; EmFundFavorVersion=2000; p_origin=https%3A//passport2.eastmoney.com; ct=GLl6AXYdlKP61SXuDw6hXtNX8hmsfGAtJFJs4RtQB_Zo2kqNS4yM-Nu5K4kLOoajWiudNljozWomy8GrRW7FcOrV5wETKXaafHaliTPh9V_JiAy51QeHuZ4qC6TCpo1AOgPzMmUT2BLsRJLVdfcBQIzP7RHSPKISV0mhSlkhkEo; ut=FobyicMgeV7bfas_M05TDNJm38aaLVfa52GqwirbfpHtvoujr6kuApyUMcSEw1x4CDQQSf49fiYWdfU-CXWQaVzH3uabmyi5zCIlpcz9Nm6_R-eZoBGyS5wql3Rl2OOiZJJh-9xIH22srIQQRn_n-MohUHUGjttgy-g2S-LHbJPwgclRi1IH_spwPppjhXMyELSHMBEL-iuQbxWSdgePg40vzi8YEac8p0yBFLGFZ9COQtVW30rcpiQAh8OdaFbBO8M5wPhXpgvqd5vdM_ly0rZollOiPwle; pi=5622375748462534%3bh5622375748462534%3b%e8%82%a1%e5%8f%8bCUw8xH%3bxVCy4JfhqCulO44YmAjHPn01BksDMrcR24k4olXv%2bQpW5hHGn7Xvlx3TjkXqu9D0O%2bxah0dzqneGn3BMJeHXspTNYVb7WnO0i77w9XvD%2fPDtg1JqOJfEl9QMBwwKsk5o5r6NWwaYNZshwAlg%2f%2fCeQBBQIZhRZxgyzhkhOapKl2AO7UoaibRDfXs%2f3mFamkAu7y3jpGQb%3bgZ2bTo2zGCCq%2f7Y6U5%2fUNWxlXOBdVInYCN0oN4psJJaXhdHhKkC1vtXGQ3n6u8Dym5rTPw2Ga20r70hCc9jnZTo6cfSuX29TB1WTQbnfQWEH%2b15n2%2bMbQVIeBZtZXL4qaFUm1G1J5%2bH2V66uaY9uZhhMm%2fH%2bDA%3d%3d; testtc=0.7357732525257445; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null; EMFUND0=null; EMFUND9=04-09 09:10:35@#$%u7EA2%u571F%u521B%u65B0%u4F18%u6DF3%u8D27%u5E01A@%23%24005150; st_pvi=74291853600854; st_sp=2020-04-08%2014%3A41%3A40; st_inirUrl=https%3A%2F%2Fopen.weixin.qq.com%2Fconnect%2Fqrconnect; st_sn=5; st_psi=2020040909103442-0-7757783794','Host': 'api.fund.eastmoney.com','Referer': 'http://fundf10.eastmoney.com/jjjz_005150.html','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

        print ('正在获取地址:' + url)

        req = urllib.request.Request(url,headers=headers)
        res=urllib.request.urlopen(req)
        resContentType = res.headers['Content-Type']
        result = res.read()
        if type(result) == bytes:
            result = str(result, 'utf8')
        if resContentType.find('application/json') >= 0:
            result = loads_jsonp(result)
        #print(result['Data']['LSJZList'])
        data.extend(result['Data']['LSJZList'])
        #print(data)
        #break
        #bs = BeautifulSoup(result, 'html.parser', from_encoding='utf-8')
        #print(bs)
        #alllist = bs.find_all('tr')
    writeIntoExcel(data,'002936.xlsx')

def writeIntoExcel(data, dest_filename):
    # 将数据写入Excel
    wb = Workbook()
    # 设置Excel文件名
    #dest_filename = 'UserInfoFile.xlsx'
    # 新建一个表
    sheet = wb.active
    

    # 填写表内容
    for d in data:
        sheet.append(list(d.values()))

    if dest_filename.find('.') < 0:
        dest_filename += '.xlsx'
    wb.save(filename=dest_filename)  

if __name__ == '__main__':
    main()
