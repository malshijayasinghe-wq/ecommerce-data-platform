import pandas as pd

print("Starting data pipeline...")

# Step 1 — Load dataset
sales = pd.read_csv(
    "G:/ecommerce-data-platform/data/Ecommerce Purchases.csv",
    encoding="latin1"
)

print("Dataset loaded.")

# Step 2 — Clean data

# Remove missing CustomerID
sales = sales.dropna(subset=["CustomerID"])

# Remove negative Quantity
sales = sales[sales["Quantity"] > 0]

# Convert InvoiceDate to datetime
sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])

# Create Revenue column
sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]

print("Data cleaned.")

# Step 3 — Save cleaned dataset
sales.to_csv(
    "G:/ecommerce-data-platform/data/cleaned_data.csv",
    index=False
)

print("Pipeline finished successfully.")