import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data=pd.read_csv("z.csv")
x=data.iloc[:,[3,4]].values
print(data)
print(x)

wcss=[]
for i in range(1,5):
    km=KMeans(n_clusters=i)
    km.fit(x)
    wcss.append(km.inertia_)
    plt.plot(range(1,5),wcss)
    plt.show()

    km=KMeans(n_clusters=5)
ypred=km.fit_predict(x)

plt.scatter(x[ypred==0,0],x[ypred==0,1],s=100,c="red")
plt.scatter(x[ypred==1,0],x[ypred==1,1],s=100,c="blue")
plt.scatter(x[ypred==2,0],x[ypred==2,1],s=100,c="green")

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],s=300,c="yellow",label="centroid")
plt.show()
    