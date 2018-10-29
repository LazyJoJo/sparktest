#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/2 10:23
# Author  :ZhengChengBin
# File    :const.py

class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):  # 存在相同的变量名报错
            raise self.ConstError, "can't change const.%s" % key
        if not key.isupper():  # 变量名没有大写报错
            raise self.ConstCaseError, "%s is not all uppercase" % key
        self.__dict__[key] = value  # 变量赋值
        print 'setattr'

import sys

sys.modules[__name__] = _const() # __name__表示文件的入口，相当于这个模块以_const()这个实例为入口
