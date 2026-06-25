# oasisinfobyte-intenship-project3
# Data cleaning

##  Project Overview
This project focuses on cleaning and preprocessing the Airbnb NYC 2019 dataset using Python and Pandas. The goal is to improve data quality by handling missing values, removing duplicates, standardizing text data, and eliminating outliers.

##  Dataset
Dataset Used: AB_NYC_2019.csv

The dataset contains information about Airbnb listings in New York City, including:
- Listing names
- Host information
- Neighborhood details
- Price
- Reviews
- Availability

## Technologies Used
- Python
- Pandas
- NumPy

##  Data Cleaning Steps Performed

### 1. Data Inspection
- Displayed first 5 rows
- Checked dataset shape
- Viewed dataset information

### 2. Missing Value Handling
- Filled missing `host_name` values with "Unknown"
- Filled missing `reviews_per_month` values using median
- Filled missing `last_review` values with "Not Reviewed"
- Filled missing `name` values with "No Name"

### 3. Duplicate Removal
- Identified duplicate records
- Removed duplicate rows

### 4. Data Standardization
- Removed extra spaces from text columns
- Standardized host names using title case

### 5. Outlier Removal
- Applied IQR (Interquartile Range) method on the `price` column
- Removed extreme price outliers

### 6. Export Cleaned Data
- Saved the cleaned dataset as:
  `cleaned_AB_NYC_2019.csv`

## 📊 Output
The cleaned dataset is free from:
- Missing values
- Duplicate records
- Extreme outliers in price data

