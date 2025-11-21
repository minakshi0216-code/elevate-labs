#created by Minakshi
import pandas as pd
import matplotlib.pyplot as plt


# 1. Load CSV file

df = pd.read_csv("sales.csv")     # CSV file MUST be inside the same folder


# 2. Show first few rows

print("First 5 rows of the dataset:")
print(df.head())


# 3. Basic summary

print("\nData Summary:")
print(df.describe())

# 4. Total sales for each product
sales_by_product = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales by Product:")
print(sales_by_product)
# 5. Plot bar chart
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()