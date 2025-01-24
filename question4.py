# Importing the DataFrame from Question 1
from question1 import df

# Ensure the 'State' and 'SalesPersonID' columns exist
print("Columns in DataFrame:", df.columns)

# Assuming you've already identified the top 3 states with the highest growth in revenue from Question 3
# (you can replace `top_3_states_growth` with the actual DataFrame from Question 3)

# Create a 'SalesPerson Profit' column: Revenue - Cost of Sales
df['SalesPerson Profit'] = df['Revenue'] - df['Cost of Sales']
print(df.columns)

# Filter data for 2024 and top 3 states
top_3_states = ['State1', 'State2', 'State3']  # Replace with actual state names
filtered_data = df[(df['Year'] == 2024) & (df['State'].isin(top_3_states))]

# Group by SalesPersonID and sum the profit
top_salespersons = filtered_data.groupby('SalesPersonID')['SalesPerson Profit'].sum().sort_values(ascending=False).head(5)

# Display the top 5 salespersons by profit
print("Top 5 Salespersons by profit in 2024:")
print(top_salespersons)
