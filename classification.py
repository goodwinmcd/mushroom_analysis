import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

mushrooms = pd.read_csv(os.environ['mushroom_data'])

def treat_data(data_feature):
    number = LabelEncoder()
    data_feature = number.fit_transform(data_feature.astype('str'))
    return data_feature

def treat_all_data(data):
    for column in data.columns:
        data[column] = treat_data(data[column])
    return data

def fit_data(model_array, x_data, y_data):
    for model in model_array:
        model_array[model].fit(x_data, y_data)

def print_accuracy(model_array, x_test_data, y_test_data):
    for model in model_array:
        accuracy = model_array[model].score(x_test_data, y_test_data)
        print('Accuracy of {}: {}'.format(model, accuracy))

mushrooms = treat_all_data(mushrooms)
x_data = mushrooms.drop(columns=['class'])
y_data = mushrooms['class']

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=.2)

models = {'Logistic Regression': LogisticRegression(), 
          'Gaussian naive bayes': GaussianNB(), 
          'Support vector machine': SVC(), 
          'Decision tree classifier': DecisionTreeClassifier(), 
          'Random Forest Classifier': RandomForestClassifier(), 
          'Neural Network MLP': MLPClassifier()
          }
fit_data(models, x_train, y_train)
print_accuracy(models, x_test, y_test)


