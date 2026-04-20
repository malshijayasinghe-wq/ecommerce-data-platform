import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s — %(message)s"
)

logging.info("Pipeline started")

# Step 1 — Load dataset
sales = pd.read_csv(
    "G:/ecommerce-data-platform/data/Ecommerce Purchases.csv",
    encoding="latin1"
)

logging.info("Dataset loaded")

# Step 2 — Clean data

sales = sales.dropna(subset=["CustomerID"])
logging.info("Removed missing CustomerID")

sales = sales[sales["Quantity"] > 0]
logging.info("Removed negative quantities")

sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"])
logging.info("Converted InvoiceDate to datetime")

sales["Revenue"] = sales["Quantity"] * sales["UnitPrice"]
logging.info("Revenue column created")

# Step 3 — Save cleaned dataset

sales.to_csv(
    "G:/ecommerce-data-platform/data/cleaned_data.csv",
    index=False
)

logging.info("Cleaned data saved")

logging.info("Pipeline finished successfully")