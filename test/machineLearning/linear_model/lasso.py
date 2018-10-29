#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/4 14:04
# Author  :ZhengChengBin
# File    :lasso.py

import numpy as np
from scipy import sparse  # 矩阵生成
from scipy import ndimage
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

# n = 128
# proj_operator = build_projection_operator(n, n / 7.)


def build_projection_operator(n_x, n_dir):
    """
    计算层析成像设计矩阵
    :param n_x: 图像矩阵的线性大小
    :param n_dir: 投影需要的的角度数量
    :return:
    """
    X, Y = _generate_center_coordinates(n_x)
    angles = np.linspace(0, np.pi, n_dir, endpoint=False)  # 0~pi ,分成n_dir份，如何endpoint=TRUE则 分成n_dir-1份
    data_inds, weights, camera_inds = [], [], []
    data_unravel_indices = np.arange(n_x ** 2)  # 平方
    data_unravel_indices = np.hstack((data_unravel_indices, data_unravel_indices))  # 把每行数据拼接在一起，要保证行数相同
    for i, angle in enumerate(angles):
        Xrot = np.cos(angle) * X - np.sin(angle) * Y  # 矩阵相减，每个对应的位置上的数相减
        inds, w = _weights(Xrot, dx=1, orig=X.min())  # 矩阵(1*n)
        mask = np.logical_and(inds > 0, inds < n_x)  # 功能（逻辑与），放回（true，false）inds.size = mask.size
        weights += list(w[mask])  # 矩阵转成list (1*n)
        camera_inds += list(inds[mask] + i * n_x)
        data_inds += list(data_unravel_indices[mask])

    # proj_operator = sparse.coo_matrix((weights, (camera_inds, data_inds)))
    # return proj_operator


def _generate_center_coordinates(l_x):
    # mgrid(x,y) 第一个元素是向右扩展，第二个元素是向下扩展（copy）,分别生成两个矩阵，矩阵的大小为x行，y列
    X, Y = np.mgrid[:l_x, :l_x].astype(np.float64)  # x 是每一行相同，（第一行为0，最后一行为l_x）,y是每一列都相同
    center = l_x / 2.
    X += 0.5 - center  # 整个矩阵每个数都添加
    Y += 0.5 - center

    return X, Y


def _weights(x, dx=1, orig=0):
    """

    :param x:矩阵
    :param dx: 放缩比例
    :param orig: 加减放缩比例
    :return:
    """
    x = np.ravel(x)  # 将多维矩阵变成单行矩阵，每一行拼接在一起
    floor_x = np.floor((x - orig) / dx)  # 将每个数变成不大于他本身的最大整数
    alpha = (x - orig - floor_x * dx) / dx
    return np.hstack((floor_x, floor_x + 1)), np.hstack((1 - alpha, alpha))


if __name__ == '__main__':
    # build_projection_operator(128, 128 / 7.)
    # build_projection_operator(128,120/7.)
    # a = np.array([1, 2, 3])  # 注意np.array和list是不一样的，
    # a = np.arange(1, 4)  # 也是生成矩阵
    #
    # b = np.array([False, True,False])
    # print 128 **2
    # print b
    # print a[b]  # 矩阵竟然可以有这种操作

    a = np.array([[1, 2, 3], [1, 2, 3]])
    print a
    print len(a), len(a[0])  # 获取矩阵行，获取矩阵列， 如果矩阵为向量，第二个数据会报错
