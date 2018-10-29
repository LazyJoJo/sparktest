#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/10/17 10:49
# Author  :ZhengChengBin
# File    :copyspecial.py

# !/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them

def get_path_file(filepath):
    results =[]
    paths = os.listdir(filepath)
    for file in paths:
        match = re.search(r'__\w+__',file)
        if match:
            # print(os.path.abspath(file))  # 没指名前缀的话，默认是命令行中当前目录的前缀
            results.append(os.path.abspath(os.path.join(filepath,file)))
    return results


def savedir(path, todir):

    if not os.path.exists(todir):
        os.makedirs(todir)  # 创建多级目录 mkdir()只会创建一级目录
    for file in path:
        shutil.copy(file, todir)  # 前一个为 文件路径，后一个为 文件夹路径 或 文件路径

def savezip(path, tozip):
    cmd = 'zip -j ' + tozip+' '+' '.join(path)
    # cmd = 'zip'
    (status,output) = subprocess.getstatusoutput(cmd)  # 返回状态码和命令结果
    if status:  # 正常结果为0
        sys.stderr.write(output)
        sys.exit(1)
    # if not os.path.exists(tozip):
    #     os.makedirs(tozip)






def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print ("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    paths = []
    for filepath in args:
        get_paths = get_path_file(filepath)
        if get_paths:
            paths.extend(get_paths)

    if todir:
        savedir(paths,todir)
    elif tozip:
        savezip(paths,tozip)
    else:
        print("error")

if __name__ == "__main__":
    main()
