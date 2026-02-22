import pandas as pd 

#Data Cleaning is = the process of fixing/removing:
#                   incomplete, incorrect, or irrelevent data.   
#                   ~75% of the work is done with pandas is data cleaning

df = pd.read_csv("data.csv")

# 1. Drop irrelevent columns 
df = df.drop(columns = ["Legendary", "No"])

print(df)

# 2. Handle missing data : like if a rows is missing a row then we are going to drop down tht full row
# df = df.dropna(subset=["Type2"])

df = df.fillna({"Type2":"None"})

print(df)