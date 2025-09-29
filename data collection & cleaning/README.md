# 🏠 Real Estate Price Predictor in Egypt

This repository contains the **data collection, cleaning, and initial exploratory analysis** steps for a Real Estate Price Prediction project focused on ready-to-sell properties in Egypt.

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| `scraping.py` | Python script used to perform web scraping from [Bayut.com](https://www.bayut.com/) to collect property listings. |
| `houses.csv` | Raw dataset (~50,000 rows) obtained after scraping, containing property type, price, area, bathrooms, bedrooms, and location. |
| `ready_houses.xlsx` | Cleaned dataset (~46,000 rows) after preprocessing, including a small dashboard and basic analysis. |
| `Real Estate Price Predictor in Egypt.pdf` | Documentation summarizing project steps (data collection, cleaning, and exploratory data analysis). |

---

## 📝 Project Overview

- **Objective:** Predict prices of ready-to-sell houses in Egypt.
- **Data Source:** Properties scraped from Bayut.com using Python.
- **Initial Dataset Size:** ~50,000 records.
- **Cleaned Dataset Size:** ~46,000 records after removing duplicates, rare categories, and handling outliers.

---

## 🔧 Data Cleaning & Preprocessing

Key steps taken (detailed in the PDF):

- Removed duplicate records and dropped rows with <5% missing values.
- Standardized column names.
- Merged rare property types into broader groups.
- Grouped extreme values for bedrooms and bathrooms (6+ into one category).
- Extracted numeric values from text fields (e.g., `140 متر مربع` → `140`).
- Cleaned location fields (separated area/governorate, dropped very rare values).
- Handled outliers in price, area, and rooms.
- Added a log-transformed price column for modeling.

---

## 📊 Exploratory Data Analysis (EDA)

- **Average price per property type** (Villas highest, Apartments lowest).
- **Average price per location and sub-location** (North Coast and Sidi Abdel Rahman highest).
- **Number of houses per location** (Cairo and New Cairo dominate).
- **Distribution of bedrooms and bathrooms** (most properties have 2–3).

These insights help identify market segments and prepare the dataset for modeling.

---

## 📈 Current Dataset Status

- ~46,000 cleaned rows of ready-to-sell properties.
- Main features prepared for modeling.
- No duplicates or major missing values remain.
- Dataset is ready for feature encoding and model training.

---

## 🚀 Next Steps

- Encode categorical features (property type, location).
- Normalize/log-transform skewed numerical features (price).
- Perform train/test split for model evaluation.
- Build baseline models (Linear Regression, Random Forest, etc.).
- Evaluate and tune models to improve accuracy.

---

## 👤 Author

Mohamed Waleed EL-masry  
📧 mwezzat16@gmail.com


