import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('./first_deploy/insurance.csv')

label = LabelEncoder()
label.fit(df['sex'])
df['Sex'] = label.transform(df['sex'])
label.fit(df['smoker'])
df['Smoker'] = label.transform(df['smoker'])
label.fit(df['region'])
df['Region'] = label.transform(df['region'])

#.....
x = df[['age', 'bmi','children', 'Sex', 'Smoker', 'Region']]
y = df['charges']

#...split data

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
#...training
linreg = LinearRegression()
linreg.fit(X_train, y_train)

predict_y = linreg.predict(X_test)
linreg.score(X_test, y_test)
file = open("expense_model.pkl", 'wb')
pickle.dump(linreg, file)