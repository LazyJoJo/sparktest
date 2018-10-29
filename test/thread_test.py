#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/28 11:14
# Author  :ZhengChengBin
# File    :thread_test.py


# 线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
import time, threading


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name


def thread_test():
    print 'thread %s is running...' % threading.current_thread().name
    t = threading.Thread(target=loop, name='LoopThread')  # 单个线程
    t.start()
    t.join()
    print 'thread %s ended.' % threading.current_thread().name


# ----------测试线程锁-------------------

balance = 0
lock = threading.Lock()

# 保证最终balance为 0
def change_it(n):
    global balance  # 方法内部获得全局变量  只有全局变量有必要加锁
    balance = balance + n
    balance = balance - n


# 注意死锁问题
def run_thread(n):
    for i in range(100000):
        lock.acquire()  # 这段运行添加锁
        try:
            change_it(n)
        finally:
            lock.release()  # 释放锁


def lock_test():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print balance


if __name__ == '__main__':
    # thread_test()
    lock_test()
