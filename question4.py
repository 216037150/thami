import pandas as pd

# Load the data
df = pd.read_csv('ApplianceWorld.csv', delimiter=';')

# Create the 'SalesPerson Profit' column: Revenue - Cost of Sales
df['SalesPerson Profit'] = df['Revenue'] - df['Cost of Sales']

# Filter the data for the year 2024
df_2024 = df[df['Year'] == 2024]

# Group by SalesPersonID and sum the profit, then sort by profit in descending order
top_salespersons = df_2024.groupby('SalesPersonID')['SalesPerson Profit'].sum().sort_values(ascending=False).head(5)

# Display the top 5 salespersons based on profit
print("Top 5 Salespersons by profit in 2024:")
print(top_salespersons)
