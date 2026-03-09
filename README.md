# US Vehicle Market - Interactive EDA Dashboard

An advanced Exploratory Data Analysis (EDA) web application built with **Streamlit** and **Plotly**. This project goes beyond basic visualization, implementing robust data cleaning and statistical imputation to provide reliable market insights.

## 🛠 Tech Stack
- **Python** (Pandas, Pathlib)
- **Streamlit** (Web Interface & Deployment)
- **Plotly Express** (Interactive Graphics)
- **Render** (Cloud Hosting)

## 📊 Data Engineering & Cleaning (Professional Approach)

To ensure high-quality analysis and maintain a professional-grade portfolio, the following data integrity steps were implemented:

### 1. Robust Data Imputation (Group-based)
Instead of simply dropping rows with missing values, I applied a **context-aware imputation** strategy:
- **Model Year & Cylinders:** Missing values were filled using the **median** value of each specific vehicle `model`. This preserves the characteristic distribution of each car type.
- **Odometer:** Missing mileage was imputed based on the **median** for the corresponding `model_year`, reflecting the logical correlation between a car's age and its usage.
- **Boolean Features:** The `is_4wd` column was standardized, treating nulls as `0` (False) based on the dataset's structure.

### 2. Defensive Programming & Data Types
- Implemented a robust file path resolution using `pathlib` for seamless deployment on **Render/GitHub**.
- Enforced strict numeric typing for `price`, `odometer`, and `model_year` to prevent runtime errors during interactive filtering.

### 3. Advanced Visualization Logic
- **Depreciation Analysis:** A scatter plot with a "Condition" overlay to visualize how wear and tear affects resale value.
- **Market Segmentation:** Boxplots to identify price outliers and distribution across different vehicle types (SUV, Truck, Sedan, etc.).

---
*Note: This project was developed as part of the TripleTen Data Analytics Bootcamp, enhanced with custom features for professional portfolio standards.*
