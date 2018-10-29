#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/28 9:12
# Author  :ZhengChengBin
# File    :os_test.py

# 在window下无法运行fork模块，在Linux才可以运行
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求
# os 本身就是一个进程
import os
from multiprocessing import Process


def fork_test():
    print 'Process (%s) start...' % os.getpid()
    pid = os.fork()  # 创建子进程
    if pid == 0:
        print 'I am child process %s and my parent is %s.' % (os.getpid(), os.getppid())
    else:
        print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)


# 这个在windows下是可以运行的  单个线程
def process_test():
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'


# process_test测试时使用的方法
def run_proc(name):
    print 'Run child process %s (%s)' % (name, os.getpid())


from multiprocessing import Pool
import time, random


# 线程池
def pool_test():
    print 'Parent process %s.' % os.getpid()
    p = Pool()  # 正常是只运行4个进程，CPU只有四个核时
    # p = Pool(5) 要开启5个需要这样定义

    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    p.map(long_time_task, range(5))  # map可以使用，apply_async无法使用
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'


# pool_test 测试时使用的方法
def long_time_task(name):
    # 子进程内部拿不到父进程的id
    print 'Run task %s (%s)' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 10)  # [0,1)随机数*10
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


from multiprocessing import Process, Queue


def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        value = q.get(True)  # get(self, block=True, timeout=None)
        print 'get %s from queue.' % value


def queue_test():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


if __name__ == '__main__':
    # process_test()
    # pool_test()
    queue_test()
