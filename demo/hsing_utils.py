#一些python简便工具
import re, datetime

#url地址去除不符合文件夹名称的字符
def replace_url_to_fold_name(url):
    return re.sub(r'\\|\/|:|\*|\?|"|<|>|\|', '', url)

#当前时间格式化
def f_now():
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')