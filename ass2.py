import numpy as np
import pandas as pd


data=pd.read_csv("iris.csv")
x=data["spl"]
y=data["swl"]
print(data)
print(x,y)
x1=data.dropna(axis=0,how="any")
print(x1)


