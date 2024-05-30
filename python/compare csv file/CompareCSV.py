import pandas as pd

blank_data = "C:/Users/przns/Downloads/Blank Data.csv"
nonblank_data = "C:/Users/przns/Downloads/NON BLANK.csv"

df1 = pd.read_csv(blank_data)
df2 = pd.read_csv(nonblank_data)

columns_to_compare = [col for col in df1.columns if col != 'last_action']

difference = df1[columns_to_compare].compare(df2[columns_to_compare])

# Iterate through differences and pinpoint location
for (col, row), value in difference.items():  # Replace .stack().iteritems() with .items()
    if value != False:
        print(f"Difference in row {row + 1}, column '{col}'")
