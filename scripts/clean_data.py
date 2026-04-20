import pandas as pd

# Load dataset
sales = pd.read_csv(
    "G:/ecommerce-data-platform/data/Ecommerce Purchases.csv",
    encoding="latin1"
)

print("Original dataset shape:")
print(sales.shape)

# Remove missing CustomerID
sales = sales.dropna(subset=["CustomerID"])

# Remove negative Quantity
sales = sales[sales["Quantity"] > 0]

# Convert InvoiceDate to datetime
sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

# Create Revenue column
sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]

print("Cleaned dataset shape:")
print(sales.shape)

# Save cleaned data
sales.to_csv(
    "G:/ecommerce-data-platform/data/cleaned_data.csv",
    index=False
)

print("Cleaned data saved successfully.")