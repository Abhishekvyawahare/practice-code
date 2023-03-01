import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("b.csv")
print(data)

x=data[["sqft_living"]]
y=data.price

print(x)
print(y)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
print(xtrain)
print(ytrain)
print(xtest)
print(ytest)

lr=LinearRegression()
lr.fit(xtrain,ytrain)

print(lr.coef_)
print(lr.intercept_)



ypred=lr.predict(xtest)
cm=mean_absolute_error(ytest,ypred)
print(cm)