import pandas

df = pandas.read_csv('megaCoffee.csv')

# print(df)
print(df.shape) #(300,3) 행과 열
print(df.columns) #열의 이름
print(df.index)

print(df.describe())
print(df.sort_values(by='age'))
print(df.sort_values(by='name'))
