#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/29 9:23
# Author  :ZhengChengBin
# File    :hashlib_test.py

import hashlib

# md5-----------------
md5 = hashlib.md5()
md5.update('how to use md5')
md5.update('how to use 2')  # 编码
print 'md5 = ' + md5.hexdigest()
md52 = hashlib.md5()
md52.update('how to use md5how to use 2')
print 'md52 = ' + md5.hexdigest()
# 数据量很大，可以分块多次调用update(),相当于两个字符串直接相加

# sha1----------------------编译后的字符串更长
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()


# 密码保存数据库时加盐处理
def md5passwd(pwd):
    md5.update(pwd + 'the salt')  # 使得数据库中的密码不易被破译

