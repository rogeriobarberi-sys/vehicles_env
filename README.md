![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

# 🚗 US Vehicle Market - Strategic Analysis Dashboard

A **Business Intelligence** web application built with **Streamlit** and **Plotly**. This project transforms a raw automotive listing dataset into a decision-making tool, utilizing advanced data engineering and interactive visualization techniques.

## 🚀 Live Demo
[https://vehicles-env-1niq.onrender.com](https://vehicles-env-1niq.onrender.com)

## 🎯 Project Goal
The objective was to transform a listing database into actionable insights for car dealerships, answering key market questions:
* Which vehicle categories sell the fastest (liquidity)?
* What is the real impact of 4WD traction on resale price?
* How do mileage and color influence asset depreciation?

---

## 🛠 Tech Stack
* **Python 3.12** (Project Core)
* **Pandas** (Data Manipulation & Statistical Imputation)
* **Streamlit** (Web Interface & Dashboard Deployment)
* **Plotly Express** (Dynamic Interactive Visualizations)
* **Render** (Hosting & CI/CD via GitHub)

---

## 📊 Data Engineering & Cleaning (Professional Approach)

Data integrity is the foundation of reliable insights. I implemented a cleaning pipeline that prevents the loss of valuable information:

### 1. Contextual Group-based Imputation
To avoid the bias of simply deleting incomplete rows, I utilized **statistical imputation**:
* **Model Year & Cylinders:** Missing values were filled using the **median by model** (`groupby('model')`), ensuring a sedan doesn't receive truck specifications.
* **Odometer:** Mileage was imputed based on the **median model year**, respecting the natural correlation between age and usage.
* **Boolean Normalization:** The `is_4wd` column was normalized (nulls to `0`), enabling precise binary analysis of value appreciation.

### 2. Defensive Programming & Optimization
* **Path Resolution (Pathlib):** The system automatically detects the environment (Local vs. Render) to locate `.csv` files, eliminating directory errors.
* **Data Caching (`@st.cache_data`):** Implemented caching so that loading and processing 51,525 rows occurs only once, making the user experience instantaneous.

---

## 📈 Business Analysis Implemented

The dashboard was designed to answer strategic market questions:

* **Value-Added Analysis (4WD):** We measured the financial impact of all-wheel drive on resale prices using **Boxplots**, allowing for the identification of median values and price dispersion (outliers).
* **Mileage Impact (Depreciation):** Interactive scatter plots correlating vehicle usage with value, segmented by condition (Excellent, Good, Fair) using **Lowess trendlines**.
* **Liquidity Analysis (Time to Sell):** Study of `days_listed` to understand which price ranges and vehicle types have the highest inventory turnover.
* **Temporal Trend Curves:** Line charts demonstrating average price variation by manufacture year, essential for understanding annual depreciation.

---

## 💡 Key Business Insights

Beyond simple visualization, this project extracted actionable patterns:

* **Inventory Turnover:** We identified that **Trucks and Pickups under $30k** are the highest liquidity assets (fastest sales).
* **Price Premium:** Vehicles with **4WD** show a median price up to **100% higher** than 4x2 models.
* **Depreciation Curve:** Using *Lowess* trendlines, we mapped that the "blind spot" for depreciation occurs after **150,000 miles**, where condition becomes secondary to residual functional value.
* **Color Psychology:** Vibrant colors (Yellow/Orange) signal high-ticket niches, while Purple and Green suffer higher depreciation due to lower market acceptance.

---

## 📁 Repository Structure
* `app.py`: Main Streamlit application code.
* `notebooks/EDA.ipynb`: Detailed exploratory analysis and cleaning drafts.
* `vehicles_us.csv`: Dataset (referenced in the root).
* `requirements.txt`: List of dependencies for the production environment.

---

### 💻 How to run this project locally
1. Clone the repository.
2. Create a virtual environment: `python -m venv env`.
3. Activate the environment and install dependencies: `pip install -r requirements.txt`.
4. Run the app: `streamlit run app.py`.

---
**Developed by Rogério Barberi**
