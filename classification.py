import pandas as pd

mushrooms = pd.read_csv('C:\\Users\\mcdonago\\source\\repos\\mushroom_data\\mushroom_data\\mushrooms.csv')

x_data = mushrooms.drop(columns=['class'])
y_data = mushrooms['class']

