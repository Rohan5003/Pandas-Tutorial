import pandas as pd
import numpy as np

data = {
    'Name': ['Ravi', 'Priya', 'Anil', 'Neha', None],
    'Age': [20, 21, np.nan, 20, 19],
    'Marks': [85, np.nan, 78, 88, 92]
}

df = pd.DataFrame(data)
print(df)

# print(df.isna())

# print(df.dropna())

# df_filled = df.fillna(0)
# print(df_filled)

# mean_marks = df['Marks'].mean()
# df['Marks'].fillna(mean_marks, inplace=True)
# print(df)

# df['Age'].fillna(df['Age'].mean(), inplace=True)
# df['Age'] = df['Age'].astype(int)
# print(df)

# df.loc[5] = ['Ravi', 20, 85.00]
# print(df)


# print(df.duplicated())

# print(df.duplicated(subset='Name'))

# print(df.duplicated(subset=['Name', 'Marks']))

# print(df.duplicated(subset='Name', keep='last'))

# print(df.duplicated(subset='Name', keep=False))

# df_unique_names = df.drop_duplicates(subset='Name', keep='first')
# print(df_unique_names)


# df.drop_duplicates(inplace=True)
# print(df)

# df.rename(columns={'Name': 'Student Name'}, inplace=True)
# print(df)


# df['Marks'].replace(85.00, 100, inplace=True)
# print(df)


# df['Student Name'] = df['Student Name'].map({'Ravi': 1, 'Priya': 2, 'Anil': 3, 'Neha': 4})
# print(df)

# df['Marks'] = df['Marks'].apply(lambda x: x + 10)
# print(df)

# # you can also use function inplace of lambda 
# def add_bonus(x):
#     return x + 10

# df['Marks'] = df['Marks'].apply(add_bonus)
#  # or use numpy
# import numpy as np
# df['Marks'] = np.add(df['Marks'], 10)


# #--conditionally add marks
# # df.loc[df['Name'] == 'Priya', 'Marks'] += 10
# print(df)

# df.loc[3, 'Marks'] += 5
# print(df)

# df.loc[df['Age'] == 20, 'Marks'] += 2
# print(df)

# # df.loc[(df['Name'] == 'Anil') & (df['Age'] == 20), 'Marks'] += 5
# print(df)

# df.iloc[0, 2] += 3  # Add 3 marks to first row (Ravi)
# print(df)

