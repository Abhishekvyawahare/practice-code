import numpy as np
import pandas as pd

data=pd.read_csv("b.csv")
print(data)

x=data[["sqft_living","bathroom"]]
y=data["price"]

print(x,y)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

xtest,xtrain,ytest,ytrain=train_test_split(x,y,test_size=0.2)
print(xtest,xtrain,ytrain,ytest)

lr=LinearRegression
lr.fit(xtrain,ytrain)

print(lr.intercept_)
print(lr.coef_)
print(lr.predict([2570,3]))

ypred=lr.predict(xtest)
cm=mean_absolute_error(ytest,ypred)
print(cm)