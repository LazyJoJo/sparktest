#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/10/17 14:47
# Author  :ZhengChengBin
# File    :urllib_test.py

# !/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.parse
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    basename = os.path.basename(filename)
    num = basename.index('_')+1
    host = basename[num:]
    # host = 'developers.google.com'
    with open(filename) as f:
        text = f.read()

    ans = {}
    result = []
    puzzles = re.findall(r'GET\s+(\S+puzzle\S+)\s+HTTP',text)
    if puzzles:
        for puzzle in puzzles:
            if puzzle not in ans.keys():
                ans[puzzle] = 1
                result.append('http://'+host+puzzle)
    result = sorted(result)
    print(len(result))
    return result



def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    for url in img_urls:
        print(url)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    x=0
    for url in img_urls:
        str = 'img%s.jpg' % x
        urllib.request.urlretrieve(url, os.path.join(dest_dir,str))
        x+=1
        print('img%s' % x)

    with open(os.path.join(dest_dir,'index.html'),'w') as f:
        str = '<html><body>\n'
        for i in range(x):
              str += '<img src="img%s.jpg">' % i
        str +='\n</body></html>'
        f.write(str)



def main():
    # args = sys.argv[1:]
    #
    # if not args:
    #     print('usage: [--todir dir] logfile ')
    #     sys.exit(1)
    #
    # todir = ''
    # if args[0] == '--todir':
    #     todir = args[1]
    #     del args[0:2]

    todir = 'C:\\Users\\zcb\\Desktop\\google-python-exercises\\logpuzzle\\ans'
    args = []
    args.append('C:\\Users\\zcb\\Desktop\\google-python-exercises\\logpuzzle\\place_code.google.com')
    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))



if __name__ == '__main__':
    main()
