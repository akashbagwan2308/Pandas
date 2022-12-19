# Data frame ---> is a 2-D labelled data structure
#data frame comprises of rows and columns

import pandas as pd
dict = { 'Name': ['Bob','Alic','Sam'],'Marks':[99,85,56]}
df = pd.DataFrame(dict)
print('Data Frame 1 :\n',df)
# we can change the inndex also
df1 = pd.DataFrame(dict,index=['a','b','c'])
print('Data Farme 2 :\n',df1)

# Data Frame In built functions ----> haed(), tail(), shape(), decribe()
iris = pd.read_csv(r'C:\Users\Admin\Downloads\iris.csv')
print(iris.head())  # .head() will give first five data frame members
print(iris.tail())  # .tail() will give last five data frame members
print(iris.shape)  # .shape() will give dimension of data frame
print(iris.describe())  # .describe() will give all over quantity of data frame

# to extract particular data frame , we use  .iloc() and
exdf = iris.iloc[0:3,0:2]   # 0:3 ---> rows indices, 0:2 ---> column indices
print(exdf)
exdf1 = iris.loc[0:3,('sepal_length','petal_width')]
print(exdf1)
# to remove a particular column from data frame
rdf = iris.head().drop('sepal_length',axis=1)
print(rdf)
# to remove a particular row from data frame
rdf1 = iris.head().drop([1,3],axis=0)
print(rdf1)

# pandas function
print(iris.mean())
print(iris.median())
print(iris.min())
print(iris.max())
