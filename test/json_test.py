#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/6/27 14:00
# Author  :ZhengChengBin
# File    :json_test.py

import json

d = dict(name='dfd', age=20, score=80)
js = json.dumps(d)  # 转成json类型
print js
d2 = json.loads(js)  # json 默认编码格式是utf-8，转回来都带u''
print d2


class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'score': self.score
        }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


# 转入方法在Student内部，转出方法是整个外部，所以引用时也不一样，可以都写到外面来
s = Student('bob', 20, 90)
print json.dumps(s, default=lambda obj: obj.student2dict())  # 提供转换函数
js = json.dumps(s, default=lambda obj: obj.__dict__)  # 每个对象都有一个转换成dict的方法

s = json.loads(js, object_hook=dict2student)  # 需要另外提供转换方法

# 平时应该不常用下面的方法，因为有多个对象时可能报错
f = open('C:\Users\zcb\Desktop\dump.txt', 'w')
json.dump(s, f, default=lambda obj: obj.__dict__)
f.close()

f = open('C:\Users\zcb\Desktop\dump.txt', 'r')
print json.load(f, object_hook=dict2student)  # 这个方法（dict2student）只能实例化一个对象，如果文件中有多个对象则报错
f.close()

