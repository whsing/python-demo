#test 多线程
import asyncio, time, aiohttp, requests

url = 'https://cdn.sw92.com/963ECD/index0.ts'

#@asyncio.coroutine
async def hello(url, i, semphore):
    async with semphore:
        async with aiohttp.ClientSession() as session:
            #print(url, '***', i)
            async with session.get(url) as res:
                print(url, '***', i)
                return await res.read()
async def run():
    semphore = asyncio.Semaphore(20)
    tasks = []
    for i in range(1000):
        tasks.append(hello(url, i, semphore))
    
    await asyncio.wait(tasks)

if __name__ =='__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    print(time.ctime())
    loop.run_until_complete(run())
    print(time.ctime())
    loop.close()