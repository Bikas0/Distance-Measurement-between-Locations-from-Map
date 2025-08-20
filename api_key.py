

import csv
from itertools import permutations
import pandas as pd

data = pd.read_csv("branch_clean_addresses.csv")
# Generate all permutations (pairs without repetition)
pairs = permutations(data["Clean Address"], 2)

# Write to CSV
with open("address_combinations.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Address1", "Address2"])  # Header
    for a1, a2 in pairs:
        writer.writerow([a1, a2])

print("CSV file 'address_combinations.csv' generated with all combinations.")