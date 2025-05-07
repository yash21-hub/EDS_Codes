import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code

date_products = {}

# Group products by date
for date, group in df.groupby('Date'):
    products = group['Product'].unique()
    if len(products) > 1:
        date_products[date] = products

# Count product pairs
pair_counter = Counter()

for products in date_products.values():
    # Sort to avoid duplicate pairs like (A,B) and (B,A)
    pairs = combinations(sorted(products), 2)
    pair_counter.update(pairs)

# Find the maximum frequency
if pair_counter:
    max_count = max(pair_counter.values())

    # Output the most frequent product pairs
    for pair, count in pair_counter.items():
        if count == max_count:
            print(f"{pair[0]} and {pair[1]}: {count} times")
else:
    print("No product pairs found.")
# Output the most frequent product pairs