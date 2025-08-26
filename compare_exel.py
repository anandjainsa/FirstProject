import pandas as pd

# Input file paths
file1 = "file1.xlsx"
file2 = "file2.xlsx"

# Column name to compare (example: "ID")
compare_column = "ID"

# Read the Excel files
df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Find matches (inner join on compare_column)
matches = pd.merge(df1, df2, on=compare_column, how="inner")

# Find non-matching (in df1 but not in df2)
only_in_file1 = df1[~df1[compare_column].isin(df2[compare_column])]

# Find non-matching (in df2 but not in df1)
only_in_file2 = df2[~df2[compare_column].isin(df1[compare_column])]

# Save to a new Excel file with multiple sheets
output_file = "comparison_output.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    matches.to_excel(writer, sheet_name="Matches", index=False)
    only_in_file1.to_excel(writer, sheet_name="Only_in_File1", index=False)
    only_in_file2.to_excel(writer, sheet_name="Only_in_File2", index=False)

print(f"✅ Comparison done. Output saved to {output_file}")
