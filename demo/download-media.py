import requests
import time
import sys
import os

rootPath = 'E:\\2-卓卓卓\\python-file\\'

url1 = sys.argv[1]
savePath = rootPath + url1.replace('/','').replace(':','').replace('?','')
print(savePath)
rangeStart = int(sys.argv[2])
rangeEnd = int(sys.argv[3])

if not os.path.exists(savePath):
    os.makedirs(savePath)

for i in range(rangeStart, rangeEnd):
    fileName = 'index' + str(i) + '.ts'
    url = url1 + fileName
    print('开始下载：', url, time.ctime())
    res = requests.get(url, stream=True, timeout=100)
    
    with open(savePath + '\\' + fileName, 'wb') as mp4:
        for chunk in res.iter_content(chunk_size=1024*1024):
            if chunk:
                mp4.write(chunk)
    print('下载结束：', url, time.ctime())