from moviepy.editor import *
import os
import time
from natsort import natsorted

path = 'E:\\2-卓卓卓\\python-file\\test\\'

L = []
for root, dirs, files in os.walk(path):
    print(root,dirs,files)
    #files.sort()
    files = natsorted(files)
    for file in files:
        filePath= os.path.join(root, file)
        #print(os.path.splitext(filePath))
        if file.startswith('index'):
            print('载入：', filePath,time.ctime())
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)

final_clip.to_videofile(path + 'target-from-py2.mp4', fps=24, remove_temp=True)
print('Done!!!', time.ctime())