## 🧹 Data Preprocessing Steps

### 1. Import Libraries
Used the following main libraries:
- **NumPy**, **Pandas** → Data manipulation and computation  
- **Matplotlib**, **Seaborn** → Visualization and exploratory analysis  
- **category_encoders** → Target encoding for categorical features  
- **Scikit-learn** → Train/test split and preprocessing utilities  

---

### 2. Load Dataset
- Loaded dataset from Excel containing property attributes (price, area, location, etc.).  
- Created a copy to preserve the original data.

---

### 3. Rename Columns
- Translated and standardized Arabic column names into English for consistency.  
  *(Example: السعر → price, نوع العقار → type, الموقع → location)*

---

### 4. Encode Categorical Values
- Converted Arabic property values to English (e.g., "شقة" → "Apartment", "فیلا" → "Villa").  
- Applied **Target Encoding** on `type`, `location`, and `sub_location` using mean target values with K-Fold validation.

---

### 5. Outlier Removal & Log Transformation
- Removed extreme values from `price` and `area` using quantile thresholds.  
- Applied **log transformation** on both columns to reduce skewness and improve stability.  
  - Target variable: `log_price`  
  - Feature: `log_area`

---

### 6. Feature Engineering
New features created to enrich the dataset:
- `bath_to_bed` → Bathrooms-to-bedrooms ratio  
- `total_rooms` → Sum of bedrooms and bathrooms  
- `log_total_rooms` → Log of total rooms  
- `area_per_room`, `area_per_bedroom` → Indicators of space efficiency  
- `loc_area_interaction`, `loc_cross` → Location-based interaction effects  

---

### 7. Train/Test Split & Export
- Defined **`log_price`** as the target variable.  
- Split the dataset into:
  - **Train (80%)**
  - **Test (20%)**
- Exported final processed files:
  - `train.csv`
  - `test.csv`

---

### ✅ Final Notes
- The final dataset is **cleaned, encoded, log-transformed**, and **feature-engineered**.  
- Ready for use in model training and evaluation.

---

## 📁 Resources

| File | Type | Description |
|------|------|-------------|
| `train.csv` | Data | Processed training dataset |
| `test.csv` | Data | Processed testing dataset |
| `Real Estate Price Prediction - Data Preprocessing & Feature Engineering.pdf` | Presentation | Full documentation of preprocessing steps and analysis |
| `house_preprocessing.ipynb` | Code | Complete preprocessing and feature engineering notebook |

---

📌 **Author:** Mohamed Waleed Elmasry  
📅 **Project:** Real Estate Price Prediction — Data Preprocessing & Feature Engineering  

