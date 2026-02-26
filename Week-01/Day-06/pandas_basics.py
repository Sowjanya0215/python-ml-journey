import pandas as pd 
   
df = pd.DataFrame() 
print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
df = pd.DataFrame(lst) 
print(df)

#Loading data

df = pd.read_csv("data.csv")
print(df.head())
print(df.info())

#Handling mising data

print(df.isnull().sum())
df = df.fillna(0)

#filtering Data

ages = df[df['age'] > 25]
print(ages)
