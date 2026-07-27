import pandas as pd
import numpy as np
# Step 1: Create Sample Dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", np.nan],
    "Age": [25, np.nan, 35, 40, 30],
    "Salary": [50000, 60000, np.nan, 80000, 70000],
    "City": ["New York", "Chicago", "New York", np.nan, "Chicago"]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Step 2: Data Cleaning

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values with mean
# df["Age"].fillna(df["Age"].mean(), inplace=True)

df["Age"] = df["Age"].fillna(df["Age"].mean())

# df["Salary"].fillna(df["Salary"].mean(), inplace=True)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())


# Fill missing categorical values with mode

df["City"] = df["City"].fillna(df["City"].mode()[0])

print(df)

#  Drop rows where Name is missing
df.dropna(subset=["Name"], inplace=True)

print(df)

# # Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# print("\nData after Cleaning:")

#  Step 3: Data Preprocessing

# Convert Name to uppercase
df["Name"] = df["Name"].str.upper()

# Create Age Group column

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 30, 40, 100],
    labels=["Young", "Middle", "Senior"]
)

print(df)

# Normalize Salary(scaling)
df["Normalized_Salary"] = (
    (df["Salary"] - df["Salary"].min()) /
    (df["Salary"].max() - df["Salary"].min())
)

# print("\nData after Preprocessing:")
print(df)

print("__________________________")
print("Data Manipulation")
# # Step 4: Data Manipulation

# Filter employees with salary > 60000
high_salary = df[df["Salary"] > 60000]

# print("\nEmployees with Salary > 60000:")
print(high_salary)

print("______________________")
# Sort by Salary
sorted_df = df.sort_values(by="Salary", ascending=False)

# print("\nSorted by Salary:")
print(sorted_df)

# Group by City and calculate average salary

grouped = df.groupby("City")["Salary"].mean()

# print("\nAverage Salary by City:")
print(grouped)

# # Add a new column (Bonus = 10% of Salary)
df["Bonus"] = df["Salary"] * 0.10

# print("\nFinal DataFrame:")
print(df)




sales.csv 