#csv file-----
Name,Maths,Science,English
Sowjanya,85,78,90
Rahul,67,88,72
Anu,92,95,89

#code----
import pandas as pd
data=pd.read_csv("data.csv")
print(data["Maths"])

print(data[["Maths", "Science"]])

print (data[(data["Maths"]>80) & (data["Science"]>70) ])
subjects=["Maths","Science","English"]
print(data[(data[subjects] > 90).all(axis=1)])

#who got above 80 if there is large data set
print(data[(data.select_dtypes(include="number") > 80).all(axis=1)])

#who got greater tha  or equal to 90
print(data[(data.select_dtypes(include="number") >= 90).all(axis=1)])
