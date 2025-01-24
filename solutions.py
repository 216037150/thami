import pandas as pd

# Read the Excel file
df = pd.read_excel('ApplianceWorld.xlsx')

df.to_csv('ApplianceWorld.csv', index=False, sep=';')

# Read the CSV file
csv_data = pd.read_csv('ApplianceWorld.csv', sep=';')
import pandas as pd

# Read the CSV data
df = pd.read_csv('ApplianceWorld.csv', delimiter=';')

# Filter for Quarter 1 of 2023 (January, February, March)
q1_2023 = df[(df['Year'] == 2023) & (df['Month No'].isin([1, 2, 3]))]

# Calculate total revenue for Quarter 1 of 2023
total_revenue_q1_2023 = q1_2023['Revenue'].sum()
print(f"Total revenue for Quarter 1 of 2023: {total_revenue_q1_2023}")


# Question 2: Top 5 Best-Selling Appliances for 2023 and 2024 Combined
top_appliances = df[df['Year'].isin([2023, 2024])]
top_appliances_grouped = top_appliances.groupby('Product Code')['Revenue'].sum().sort_values(ascending=False).head(5)
print("Top 5 best-selling appliances based on revenue:")
print(top_appliances_grouped)

# Question 3: Highest Revenue Growth States (assuming we have state data, which isn't in the provided dataset)
# If we had state data, it would look like this:
# Assuming 'state' column exists
# df['State'] = some_column_for_state
# growth_by_state = df.groupby(['State', 'Year'])['Revenue'].sum().unstack()
# growth_by_state['Growth'] = growth_by_state[2024] - growth_by_state[2023]
# top_3_states_growth = growth_by_state.sort_values('Growth', ascending=False).head(3)
# print("Top 3 states with highest growth:")
# print(top_3_states_growth)

# Question 4: Top 5 Salespersons in the Best 3 States (for 2024)
# Assuming 'state' and 'SalesPersonID' exist, and we found the best 3 states already
# df['SalesPerson Profit'] = df['Revenue'] - df['Cost of Sales']
# top_salespersons = df[df['State'].isin(top_3_states_growth.index)].groupby('SalesPersonID')['SalesPerson Profit'].sum().sort_values(ascending=False).head(5)
# print("Top 5 salespersons by profit in 2024:")
# print(top_salespersons)

# Question 5: Top 3 Products with Most Decline in Units Sold
# For the last 6 months, calculate the difference in units sold by product code
# Assuming 'Month No' is a numerical representation, let's take the last 6 months and compare
recent_data = df[df['Year'] == 2024]
recent_units_sold = recent_data.groupby('Product Code')['# Units Sold'].sum()
previous_data = df[(df['Year'] == 2023) & (df['Month No'] > 6)]
previous_units_sold = previous_data.groupby('Product Code')['# Units Sold'].sum()
units_sold_change = recent_units_sold - previous_units_sold
declining_products = units_sold_change.sort_values().head(3)
print("Top 3 products with the most significant decline in units sold:")
print(declining_products)


