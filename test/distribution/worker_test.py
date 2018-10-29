#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/28 15:35
# Author  :ZhengChengBin
# File    :worker_test.py

import time, Queue
from multiprocessing.managers import BaseManager, Process


class QueueManager(BaseManager):
    pass


def worker_test():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    server_addr = '127.0.0.1'
    print 'Connect to server %s...' % server_addr
    m = QueueManager(address=(server_addr, 5000), authkey='abc')
    connect(m,'m')


def connect(m, name):
    try:
        m.connect()
        task = m.get_task_queue()
        result = m.get_result_queue()
        for i in range(10):
            try:
                print 'try to get task...'
                n = task.get(block=True, timeout=1)
                print 'run task %d * %d...' % (n, n)
                r = '%d * %d = %d' % (n, n, n * n)
                time.sleep(1)
                result.put(r)
            except Queue.Empty:
                print 'task queue is empty.'
        print 'worker exit.'
    except Exception, e:
        print e
        print name + u' 连接中断'



if __name__ == '__main__':
    worker_test()
