#################################################################### to save for future use ##############################################
import joblib

model = joblib.load('salary1.pk1')

yrsExp = float(input("Enter  Experience : "))

prediction = model.predict([[yrsExp]])

print("Your Salary as per dataset would be : ", prediction)


