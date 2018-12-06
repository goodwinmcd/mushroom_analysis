import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np

mushrooms = pd.read_csv('/home/goodwin/Documents/Projects/mushroom_analysis/mushrooms.csv')

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

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=.2)

lg = LogisticRegression()
lg.fit(x_train, y_train)
accuracy = lg.score(x_test, y_test)
print('Accuracy of logistic regression: {}'.format(accuracy))
