#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/3 14:03
# Author  :ZhengChengBin
# File    :finger_num_test.py

import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics


"""
----------------------------
重点注意
----------------------------
plt.imshow(image, cmap='gray_r')
digits.images.reshape((n_samples, -1))
classifier = svm.SVC(gamma=0.001)
metrics.classification_report(expected, predicted) #结果： precision(正样本识别率)    recall（负样本识别率）  f1-score（综合评分）   support（样本数）
metrics.confusion_matrix(expected, predicted)
----------------------------
改进：最好能显示出分错类的具体数据内容？
------------------------------
"""

digits = datasets.load_digits()  # 手写数字数据集
# print (digits.data)
# print(digits.images[0])
# print dir(digits)
# print (digits.target_names[0])
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    # plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap='gray_r')  # 画灰度图
    plt.title('Training: %i' % label)
    # plt.show()

n_samples = len(digits.images)

print digits.images[0]
data = digits.images.reshape((n_samples, -1))  # 重塑形状（总数据/n_samples） n行，列数未知标记为-1 ,把一副图的数据（二维列表）放在一维列表中
print(data[0])

classifier = svm.SVC(gamma=0.001)  # 计算函数
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])  # 训练

predicted = classifier.predict(data[n_samples // 2:])  # 预测
expected = digits.target[n_samples // 2:]  # 预测数据原本的标记

print('classsification report for classifier %s:\n%s\n'
      % (classifier, metrics.classification_report(expected, predicted)))  # metrics评价工具
print ('confusion matrix:\n%s' % metrics.confusion_matrix(expected, predicted))  # 混合矩阵，查看数据分错到哪个类

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))  # 只是为了画图
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.axis('off')
    plt.imshow(image, cmap='gray_r')
    plt.title('Prediction:%i' % prediction)
    # plt.show()
