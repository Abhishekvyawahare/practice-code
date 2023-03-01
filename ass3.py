import pandas as pd
import numbers as np

data=pd.read_csv("a.csv")
x=data.iloc[:,0:1].values
print(data)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
x1=le.fit_transform(x)

print(x1)

from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder()
x2=ohe.fit_transform(x).toarray()
print(x2)



