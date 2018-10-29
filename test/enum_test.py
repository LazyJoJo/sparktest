#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/2 14:11
# Author  :ZhengChengBin
# File    :enum_test.py

from enum import Enum


# 假的enum
class Month(Enum):
    jan, feb, mar, apr = range(4)


print Month.__dict__
print Enum.__dict__
print Month.jan

# python 2.7不支持使用enum，3.4之后才有
# for name, member in Month.__members__.items():
#     print name, '=>', member, ',', member.value

seq = range(5)
a = enumerate(seq, 1)  # 不是枚举类型
