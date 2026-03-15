import pandas as pd

# Load dataset
sales = pd.read_csv("G:/ecommerce-data-platform/data/Ecommerce Purchases.csv", encoding="latin1")

# Show first 5 rows
print("First 5 rows:")
print(sales.head())

# Show columns
print("\nColumns:")
print(sales.columns)

# Show data info (types and non-null counts)
print("\nData info:")
print(sales.info())

# Show missing values
print("\nMissing values:")
print(sales.isnull().sum())


# ------------------------
# BUSINESS INSIGHTS
# ------------------------

# Total transactions
print("\nTotal transactions:")
print(len(sales))

# Total revenue column
sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]

print("\nTotal revenue:")
print(sales["Revenue"].sum())

# Top selling products
print("\nTop 10 products:")
print(sales["Description"].value_counts().head(10))

# Top countries
print("\nTop countries:")
print(sales["Country"].value_counts().head())

# Top customers
print("\nTop customers by number of purchases:")
print(sales["CustomerID"].value_counts().head())