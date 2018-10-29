#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/27 10:34
# Author  :ZhengChengBin
# File    :file_io_test.py


f = open('C:\Users\zcb\Desktop\SVN.txt', 'r')  # 默认是AII编码的  # 后面参数是权限设置r,w,a（加到文件末尾）,r+(读写)
# f.read()  # 全部读取
# f.read(50)  # 单位kb
# f.write()  #写入数据
# f = open('/Users/michael/test.jpg', 'rb')  # rb读取二进制文件，  图片视频等都属于这类文件

f.close()

import codecs


def readf():
    f = codecs.open('C:\Users\zcb\Desktop\SVN.txt', 'r', 'gbk')  # 可以设置编码的读取
    flist = f.readlines()  # 也是一次性加载所有数据
    for line in flist:
        print line.strip()  # 去除尾部/n
    f.close()


def writef():
    f = codecs.open('C:\Users\zcb\Desktop\SVN.txt', 'a', 'gbk')
    flist = [u'测试', u'用例']
    f.writelines(flist)
    f.close()


# 简单的写法：(with)会自动封装f.close()
def readf2():
    with codecs.open('C:\Users\zcb\Desktop\SVN.txt2', 'r', 'gbk'):
        print f.read()


# 读写大量数据

# 利用open（“”， “”）系统自带方法生成的迭代对象 (推荐使用，原理不明)
def readBigf():
    with codecs.open('C:\Users\zcb\Desktop\SVN.txt', 'r', 'gbk') as f:
        for line in f:
            print line.strip()


# 读取固定文本大小（比较复杂）
def readBigf2():
    file_path = 'C:\Users\zcb\Desktop\SVN.txt'
    a = read_in_block(file_path)
    for block in a:
        print block


def read_in_block(file_path):
    BLOCK_SIZE = 1024
    with codecs.open(file_path, "r", 'gbk') as f:
        while True:
            block = f.read(BLOCK_SIZE)  # 每次读取固定长度到内存缓冲区
            if block:
                yield block  #返回 一个 iterable对象，执行完后print block后，又回到这里继续下一行操作，这样每次只处理一个block，节省内存
            else:
                print 'end'
                return  # 如果读取到文件末尾，则退出循环




if __name__ == '__main__':
    readBigf2()
