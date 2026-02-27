#csv file---------

Name,Maths,Science,English
Sowjanya,85,78.0,90
Rahul,67,88.0,72
Anu,92,95.0,89
priya,9,8.0,0
Anu,92,95.0,89
Anu,92,95.0,80
priya,9,,0

#code-------

import pandas as pd
import numpy as np
data=pd.read_csv("data.csv")
#Identifies null
print(data.isnull())
#Drops null
print(data.dropna())
print(data.dropna(axis=1))
#fill null with zero
print(data.fillna(0))
#finds duplicate
print(data.duplicated())
#drop duplicates
print(data.drop_duplicates())
#particular subject is in int or not
data["Maths"] = data["Maths"].astype(int)
print(data["Maths"])
data["English"] = data["English"].fillna(0).astype(int)
print(data["English"])
#changing the csv file
df=data.to_csv("data.csv", index=False)
print(df)
