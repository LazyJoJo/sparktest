#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/28 15:23
# Author  :ZhengChengBin
# File    :manager_test.py

import random, time, Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()  # 这里是队列类型，和multiprocessing.Queue不一样,但是效果相同


# 控制多台机子之间的网络通信
class QueueManager(BaseManager):
    pass


# 提供返回变量的方法 不能用lambda 传给callable，会报错
def fun_task_queue():
    global task_queue
    return task_queue


def fun_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':  # 必须要放在main中，放在子进程中会报错

    # 注册接口
    QueueManager.register('get_task_queue', callable=fun_task_queue)  # 传入的是方程，不是值，加（）才变成值
    QueueManager.register('get_result_queue', callable=fun_result_queue)

    manager = QueueManager(address=('127.0.0.1', 5000), authkey='abc')
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 注意这里是两个队列 ，所以一开始result是没有值的，单独运行会报错，需要运行worker_test
    for i in range(10):
        n = random.randint(0, 10000)
        print 'Put task %d...' % n
        task.put(n)

    print 'Try get results...'
    try:
        for i in range(10):
            r = result.get(block=True, timeout=10)
            print ('Result: %s' % r)
    except Queue.Empty:
        print 'result queue is empty.'

    manager.shutdown()
