import pandas as pd

df = pd.DataFrame({
    "Name": ["Arjun", "Rahul", "Priya", "Anu", "Ravi"],
    "Age": [20, 35, 25, 40, 22],
    "City": ["Hyderabad", "Delhi", "Chennai", "Mumbai", "Bangalore"]
})

print("Original Data:")
print(df)

# Generalize Age
age_group = []

for age in df["Age"]:
    if age < 30:
        age_group.append("Young")
    else:
        age_group.append("Adult")

df["Age Group"] = age_group


# Generalize City
region = []

for city in df["City"]:
    if city in ["Hyderabad", "Chennai", "Bangalore"]:
        region.append("South")
    else:
        region.append("North")

df["Region"] = region


print("\nGeneralized Data:")
print(df[["Age Group", "Region"]])

print("\nCount:")
print(df.groupby(["Age Group", "Region"]).size())