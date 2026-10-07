import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone"],
    "City": ["Hyderabad", "Chennai", "Hyderabad", "Delhi", "Chennai"],
    "Year": [2024, 2024, 2025, 2025, 2025],
    "Sales": [50000, 30000, 60000, 20000, 40000]
})

print("Data Cube:")
print(df)


# ---------------- ROLL-UP ----------------
print("\nRoll-up:")

total = df["Sales"].sum()

print("Total Sales:", total)


# ---------------- SLICE ----------------
print("\nSlice:")

slice_data = df[df["City"] == "Hyderabad"]

print(slice_data)


# ---------------- DICE ----------------
print("\nDice:")

dice_data = df[
    (df["Product"] == "Laptop") &
    (df["Year"] == 2025)
]

print(dice_data)


# ---------------- DRILL-DOWN ----------------
print("\nDrill-down:")

print(df.sort_values(["Product", "Year"]))