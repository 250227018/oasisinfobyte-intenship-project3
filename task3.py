import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/datasets/AB_NYC_2019.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values

# host_name missing values
df['host_name'].fillna('Unknown', inplace=True)

# reviews_per_month missing values
df['reviews_per_month'].fillna(df['reviews_per_month'].median(), inplace=True)

# last_review missing values
df['last_review'].fillna('Not Reviewed', inplace=True)

# name missing values
df['name'].fillna('No Name', inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check Duplicates
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Standardize Text Columns

df['host_name'] = df['host_name'].str.strip().str.title()
df['name'] = df['name'].str.strip()

# Outlier Detection and Removal

Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['price'] >= lower_bound) &
        (df['price'] <= upper_bound)]

print("\nDataset Shape After Cleaning:")
print(df.shape)

# Final Check
print("\nFinal Missing Values:")
print(df.isnull().sum())

# Save Cleaned Dataset
df.to_csv("cleaned_AB_NYC_2019.csv", index=False)

print("\nData Cleaning Completed Successfully!")