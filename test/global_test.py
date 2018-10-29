#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/28 14:33
# Author  :ZhengChengBin
# File    :global_test.py


a = 3


def test1():
    global a
    a = 4  # 这里面还是局部变量，方法内优先使用局部变量
    print a


def test2():
    print a


if __name__ == '__main__':
    test1()
    test2()
