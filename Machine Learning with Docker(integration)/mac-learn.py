import pandas
import numpy
from sklearn.linear_model import LinearRegression


ds = pandas.read_csv('Salary_Data.csv')
x = ds['YearsExperience'].values.reshape(30, 1)
y = ds['Salary']
model = LinearRegression()
model.fit(x, y)
model.predict([[ 8.1 ]])

# for saving the model for future use we use joblib library
# importing the package to save the model...
import joblib
joblib.dump(model, 'salary1.pk1')
