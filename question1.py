import pandas as pd

# Read the CSV data
df = pd.read_csv('ApplianceWorld.csv', delimiter=';')

# Filter for Quarter 1 of 2023 (January, February, March)
q1_2023 = df[(df['Year'] == 2023) & (df['Month No'].isin([1, 2, 3]))]

# Calculate total revenue for Quarter 1 of 2023
total_revenue_q1_2023 = q1_2023['Revenue'].sum()
print(f"Total revenue for Quarter 1 of 2023: {total_revenue_q1_2023}")
