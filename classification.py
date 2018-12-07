import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.naive_bayes import GaussianNB


mushrooms = pd.read_csv(os.environ['mushroom_data'])

def treat_data(data_feature):
    number = LabelEncoder()
    data_feature = number.fit_transform(data_feature.astype('str'))
    return data_feature

def treat_all_data(data):
    for column in data.columns:
        data[column] = treat_data(data[column])
    return data

mushrooms = treat_all_data(mushrooms)
x_data = mushrooms.drop(columns=['class'])
y_data = mushrooms['class']

print(mushrooms.corr())

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=.2)

lg = LogisticRegression()
gnb = GaussianNB()

lg.fit(x_train, y_train)
gnb.fit(x_train, y_train)
lg_accuracy = lg.score(x_test, y_test)
gnb_accuracy = gnb.score(x_test, y_test)
print('Accuracy of logistic regression: {}'.format(lg_accuracy))
print('Accuracy of gausian naive bayes regression: {}'.format(gnb_accuracy))
