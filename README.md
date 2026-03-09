# 🚗 US Vehicle Market - Strategic Analysis Dashboard

A **Business Intelligence** web application built with **Streamlit** and **Plotly**. This project transforms a raw dataset of automotive advertisements into a decision-making tool, using advanced data engineering techniques and dynamic interactive visualizations.

## 🚀 Live Demo
[https://vehicles-env-1niq.onrender.com](https://vehicles-env-1niq.onrender.com)

---

## 🛠 Technologies Used
* **Python 3.12** (Project Core)
* **Pandas** (Manipulation and Statistical Imputation)
* **Streamlit** (Web Interface and Dashboard Deployment)
* **Plotly Express** (Dynamic Interactive Visualizations)
* **Render** (Hosting and CI/CD via GitHub)

---

## 📊 Data Engineering & Cleaning (Professional Approach)

Data integrity is the foundation of reliable insights. I implemented a cleaning pipeline that avoids discarding valuable information:

### 1. Group-based Statistical Imputation
To avoid the bias of simply deleting incomplete rows, I used **contextual imputation**:
* **Model Year and Cylinders:** Missing values were filled using the **median per model** (`groupby('model')`), ensuring a sedan doesn't receive truck specifications.
* **Odometer:** Mileage was imputed based on the **median of the model year**, respecting the natural correlation between age and usage.
* **Boolean Normalization:** The `is_4wd` column was standardized (nulls to `0`), enabling precise binary analysis of vehicle valuation.

### 2. Defensive Programming & Optimization
* **Path Resolution (Pathlib):** The system automatically detects the environment (Local vs. Render) to locate `.csv` files, eliminating directory-related errors.
* **Data Caching (`@st.cache_data`):** Implemented caching so that loading and processing over 51,000 rows occurs only once, making the user experience instantaneous.



---

## 📈 Implemented Business Analyses

The dashboard was designed to answer strategic market questions:

* **Value-Added Analysis (4x4):** We measured the financial impact of all-wheel drive on resale prices using **Boxplots**, identifying medians and price dispersion (outliers).
* **Mileage Impact (Depreciation):** Interactive scatter plots correlating vehicle usage with value, segmented by condition (Excellent, Good, Fair).
* **Market Liquidity Analysis:** Study of `days_listed` to understand which price ranges and vehicle types have the highest inventory turnover.
* **Temporal Trend Curve:** Line charts demonstrating average price variation by manufacturing year, essential for understanding annual depreciation.

---

## 📁 Repository Structure
* `app.py`: Main Streamlit application code.
* `notebooks/EDA.ipynb`: Detailed exploratory analysis and cleaning drafts.
* `vehicles_us.csv`: Database (referenced in the root directory).
* `requirements.txt`: List of dependencies for the production environment.

---

### 💡 How to run this project locally
1. Clone the repository.
2. Create a virtual environment: `python -m venv env`.
3. Activate the environment and install dependencies: `pip install -r requirements.txt`.
4. Run the app: `streamlit run app.py`.