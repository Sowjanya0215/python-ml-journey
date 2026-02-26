import pandas as pd

df = pd.read_csv("students.csv")
print(df)

#Head
print(df.head())

#Tail
print(df.tail())

#Info
print(df.info())

#Describe
print(df.describe())

#Shape
print(df.shape)
