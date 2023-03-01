import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("b.csv")
print(data)
x=data["sqft_living"]
y=data.price

print(x)
print(y)

plt.scatter(x,y)
plt.xlabel("bhk")
plt.ylabel("price")
plt.show()



from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
print(xtest)
print(xtrain)

print(ytest)
print(ytrain)

lr=LinearRegression
lr.fit(xtrain,ytrain)

print(lr.intercept_)
print(lr.coef_)

print(lr.predict[[1000]])

ypred=lr.predict(xtest)
cm=mean_absolute_error(ytest,ypred)
print(cm)