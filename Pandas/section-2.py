import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Ravi', 'Priya', 'Anil', 'Neha', 'Sara'],
    'Age': [20, 21, 22, 20, 19],
    'Marks': [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)
print(df)

# df['Name']

# df[['Name', 'Marks']]

# df.loc[2]
# df.iloc[2]

# df[df['Age'] > 20]

# df[(df['Age'] > 20) & (df['Marks'] > 80)]

#---Use .isin() to filter rows that match values from a list.
c = df[df['Name'].isin(['Ravi', 'Neha'])]
print(c)

# #-----Use it for range filtering.
# df[df['Marks'].between(80, 90)]

# #------Use natural language-style filtering
# df.query('Age > 20 and Marks > 80')

# df.loc[df['Name'] == 'Ravi', 'Marks'] = 95
# print(df)


