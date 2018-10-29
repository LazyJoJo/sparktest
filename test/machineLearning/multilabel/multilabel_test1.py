#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/3 19:49
# Author  :ZhengChengBin
# File    :multilabel_test1.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
from sklearn.preprocessing import LabelBinarizer
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA


def plot_hyperplane(clf, min_x, max_x, linestyle, label):
    w = clf.coef_[0]


def plot_subfigure(X, Y, subplot, title, transform):
    if transform == 'pca':
        X = PCA(n_components=2).fit_tansform(X)
    elif transform == 'cca':
        X = CCA(n_components=2).fit(X, Y).transform(X)
    else:
        raise ValueError

    min_x = np.min(X[:, 0])
    max_x = np.max(X[:, 0])

    min_y = np.min(X[:,1])
    max_y = np.max(X[:,1])



plt.figure(figsize=(8, 6))
X, Y = datasets.make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=True, random_state=1)
plot_subfigure(X, Y, 1, 'With unlabeled samples + CCA', 'cca')
plot_subfigure(X, Y, 2, 'With unlabeled samples + PCA', 'pca')
X, Y = datasets.make_multilabel_classification(
    n_classes=2, n_labels=1, allow_unlabeled=False, random_state=1)
plot_subfigure(X, Y, 3, "Without unlabeled samples + CCA", "cca")
plot_subfigure(X, Y, 4, "Without unlabeled samples + PCA", "pca")

plt.subplots_adjust(.04, .02)
