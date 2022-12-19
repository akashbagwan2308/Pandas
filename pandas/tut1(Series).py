# panda ---> panel data
#  single dimensional data structure ---> Series Object
#  multi dimensional data structure ---> Data-frame

# Series Object is one dimensional labelled array

import pandas as pd
s1 = pd.Series([1,2,3,4,5])
print(s1)
print(type(s1))

# we can change the index also
s2 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s2)

# series of dictionary given
dict  = {'a':15,'b':78,'c':54}
ser = pd.Series(dict)
print(ser)
# we can change the index position also
dict1  = {'a':15,'b':78,'c':54}
ser1 = pd.Series(dict1,index=['b','c','d','a'])
print(ser1)
# Extracting series object
S1 = pd.Series([1,2,3,4,5,6,7,8,9])
print(S1[4])   # extracting element from index
print(S1[:4])   # extracting element from starting
print(S1[-3:])   # extracting element from ending

# Adding scalar values to the series element
Ser = pd.Series([2,5,7,9,45,5,49,36,2])
print(Ser+15)  # adding scalar value 15 to the series
print(Ser+S1)  # adding one series to the other series
print(Ser*15)  # multiply scalar value 15 to the series
print(Ser*S1)  # multiply one series to the other series
print(Ser/15)  # divide scalar value 15 to the series
print(Ser/S1)  # divide one series to the other series
