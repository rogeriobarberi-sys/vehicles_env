# US Vehicle Market - Strategic Data Analysis Dashboard

An advanced Exploratory Data Analysis (EDA) web application built with **Streamlit** and **Plotly**. This project goes beyond basic visualization, implementing robust data cleaning and statistical imputation to provide reliable market insights.

## 🚀 Live Demo
https://vehicles-env-1niq.onrender.com

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

### 2. Feature Engineering & Defensive Programming
- **Brand Extraction:** Extracted vehicle brands from the model strings to allow high-level market segmentation and brand-specific analysis.
- **Pathlib Integration:** Implemented robust file path resolution using `pathlib` for seamless deployment on Render/GitHub environments.
- **Data Typing:** Enforced strict numeric typing for `price`, `odometer`, and `model_year` to prevent runtime errors during interactive filtering.

### 3. Advanced Visualization & Business Logic
- **Depreciation Analysis:** A scatter plot with a "Condition" overlay to visualize how wear and tear affects resale value.
- **Market Liquidity Analysis:** Calculated the "Time-to-Sell" (Days Listed) for each vehicle category, identifying which types have the highest turnover.
- **Outlier Detection:** Used Boxplots to identify price outliers and distribution consistency across different vehicle types.

## 📁 Repository Structure
