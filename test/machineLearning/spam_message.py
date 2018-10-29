#!/usr/bin/env python
# -*- coding:utf8 -*-
# TIME    :2018/7/2 16:04
# Author  :ZhengChengBin
# File    :spam_message.py

import matplotlib.pyplot as plt
import csv
from textblob import TextBlob
import pandas
import numpy as np
import sklearn  # 需要pip install scipy
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold, cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.learning_curve import learning_curve

messages = [line.rstrip() for line in open('C:\Users\zcb\Desktop\smsspamcollection\SMSSpamCollection')]

print len(messages)

for message_no, message in enumerate(messages[:10]):
    print message_no, message

pandas.set_option('max_columns', 10)
messages = pandas.read_csv('C:\Users\zcb\Desktop\smsspamcollection\SMSSpamCollection',
                           sep='\t', quoting=csv.QUOTE_NONE, names=['label', 'message'])
print messages

print messages.groupby('label').describe()

messages['length'] = messages['message'].map(lambda text: len(text))
print messages.head()
messages.length.plot(bins=100, kind='hist')  # bins分成几个类(等分) kind图形类别
plt.show()
print messages.length.describe()

print list(messages.message[messages.length > 900])  # 这里的message是一个方法，内部放判断式

messages.hist(column='length', by='label', bins=50)  # 分类画出
plt.show()


def split_into_tokens(message):
    message = unicode(message, 'utf8').lower()
    words = TextBlob(message).words
    return [word.lemma for word in words]

print messages.message.head().apply(split_into_tokens)

bow_transformer = CountVectorizer(analyzer=split_into_tokens).fit(messages['message'])
print len(bow_transformer.vocabulary_)





