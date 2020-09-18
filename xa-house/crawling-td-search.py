# -*-coding:utf-8-*-
import urllib.request
import sys,os,re
from bs4 import BeautifulSoup

#reload(sys)
#sys.setdefaultencoding('utf-8')  # 设置系统默认编码
#print (sys.version)  # 打印当前版本信息
#sys.setdefaultencoding('utf-8')

urlstart = 'http://landchina.mnr.gov.cn/land/cjgs/pmcr/'
defaultFileName = '222.txt'

maxPage = 2
# 配置定义

info = 'Line 336: 2020.03.26 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202003/t20200327_7408878.htm Line 428: 2020.02.27 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202002/t20200228_7400916.htm  Line 430: 2020.02.26 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202002/t20200227_7400077.htm  Line 431: 2020.02.26 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202002/t20200227_7400094.htm  Line 433: 2020.02.26 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202002/t20200227_7400050.htm  Line 435: 2020.02.25 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202002/t20200226_7398923.htm  Line 436: 2020.02.25 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202002/t20200226_7398929.htm  Line 440: 2020.02.25 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/202002/t20200226_7398903.htm  Line 819: 2019.12.26 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191227_7373919.htm  Line 854: 2019.12.25 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191226_7372807.htm  Line 882: 2019.12.23 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191224_7369792.htm  Line 910: 2019.12.20 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191221_7367106.htm  Line 1028: 2019.12.16 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191217_7360451.htm  Line 1051: 2019.12.16 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191217_7360429.htm  Line 1054: 2019.12.16 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191217_7360463.htm  Line 1098: 2019.12.12 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191213_7354379.htm  Line 1152: 2019.12.11 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201912/t20191212_7332364.htm  Line 1207: 2019.11.19 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201911/t20191120_7314732.htm  Line 1263: 2019.11.13 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201911/t20191114_7308875.htm  Line 1313: 2019.11.06 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201911/t20191107_7302688.htm  Line 1455: 2019.10.23 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201910/t20191024_7289077.htm  Line 1946: 2019.09.25 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201909/t20190926_7258435.htm  Line 2091: 2019.09.11 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201909/t20190912_7247385.htm  Line 2129: 2019.09.03 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201909/t20190904_7240425.htm  Line 2248: 2019.08.20 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201908/t20190821_7222691.htm  Line 2426: 2019.07.30 西安市自然资源与规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190731_7206064.htm  Line 2427: 2019.07.30 西安市自然资源与规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190731_7206063.htm  Line 2428: 2019.07.30 西安市自然资源与规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190731_7206062.htm  Line 2429: 2019.07.30 西安市自然资源与规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190731_7206061.htm   Line 2434: 2019.07.30 西安市自然资源与规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190731_7206041.htm   Line 2435: 2019.07.30 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190731_7206040.htm   Line 2488: 2019.07.23 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190724_7199962.htm   Line 2489: 2019.07.23 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190724_7199914.htm   Line 2490: 2019.07.23 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190724_7199913.htm   Line 2505: 2019.07.22 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190723_7199141.htm   Line 2507: 2019.07.22 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190723_7199139.htm   Line 2509: 2019.07.22 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190723_7199136.htm   Line 2510: 2019.07.22 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190723_7199135.htm   Line 2547: 2019.07.17 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190718_7195713.htm   Line 2567: 2019.07.16 西安市自然资源和规划局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201907/t20190717_7194240.htm   Line 2810: 2019.06.26 西安市国土资源局国有土地使用权招拍挂出让成交公示 http://landchina.mnr.gov.cn/land/cjgs/pmcr/201906/t20190627_7170911.htm'
data = []

def main():
    dataChild = []
    # 爬取数据 总页数64,为了练习,就取20页
    for d in re.finditer(r'http://((\d*)([a-z]*)([A-Z]*)(\.*)(\/*)(\_*))*.htm', info):
        #print(d.group())
        url = d.group()
        #headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

        print ('正在获取地址:' + url)

        #request = urllib.request.Request(url=url,headers=headers)
        res=urllib.request.urlopen(url)
        html = res.read().decode()
        data.append(html)
        
        #print(data)
        writeTxt(data)

def writeTxt(data, fileName=defaultFileName):
    with open(fileName, 'w') as f:
        for d in data:
            f.writelines(d)
            f.writelines('\n')
    

if __name__ == '__main__':
    print()
    main()