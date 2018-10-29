#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/28 14:00
# Author  :ZhengChengBin
# File    :thread_local_test.py

# 线程局部变量读写

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()  # 这个是全局变量，但是他的属性都是局部变量


def process_student():
    student = local_school.student  # 每个线程使用的变量都是不一样的，都是局部变量
    print 'Hello, %s (in %s)' % (student, threading.current_thread().name)


def process_thread(name):
    # 绑定ThreadLocal的student,这里相当于创建了一个新的变量
    local_school.student = name
    process_student()


def thread_local_test():
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    thread_local_test()
