import pandas as pd
import numpy as np

data=pd.read_csv("z.csv")

print(data)

x=data.iloc[:,[2,4]].values
print(x)
y=data.iloc[:,4].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.05)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
xtrain=sc.fit_transform(xtrain)
xtest=sc.fit_transform(xtest)

from sklearn.naive_bayes import GaussianNB
gb=GaussianNB()
gb.fit(xtrain,ytrain)
ypred=gb.predict(xtest)

print(xtest)
print(ypred)

from sklearn.metrics import confusion_matrix

cm=confusion_matrix(ytest,ypred)
print(cm)
