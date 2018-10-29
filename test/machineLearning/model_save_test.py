#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/3 19:06
# Author  :ZhengChengBin
# File    :model_save_test.py

from sklearn import svm, datasets

clf = svm.SVC()
iris = datasets.load_iris()
data, target = iris.data, iris.target
clf.fit(data, target)

import pickle  # 不能存文件

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(data[:1])

from sklearn.externals import joblib  # 可以保存在本地

joblib.dump(clf, 'C:\Users\zcb\Desktop\\test.pkl')
clf2 = joblib.load('C:\Users\zcb\Desktop\\test.pkl')
print(clf2.predict(data[:1]))
