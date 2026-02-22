import pandas as pd

# aggregate function = Reduces a set of values in single summary value 
#                      used to summarize and analyze data 
#                      often used with groupby() function 

df = pd.read_csv("data.csv")

print(df.mean(numeric_only=True))   # we are telling pandas tht find the mean of the columns which has numerical values only

# No           75.500000
# Height        1.200000
# Weight       46.231333
# Legendary     0.026667
# dtype: float64

print(df.sum(numeric_only=True))

# No           11325.0
# Height         180.0
# Weight        6934.7
# Legendary        4.0
# dtype: float64

print(df.min(numeric_only=True))

# No           1.0
# Height       0.2
# Weight       0.1
# Legendary    0.0
# dtype: float64

print(df.max(numeric_only=True))

# No           150.0
# Height         8.8
# Weight       460.0
# Legendary      1.0
# dtype: float64

print(df.count())  #calculates the value of each column 
 
# No           150
# Name         150
# Type1        150
# Type2         67
# Height       150
# Weight       150
# Legendary    150
# dtype: int64

# Whole dataframe
# print(df.mean(numeric_only=True))   # Calculates the mean of all numeric columns
# print(df.sum(numeric_only=True))    # Calculates the sum of all numeric columns
# print(df.min(numeric_only=True))    # Finds the minimum value in each numeric column
# print(df.max(numeric_only=True))    # Finds the maximum value in each numeric column
# print(df.count())                   # Counts non-null values in each column

#Single column
# Single column
# print(df["Height"].mean())   # Average of all values in the "Height" column
# print(df["Height"].sum())    # Sum of all values in the "Height" column
# print(df["Height"].min())    # Smallest value in the "Height" column
# print(df["Height"].max())    # Largest value in the "Height" column
# print(df["Height"].count())   # Number of non-null entries in the "Height" column

group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())

