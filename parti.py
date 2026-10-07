import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "ID": [10, 25, 31, 42, 57, 68],
    "Name": ["Arjun", "Rahul", "Priya", "Anu", "Ravi", "Sneha"],
    "Age": [20, 22, 21, 23, 24, 25],
    "City": ["Hyderabad", "Chennai", "Delhi", "Mumbai", "Bangalore", "Pune"]
})

print("Original Data:")
print(df)


# 1. Horizontal Partitioning
print("\nHorizontal Partitioning:")

p1 = df.iloc[:3, :]
p2 = df.iloc[3:, :]

print("Partition 1:")
print(p1)

print("Partition 2:")
print(p2)


# 2. Vertical Partitioning
print("\nVertical Partitioning:")

p1 = df.iloc[:, [0, 1]]
p2 = df.iloc[:, [0, 2, 3]]

print("Partition 1:")
print(p1)

print("Partition 2:")
print(p2)


# 3. Round Robin Partitioning
print("\nRound Robin Partitioning:")

p1 = df.iloc[::2, :]
p2 = df.iloc[1::2, :]

print("Partition 1:")
print(p1)

print("Partition 2:")
print(p2)


# 4. Hash Based Partitioning
print("\nHash Based Partitioning:")

p1 = df[df.iloc[:, 0] % 3 == 0]
p2 = df[df.iloc[:, 0] % 3 == 1]
p3 = df[df.iloc[:, 0] % 3 == 2]

print("Partition 1:")
print(p1)

print("Partition 2:")
print(p2)

print("Partition 3:")
print(p3)