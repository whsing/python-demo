import os

path = 'E:\\2-卓卓卓\\python-file\\httpscdn.fp35.comavid5d8882b5826d7'

for i in range(1,30):
    os.rename(path+'\\httpscdn.fp35.comavid5d8882b5826d7index' + str(i) + '.ts', path+'\\index' + str(i) + '.ts')