# -*-coding:utf-8-*-
import urllib.request
import sys
from bs4 import BeautifulSoup

if __name__ == '__main__':
    file = open('1.html', 'rb')
    html = file.read()
    print('type(html): ')
    print(type(html))
    bs = BeautifulSoup(html, 'html.parser')
    
    print(type(bs))
    #print(bs)
    print(bs.name)  # [document] #bs 对象本身比较特殊，它的 name 即为 [document]
    print(bs.title) # 获取title标签的所有内容
    print(bs.title.name)    # title #对于其他内部标签，输出的值便为标签本身的名称
    print(bs.head.name) # head #对于其他内部标签，输出的值便为标签本身的名称
    print(bs.a) # 获取第一个a标签的所有内容
    print(type(bs.a))   #<class 'bs4.element.Tag'>
    print(bs.a.attrs)   # a 标签的所有属性打印输出了出来，得到的类型是一个字典。
    print(bs.a['class'])    #等价 bs.a.get('class')
    
    print(bs.title.string)
    print(type(bs.title))
    print(type(bs.title.string))
    
    print(bs.a.string)
    print(type(bs.a))
    print(type(bs.a.string))
    
    with open('1-1.txt', 'w') as f:
        f.writelines(str(html, encoding='utf-8'))
        f.writelines('\n')
    
