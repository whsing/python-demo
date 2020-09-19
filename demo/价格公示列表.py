import requests
from bs4 import BeautifulSoup
import urllib.request

def main():
    res = urllib.request.urlopen('http://124.115.228.93/zfrgdjpt/jggs.aspx?qy=00&yxbh=0000001307&type=2')
    bs = BeautifulSoup(res.read(), 'html.parser', from_encoding='utf-8')
    print(bs)

if __name__ == '__main__':
    main();