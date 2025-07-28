import pandas as pd
import numpy as np
#---1d labelled array----(column in excell)----series
# data1 = [10, 20, 30, 40]
# s = pd.Series(data1)
# print(s)

# #---2d labelled array-----dataframe is like a excell with row and column
# data2 = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
# df1 = pd.DataFrame(data2)
# print(df1)

#-----craeting dataframes from different sources---
# #------from lists----
# data3 = [[1, 'A'], [2, 'B']]
# df2 = pd.DataFrame(data3, columns=['ID', 'Letter'])
# print(df2)

# #----------from dictionary-------
# data4 = {'Name': ['Tom', 'Jerry'], 'Score': [90, 95]}
# df3 = pd.DataFrame(data4)
# print(df3)

# #-----from numpy array------
# arr = np.array([[1, 2], [3, 4]])
# df4 = pd.DataFrame(arr, columns=['Col1', 'Col2'])
# print(df4)

#----------question------------
# You are given student data. Your goal is to:
# Create a DataFrame
# Print the first 3 rows
# Check the shape of the DataFrame
# Show column data types
# Display summary statistics
# Access Priya’s marks using .loc[]
# Access Anil’s age using .iloc[]

data = {
    'Name': ['Ravi', 'Priya', 'Anil', 'Neha', 'Sara'],
    'Age': [20, 21, 22, 20, 19],
    'Marks': [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)
print(df)
# print(df.loc[0:2])  or
print((df.head(3)))

print(df.shape)
print(df.dtypes)
print(df.describe())  # shows summary statistics
print(df.loc[1,'Marks'])
print(df.iloc[2,1])

print(df.tail(2))          # Last 2 students
print(df.at[0, 'Name'])    # Fast way to get Ravi’s name
print(df.iat[4, 2])        # Fast way to get Sara’s marks





