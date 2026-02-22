# pip install ydata_profiling

import pandas as pd 

from ydata_profiling import ProfileReport

# 1. Load your dataset into a pandas DataFrame
df = pd.read_csv("housing.csv")

# 2. Generate the profile report
profile = ProfileReport(df, title="My Data Report")

# 3. Save it as an interactive HTML file
profile.to_file("report.html")