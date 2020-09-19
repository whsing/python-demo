#python获取文件路径， 文件名， 后缀名

import os

def get_filePath_fileName_fileExt(fileUrl):
    """
    获取文件路径， 文件名， 后缀名
    :param fileUrl:
    :return:
    """
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

if __name__ == '__main__':
    print(get_filePath_fileName_fileExt('E:\\2-卓卓卓\\python-file\\test\\index0.ts'))