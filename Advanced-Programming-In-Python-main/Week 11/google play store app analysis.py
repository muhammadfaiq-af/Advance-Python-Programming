import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("googleplaystore.csv")

# Question 1
x = df['Category'].value_counts()
print(x)

drop = df.dropna()

#Question 5
y = df['Type'].value_counts()
print("Free Apps are" , y['Free'])

#Question 4
a = df["Rating"].unique()
print(a)
b = df["Installs"].unique()
print(b)

#Question 2
e = df.groupby('Category')['Content Rating'].value_counts()
print(e)

#Question 6
df['Price'] = df.Price.str.replace("$","").astype(float)
print(df[(df['Price'] == df.Price.max())])

#Question 3
df['Installs'] = df.Installs.str.replace("," , "")
df['Installs'] = df.Installs.str.replace("+" , "")
df['Installs'] = df.Installs.str.replace("Free" , "")
df['Installs'] = df.Installs.astype(float)
print(df[(df['Rating'] > 4.0) & (df['Installs'] == df.Installs.max())])