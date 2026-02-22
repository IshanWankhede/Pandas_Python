import pandas as pd

df = pd.read_csv("data.csv")

# Filtering = Keeping the rows tht match a condition

# tall_pokemon = df[df["Height"] >= 2]
tall_pokemon = df[df["Weight"] >= 2]

# tall_pokemon = df["Height"] >= 2  # returns a boolean value

# 0      False
# 1      False
# 2       True
# 3      False
# 4      False
#        ...  
# 145     True
# 146    False
# 147     True
# 148     True
# 149     True
# Name: Height, Length: 150, dtype: bool

print(tall_pokemon)  

# • df["Height"] >= 2
# → This creates a Boolean Series (True/False for each row).
# • df[..]
# → When you pass that Boolean Series inside df[..], Pandas performs Boolean indexing and returns only the rows where the condition is True.
# • Result type
# The result is still a DataFrame, not a NumPy array.
# For your dataset, it will return Venusaur (Height = 2) and any Pokémon taller than 2.


legendary_pokemon = df[df["Legendary"] == 1]

print(legendary_pokemon)