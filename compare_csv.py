import pandas as pd

# Load CSVs
a = pd.read_csv("A.csv")
b = pd.read_csv("B.csv")

# Define key column
key_col = "id"   # <-- change this as needed

# 1. Matching rows (keys present in both A and B, keep full row from A)
matching = a[a[key_col].isin(b[key_col])]

# 2. A - B (keys in A but not in B)
a_not_b = a[~a[key_col].isin(b[key_col])]

# 3. B - A (keys in B but not in A)
b_not_a = b[~b[key_col].isin(a[key_col])]

# Save results
matching.to_csv("matching.csv", index=False)
a_not_b.to_csv("a_not_in_b.csv", index=False)
b_not_a.to_csv("b_not_in_a.csv", index=False)

print("✅ Done! Generated:")
print(" - matching.csv (full rows from A where key in both)")
print(" - a_not_in_b.csv (rows only in A)")
print(" - b_not_in_a.csv (rows only in B)")
