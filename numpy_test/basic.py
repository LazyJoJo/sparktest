#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/10/18 10:06
# Author  :ZhengChengBin
# File    :basic.py


import numpy as np
import matplotlib.pyplot as plt

def main():
    a = np.array([2,3,4])
    l = np.ones(500)
    for i in range(500):
        x = np.random.binomial(500, 0.5)
        l[i]*=x
    print(l)
    plt.hist(l,bins=50)
    plt.show()


if __name__ == '__main__':
    main()