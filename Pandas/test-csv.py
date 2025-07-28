import pandas as pd
dic = {"Name":['ravi','priya','meena'], "Age":[40,50,80], "Marks":[25,63,54]}
d = pd.DataFrame(dic)
print(d)
d.to_csv("test1.csv")

# df = pd.read_csv(r"C:\Users\dell\Downloads\test.csv")
# print(df)
# print(df.head())        # First 5 rows
# print(df.tail())        # Last 5 rows
# print(df.shape)         # (rows, columns)
# print(df.dtypes)        # Data types of each column
# print(df.describe())    # Summary for numbers

print(d.head())        # First 5 rows
print(d.tail())        # Last 5 rows
print(d.shape)         # (rows, columns)
print(d.dtypes)        # Data types of each column
print(d.describe())    # Summary for numbers

print(d.loc[0, 'Name'])   # Label-based: Ravi
print(d.iloc[1, 2])       # Index-based: 90 (Marks of Priya)
print(d.loc[1])           # All info for Priya




