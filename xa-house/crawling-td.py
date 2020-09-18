# -*-coding:utf-8-*-
import urllib.request
import sys,os
from bs4 import BeautifulSoup

#reload(sys)
#sys.setdefaultencoding('utf-8')  # 设置系统默认编码
#print (sys.version)  # 打印当前版本信息
#sys.setdefaultencoding('utf-8')

urlstart = 'http://landchina.mnr.gov.cn/land/cjgs/pmcr/'
defaultFileName = '拍卖出让-结果公示.txt'

maxPage = 119
# 配置定义

data = []

def main():
    dataChild = []
    # 爬取数据 总页数64,为了练习,就取20页
    for i in range(1, maxPage+1):
        url = urlstart + 'index_' + str(i) + '.htm'
        #headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

        print ('正在获取地址:' + url)

        #request = urllib.request.Request(url=url,headers=headers)
        res=urllib.request.urlopen(url)
        html = res.read().decode()
        #print(html)
        bs = BeautifulSoup(html, 'html.parser')
        #print(type(bs))
        for ull in bs.find_all('ul', attrs={'class': 'gu-iconList'}):
            for lii in ull.find_all('li'):
                dataChild = []
                dataChild.append(lii.find('span').text)
                dataChild.append(lii.find('a').text)
                dataChild.append(urlstart + lii.find('a').get('href').replace('./',''))
            
                data.append(dataChild)
        
        #print(data)
        writeTxt(data)

def writeTxt(data, fileName=defaultFileName):
    with open(fileName, 'w') as f:
        for d in data:
            f.writelines(' '.join(d))
            f.writelines('\n')
    

if __name__ == '__main__':
    main()
