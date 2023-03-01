import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("iris.csv")
print(data)

x=data["spl"]
y=data["swl"]

plt.scatter(x,y,c="red")

plt.xlabel("spl")
plt.ylabel("swl")
plt.title("Irise")
plt.show()

