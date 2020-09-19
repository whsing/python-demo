import sys
import requests
import os
import datetime
import hsing_utils
import asyncio, aiohttp

async def download(url, file_path, semphore):
    async with semphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                print('开始写入：', file_path, f_now())
                with open(file_path, 'wb') as f:
                    for chunk in res.iter_content(chunk_size = 1024*1024):
                        if chunk :
                            f.write(res.content)
                    f.flush
                    print('写入完成：', file_path, f_now())
                return

async def run(url):
    semphore = asyncio.Semaphore(20)
    tasks = []
    
    download_path = os.path.join(os.getcwd(), 'download')
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    
    download_path = os.path.join(download_path, hsing_utils.replace_url_to_fold_name(url))
    print('保存路径：', download_path, f_now())
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
            tasks.append(download(ts_url, file_path, semphore))
    await asyncio.wait(tasks)

def f_now():
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

if __name__ =='__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    print('开始执行***', f_now())
    loop.run_until_complete(run(sys.argv[1]))
    print('执行完成***', f_now())
    loop.close()