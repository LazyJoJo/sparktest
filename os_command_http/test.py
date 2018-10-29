#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/10/16 19:51
# Author  :ZhengChengBin
# File    :test.py

import os
import urllib.request as ur
import urllib.parse as up


def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print (os.path.join(dir, filename)) # dir/foo.txt (relative to current dir)
    print (os.path.abspath(os.path.join(dir, filename))) # /home/nick/dir/foo.txt


def wget2(url):
    res = ur.urlopen(url)
    print(res.getheader('Content-Type'))


    data = bytes(up.urlencode({'word': 'hello'}), encoding='utf8')
    res = ur.urlopen('http://httpbin.org/post', data=data)
    print(res.read())


def main():
    # dir = "C:\\Users\zcb\Desktop"
    # printdir(dir)
    # wget2('https://httpbin.org/get')
    dest_dir = 'C:\\Users\\zcb\\Desktop\\google-python-exercises\\logpuzzle\\ans'
    x = 2
    with open(os.path.join(dest_dir,'index.html'),'w') as f:
        str = '<html><body>\n'
        for i in range(x):
              str += '<img src="img%s.jpg">' % i
        str+='\n</body></html>'
        f.write(str)


if __name__ == '__main__':
    main()