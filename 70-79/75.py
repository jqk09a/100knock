# -*- coding: utf-8 -*-
"""test"""

import sys
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, precision_recall_curve

from matplotlib import pyplot as plt
import seaborn

#dataを1次元配列として渡すのver0.17から廃止?でver0.19だとエラー? ->...うるさいからさよなら
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


X = np.array([[1,0,0,0],[0,0,8,0],[6,5,4,3],[1,1,2,1],[9,3,2,0],[1,4,9,1]])
y = ['+1','-2','+1','-2','+1','-2']
t = [3,5,7,9]
t2 = [0,1,0,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

t_model = LogisticRegression().fit(X_train,y_train)
y_pre = t_model.predict(X_test)
y_pro = t_model.predict_proba(X_test)

print y_pre
print y_pro[:, 0]

precision, recall, thresholds = precision_recall_curve(y_test, y_pro[:, 0], pos_label='+1')

print precision, recall, thresholds

# output
plt.plot(recall, precision)
plt.xlabel('recall')
plt.ylabel('precision')
plt.title('precision_recall curve')
plt.show()
