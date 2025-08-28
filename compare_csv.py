import pandas as pd

# File paths
file1 = "file1.csv"
file2 = "file2.csv"
output_file = "non_matched.csv"

# Column name to compare
key_column = "id"   # change this to the column you want to compare

# Read both CSVs
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Find non-matching rows
non_matching = pd.concat([
    df1[~df1[key_column].isin(df2[key_column])],  # rows in df1 not in df2
    df2[~df2[key_column].isin(df1[key_column])]   # rows in df2 not in df1
])

# Save to new CSV
non_matching.to_csv(output_file, index=False)

print(f"✅ Non-matching rows saved to {output_file}")
