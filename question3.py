# Importing the DataFrame from Question 1
from question1 import df

# Ensure the 'Revenue' and 'Year' columns exist
print("Columns in DataFrame:", df.columns)

# Convert 'Year-Month' to string format
df['Year-Month'] = df['Year-Month'].astype(str)

# Filter the data for Quarter 1 of 2023 (January)
q1_2023_data = df[(df['Year'] == 2023) & (df['Year-Month'].str.startswith('2023-01'))]

# Calculate the total revenue for Quarter 1 of 2023
total_revenue_q1 = q1_2023_data['Revenue'].sum()

# Group by SalesPersonID and Year, summing up Revenue
salesperson_year_revenue = df.groupby(['SalesPersonID', 'Year'])['Revenue'].sum().reset_index()

# Pivot the data to have separate columns for each year
salesperson_revenue_pivot = salesperson_year_revenue.pivot(index='SalesPersonID', columns='Year', values='Revenue')

# Calculate the year-on-year growth percentage
salesperson_revenue_pivot['Growth %'] = ((salesperson_revenue_pivot[2024] - salesperson_revenue_pivot[2023]) / salesperson_revenue_pivot[2023]) * 100

# Drop rows with NaN values (in case some IDs have data for only one year)
salesperson_revenue_pivot = salesperson_revenue_pivot.dropna()

# Sort by Growth % in descending order and select the top 3
top_3_salespersons = salesperson_revenue_pivot.sort_values('Growth %', ascending=False).head(3)

# Display the total revenue for Quarter 1
print("Total revenue for Quarter 1 of 2023:", total_revenue_q1)

# Display the top 3 SalesPersons with the highest revenue growth
print("\nTop 3 SalesPersons with the highest revenue growth:")
print("---------------------------------------------------")
print("{:<15} {:<10}".format("SalesPersonID", "Growth %"))
print("---------------------------------------------------")
for index, row in top_3_salespersons.iterrows():
    print("{:<15} {:.2f}%".format(index, row['Growth %']))
