#################################################################### to save for future use ##############################################
# Step 1: Installation of the package 
import joblib
# Step 2:
model = joblib.load('salary1.pk1')
# Step 3:
yrsExp = float(input("Enter  Experience : "))
# Step 4:
prediction = model.predict([[yrsExp]])
# Step 5:
print("Your Salary as per dataset would be : ", prediction)


