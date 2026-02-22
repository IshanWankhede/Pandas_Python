import pandas as pd 

# Dataframe = A tabular data structure with rows and columns. (2 Dimensional)
#            Similar to an excel spreadsheet

data = {"Name": ["Doremon", "Nobita", "Gian"],
        "Age": [30, 35, 90]
}

dataframe = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

print(dataframe)

#                Name  Age
# Employee 1  Doremon   30
# Employee 2   Nobita   35
# Employee 3     Gian   90

print(dataframe.loc["Employee 1"])

# Name    Doremon
# Age          30
# Name: Employee 1, dtype: object

# Add a New Column 

dataframe["Job"] = ["Robot", "Student", "Singer"]

print(dataframe)

#                Name  Age      Job
# Employee 1  Doremon   30    Robot
# Employee 2   Nobita   35  Student
# Employee 3     Gian   90   Singer

# Add a New Row

new_row = pd.DataFrame([{"Name":"ishan", "Age":28, "Job":"Engineer"}],
                       index = ["Employee 4"])

dataframe = pd.concat([dataframe, new_row])

print(dataframe)

# Add New Rows 
df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

df["Job"] = ["Robot", "Student", "Singer"]

new_rows = pd.DataFrame([{"Name":"ishan", "Age":18, "Job":"Web_Engineer"},
                         {"Name":"palak", "Age":18, "Job":"Software_Engineer"},
                         {"Name":"ansh", "Age":18, "Job":"BlockChain_Engineer"},
                         {"Name":"kaushal", "Age":18, "Job":"IOT_Engineer"}],
                         index = ["Employee 4", "Employee 5", "Employee 6", "Employee 7"])

df = pd.concat([df, new_rows])

print(df)


#                Name  Age                  Job
# Employee 1  Doremon   30                Robot
# Employee 2   Nobita   35              Student
# Employee 3     Gian   90               Singer
# Employee 4    ishan   18         Web_Engineer
# Employee 5    palak   18    Software_Engineer
# Employee 6     ansh   18  BlockChain_Engineer
# Employee 7  kaushal   18         IOT_Engineer