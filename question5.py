import pandas as pd

# Load the data
df = pd.read_csv('ApplianceWorld.csv', delimiter=';')

# Ensure the 'Year-Month' column is in the correct format
df['Year-Month'] = pd.to_datetime(df['Year-Month'], format='%Y%m')

# Get the most recent month in the data
recent_month = df['Year-Month'].max()

# Filter data for the last 6 months
last_6_months = df[df['Year-Month'] >= recent_month - pd.DateOffset(months=6)]

# Group by Product Code and sum the # Units Sold for each month
units_sold_by_product = last_6_months.groupby(['Product Code', 'Year-Month'])['# Units Sold'].sum().unstack()

# Calculate the difference in # Units Sold between the most recent month and 6 months ago
units_sold_by_product['Decline'] = units_sold_by_product[recent_month] - units_sold_by_product[recent_month - pd.DateOffset(months=5)]

# Sort the products by the greatest decline in units sold
top_3_declines = units_sold_by_product['Decline'].sort_values().head(3)

# Display the top 3 products with the most significant decline
print("Top 3 products with the most significant decline in # Units Sold over the last 6 months:")
print(top_3_declines)
