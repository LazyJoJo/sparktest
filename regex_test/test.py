#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/10/16 16:54
# Author  :ZhengChengBin
# File    :test.py

import re

def main():
    str='<h3 align="center">Popularity in 1990</h3>\n<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>\n<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>'
    match = re.match(r'<h3\s*align="center">Popularity\s*in\s*(\S+)</h3>', str)
    print(match.group(1))

if __name__ == '__main__':
    main()