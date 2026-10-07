import pandas as pd

# Sales data
sales = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Laptop", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics"],
    "Date": ["Jan", "Jan", "Feb", "Feb"],
    "Quantity": [10, 20, 15, 8]
})

print("Sales Data:")
print(sales)


# ---------------- STAR SCHEMA ----------------
print("\nStar Schema:")

fact_sales = sales

product = sales[["Product"]]
category = sales[["Category"]]
date = sales[["Date"]]

print("\nFact Sales:")
print(fact_sales)

print("\nProduct Dimension:")
print(product)

print("\nCategory Dimension:")
print(category)

print("\nDate Dimension:")
print(date)


# ---------------- SNOWFLAKE SCHEMA ----------------
print("\nSnowflake Schema:")

product = sales[["Product", "Category"]]
category = sales[["Category"]]
date = sales[["Date"]]

print("\nProduct:")
print(product)

print("\nCategory:")
print(category)

print("\nDate:")
print(date)

print("\nFact Sales:")
print(fact_sales)


# ---------------- FACT CONSTELLATION ----------------
print("\nFact Constellation:")

returns = pd.DataFrame({
    "Product": ["Phone", "Tablet"],
    "Date": ["Jan", "Feb"],
    "Quantity": [2, 1]
})

print("\nFact Sales:")
print(fact_sales)

print("\nFact Returns:")
print(returns)

print("\nShared Dimensions: Product, Date")