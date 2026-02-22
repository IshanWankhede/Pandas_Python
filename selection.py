import pandas as pd 

# df = pd.read_csv("data.csv") 

# here we can do like this too

df = pd.read_csv("data.csv", index_col="Name")   

# selection by column 

print(df["Name"].to_string())  # series 
print(df["Height"].to_string())
print(df["Weight"].to_string())

print(df[["Name", "Height", "Weight"]])

# Selection by Rows

# print(df.loc[0])  

#  when you do .loc[]  or .iloc[] , the result is a Series, not a DataFrame.

# No             1
# Name     Bulbasaur
# Type1       Grass
# Type2      Poison
# Height        0.7
# Weight        6.9
# Legendary       0
# Name: 0, dtype: object


print(df.loc["Pikachu"])