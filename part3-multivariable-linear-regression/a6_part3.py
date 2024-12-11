import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size= .2) 

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places.
coef = np.around(model.coef_, 2)
intercept = np.around(float(model.intercept_), 2)
r_squared = np.around(model.score(x, y), 2)

predict = model.predict(xtest)
predict = np.around(predict, 2)
print("R Squared value: ", r_squared)

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")

for index in range(len(xtest)):
    miles = xtest[index]
    actual = ytest[index]
    predicted = predict[index]

    print("Age: ", float(miles[1]),"Mileage: ", float(miles[0]), " Predicted price: ", predicted," Actual price: ", actual)