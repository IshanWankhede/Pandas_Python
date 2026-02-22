import pandas as pd

# Series = A pandas 1-Dimensional labeled array that can hold any datatype
#          Think of it like a single column in a spreadsheet (1-Dimensional)

data = [100, 102, 104] #dtype = int64

# data = [100.1,101.2,103.4] #dtype = float64
# data = ["A", "B", "C"] #dtype = objects
# data = [True, False, True] #dtype = bool

series = pd.Series(data, index=["a", "b", "c"]) #the Series() part is calling the constructor of the Series class in Pandas.
# the index parameter defines labels for the elements in your Series.


print(series.loc["a"]) # this .loc returns the value at particular given label

# 0    100
# 1    102
# 2    104
# dtype: int64 

data = [100, 102, 104]

series = pd.Series(data, index = ["a", "b", "c"])

# series.loc["c"] = 200

print(series.iloc[0])  # .iloc[] is a integer location whic takes integeres or lets say index

# ================================================================================================ #

data = [100, 102, 104, 200, 202]

series = pd.Series(data, index = ["a", "b", "c", "d", "e"])

print(series[series >= 200])

# d    200
# e    202
# dtype: int64

# ================================================================================================= #

calories = {"Day1": 1750,
            "Day2": 2100,
            "Day3": 1700}

series = pd.Series(calories)

series.loc["Day2"] += 500

print(series) 

# Day1    1750
# Day2    2100
# Day3    1700
# dtype: int64