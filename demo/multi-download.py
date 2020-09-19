#coding: utf-8
#!/usr/bin/env python
import queue
import threading
import time
import requests
import hsing_utils
import os, sys

# 定义同时处理任务数
queue = queue.Queue(maxsize=10)
url = sys.argv[1]

# 生成任务列表
def taskList():
    tasks = []
    download_path = os.path.join(os.getcwd(), 'download')
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    
    download_path = os.path.join(download_path, hsing_utils.replace_url_to_fold_name(url))
    print('保存路径：', download_path, hsing_utils.f_now())
    if os.path.exists(download_path):
        raise BaseException('路径已存在')
    else:
        os.mkdir(download_path)
    
    all_content = requests.get(url).text
    all_content_len = len(all_content)
    if all_content_len > 400:
        print(all_content[0:200])
        print('...')
        print('...')
        print(all_content[all_content_len-200:all_content_len])
    else:
        print(all_content)
    
    if '#EXTM3U' not in all_content:
        raise BaseException('非m3u8的链接')
    
    if 'EXT-X-STREAM_INF' in all_content:
        pass
    
    p_url = url.rsplit('/', 1)[0]
    #raise BaseException('iiiiiiiiiiiii')
    for line in all_content.split('\n'):
        if '.ts' in line and not '/' in line:
            ts_url = p_url  + '/' + line
            file_path = os.path.join(download_path, line)
            tasks.append((ts_url, file_path))
    return tasks

# 把任务放入队列中
class Producer(threading.Thread):
    def __init__(self, name, queue):
        self.__name = name
        self.__queue = queue
        super(Producer, self).__init__()

    def run(self):
        for ip in taskList():
            self.__queue.put(ip)


# 线程处理任务
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        self.__name = name
        self.__queue = queue
        super(Consumer, self).__init__()

    def run(self):
        while True:
            params = self.__queue.get()
            download(params[0], params[1])
            self.__queue.task_done()

def download(url, filePath):
    print("开始下载:", url)
    r = requests.get(url, stream=True, timeout=100)

    if r.status_code == 200:
        with open(filePath, "wb") as mp4:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    mp4.write(chunk)
        print("下载成功:", url)
    else:
        print('错误', r.status_code, ':', url)

def consumer_process(ip):
    time.sleep(1)
    print (ip)


def startConsumer(thread_num):
    t_consumer = []
    for i in range(thread_num):
        c = Consumer(i, queue)
        c.setDaemon(True)
        c.start()
        t_consumer.append(c)
    return t_consumer

def main():
    p = Producer("Producer task0", queue)   #生产者
    p.setDaemon(True)
    p.start()
    startConsumer(30) # 开启n个消费者

    # 确保所有的任务都生成
    p.join()

    # 等待处理完所有任务
    queue.join()



if __name__ == '__main__':
    print ('------start-------', hsing_utils.f_now())
    main()
    print ('------end-------', hsing_utils.f_now())