import pandas as pd

# --- Config ---
file1 = "file1.csv"   # can be .csv or .xlsx
file2 = "file2.csv"   # can be .csv or .xlsx
output_file = "comparison_output.xlsx"
key_column = "ID"     # column name to match on (must exist in both files)

# --- Load files ---
if file1.endswith(".csv"):
    df1 = pd.read_csv(file1)
else:
    df1 = pd.read_excel(file1)

if file2.endswith(".csv"):
    df2 = pd.read_csv(file2)
else:
    df2 = pd.read_excel(file2)

# --- Compare ---
# Inner join -> matching rows
matching = pd.merge(df1, df2, on=key_column, how="inner")

# Left join minus inner -> rows in file1 not in file2
only_in_file1 = df1[~df1[key_column].isin(df2[key_column])]

# Right join minus inner -> rows in file2 not in file1
only_in_file2 = df2[~df2[key_column].isin(df1[key_column])]

# --- Write to Excel ---
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    matching.to_excel(writer, sheet_name="Matching", index=False)
    only_in_file1.to_excel(writer, sheet_name="Only_in_File1", index=False)
    only_in_file2.to_excel(writer, sheet_name="Only_in_File2", index=False)

print(f"✅ Comparison complete. Results saved in {output_file}")
