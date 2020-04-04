# -*-coding:utf-8-*-
import urllib.request
import sys
from bs4 import BeautifulSoup
# 写入Excel表需要使用的库
from openpyxl import Workbook

#reload(sys)
#sys.setdefaultencoding('utf-8')  # 设置系统默认编码
#print (sys.version)  # 打印当前版本信息
#sys.setdefaultencoding('utf-8')

# 配置定义
#crawType = '意向登记公示'
crawType = '参与摇号公示'
urlstart = 'http://124.115.228.93/zfrgdjpt/jggs.aspx?qy=00&yxbh=0000001307&type=2'
maxPage = 157
projectName = '大华·公园世家3#地块1、5、6、7#'
# 配置定义

setSQLData = []

def main():
    # 爬取数据 总页数64,为了练习,就取20页
    for i in range(1, maxPage+1):
        url = urlstart + '&page=' + str(i)
        #headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}

        print ('正在获取地址:' + url)

        #request = urllib.request.Request(url=url,headers=headers)
        res=urllib.request.urlopen(url)
        html = res.read()
        #print(html)
        bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        #print(bs)
        alllist = bs.find_all('tr')

        # 对数据进行处理筛选
        if crawType == '意向登记公示':
            doRegistInfo(alllist)
        elif crawType == '参与摇号公示':
            doLotNumInfo(alllist)
    if crawType == '意向登记公示':
        titleList = ['流水号', '姓名', '证件类型', '证件号码', '购房家庭类型', '登记时间', '修改时间', '核验状态']
        writeIntoExcel(titleList)
    elif crawType == '参与摇号公示':
        titleList = ['意向登记号', '姓名', '证件类型', '证件号码', '购房家庭类型']
        writeIntoExcel(titleList)

def doRegistInfo(alllist):
    for contenttd in alllist:
        #print(contenttd)
        tds = contenttd.find_all('td')
        if len(tds) == 0 :
            continue

        seq = tds[0].text
        name = tds[1].text
        cardType = tds[2].text
        cardNo = tds[3].text
        buyType = tds[4].text
        registTime = tds[5].text
        registUpdateTime = tds[6].text
        registStatus = tds[7].text

        row = [seq, name, cardType, cardNo, buyType, registTime, registUpdateTime, registStatus]

        setSQLData.append(row)#将每条数据再次写入列表
        i = i+1
        print (row)


def doLotNumInfo(alllist):
    for contenttd in alllist:
        #print(contenttd)
        tds = contenttd.find_all('td')
        if len(tds) == 0 :
            continue

        seq = tds[0].text
        name = tds[1].text
        cardType = tds[2].text
        cardNo = tds[3].text
        buyType = tds[4].text

        row = [seq, name, cardType, cardNo, buyType]

        setSQLData.append(row)#将每条数据再次写入列表
        print (row)

def writeIntoExcel(titleList, dest_filename=crawType+'-'+projectName+'.xlsx'):
    # 将数据写入Excel
    wb = Workbook()
    # 设置Excel文件名
    #dest_filename = 'UserInfoFile.xlsx'
    # 新建一个表
    ws1 = wb.active

    # 设置表头
    #titleList = ['流水号', '姓名', '证件类型', '证件号码', '购房家庭类型', '登记时间', '修改时间', '核验状态']
    for row in range(len(titleList)):
        c = row + 1
        ws1.cell(row=1, column=c, value=titleList[row])

    # 填写表内容
    for listIndex in range(len(setSQLData)):
        ws1.append(setSQLData[listIndex])

    if dest_filename.find('.') < 0:
        dest_filename += '.xlsx'
    wb.save(filename=dest_filename)

if __name__ == '__main__':
    main()
