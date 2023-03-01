import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

data=pd.read_csv("z.csv")

print(data)

x=data.iloc[:,[3,4]].values
print(x)


den=sch.dendrogram(sch.linkage(x,method="ward"))
plt.title("dendogram")
plt.show()


from sklearn.cluster import AgglomerativeClustering
ag=AgglomerativeClustering(n_clusters=3)

ypred=ag.fit_predict(x)
plt.scatter(x[ypred==0,0],x[ypred==0,1],s=100,c="red")
plt.scatter(x[ypred==1,0],x[ypred==1,1],s=100,c="blue")
plt.scatter(x[ypred==2,0],x[ypred==2,1],s=100,c="green")
plt.show()