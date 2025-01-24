# Import df from question1
from question1 import df  

# Filter data for years 2023 and 2024
data_2023_2024 = df[df['Year'].isin([2023, 2024])]

# Group by Product Code and calculate total revenue
revenue_by_product = data_2023_2024.groupby('Product Code')['Revenue'].sum()

# Sort by revenue in descending order and select the top 5
top_5_products = revenue_by_product.sort_values(ascending=False).head(5)

print("Top 5 best-selling appliances (based on revenue) for 2023 and 2024 combined:")
print(top_5_products)
