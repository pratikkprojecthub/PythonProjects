import pandas
import numpy
from sklearn.linear_model import LinearRegression


ds = pandas.read_csv('Salary_Data.csv')
x = ds['YearsExperience'].values.reshape(30, 1)
y = ds['Salary']
model = LinearRegression()
model.fit(x, y)
model.predict([[ 8.1 ]])

import joblib
joblib.dump(model, 'salary1.pk1')



