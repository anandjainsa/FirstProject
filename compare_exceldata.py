import pandas as pd

# --- Config ---
file1 = "file1.csv"   # can be .csv or .xlsx
file2 = "file2.csv"   # can be .csv or .xlsx
output_file = "column_comparison.xlsx"
column_name = "ID"    # column to compare

# --- Load files ---
if file1.endswith(".csv"):
    df1 = pd.read_csv(file1, usecols=[column_name])
else:
    df1 = pd.read_excel(file1, usecols=[column_name])

if file2.endswith(".csv"):
    df2 = pd.read_csv(file2, usecols=[column_name])
else:
    df2 = pd.read_excel(file2, usecols=[column_name])

# --- Compare ---
col1 = set(df1[column_name])
col2 = set(df2[column_name])

matching = pd.DataFrame({column_name: sorted(col1 & col2)})
only_in_file1 = pd.DataFrame({column_name: sorted(col1 - col2)})
only_in_file2 = pd.DataFrame({column_name: sorted(col2 - col1)})

# --- Write to Excel ---
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    matching.to_excel(writer, sheet_name="Matching", index=False)
    only_in_file1.to_excel(writer, sheet_name="Only_in_File1", index=False)
    only_in_file2.to_excel(writer, sheet_name="Only_in_File2", index=False)

print(f"✅ Column comparison complete. Results saved in {output_file}")
