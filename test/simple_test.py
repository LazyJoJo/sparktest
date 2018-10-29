#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/3 17:59
# Author  :ZhengChengBin
# File    :simple_test.py

def normal():
    a = range(10)
    print (a[-1:])  # 最后一个数的集合
    print (a[:-1])  # 除了最后一个数以外的集合


def linear():
    from sklearn import linear_model

    reg = linear_model.RidgeCV(alphas=[0.1, 0.5, 1.0])  # 自动判别选哪个参数好
    reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
    print(
        reg.alpha_,
        reg.coef_
    )


def test():
    import numpy as np
    coef = 3 * np.random.randn(50)  # 内层元素*3 (矩阵乘法)
    coef = 3 * [[1, 2, 3], [4, 5, 6]]  # 内层元素的个数放大3倍
    # print(coef)
    a = np.arange(80)  # range很像
    np.random.shuffle(coef)  # 打乱排序，只打乱内部一层
    a[10:] = 0
    # print (a)
    X = np.random.randn(50, 200)
    coef = 3 * np.random.randn(200)

    inds = np.arange(200)
    np.random.shuffle(inds)
    coef[inds[10:]] = 0  # 只保留10个非0数，表示矩阵时一维默认是列向量
    print(coef)
    y = np.dot(X, coef)  # 矩阵乘法
    print (y)

    print(np.random.normal(size=20))  # 高斯正太分布（用于加高斯噪音）

def test2():
    import pandas as pd
    import time
    import datetime
    from datetime import timedelta
    a = time.strptime('2016/01/11','%Y/%m/%d')
    print time.mktime(a)
    b = pd.to_datetime('2016/01/11', format='%Y/%m/%d')

if __name__ == '__main__':
    test2()
