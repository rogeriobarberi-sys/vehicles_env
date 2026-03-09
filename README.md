# Vehicles US — Exploratory Data Analysis (EDA) + Interactive App

This repository contains an **interactive Exploratory Data Analysis (EDA)** project built with **Streamlit** using the **Vehicles US** dataset.  
The goal is to explore the dataset, document data-quality decisions, and provide interactive visualizations that support clear insights.

## Links

- **Live App (Render):** https://vehicles-env-1niq.onrender.com  
- **GitHub Repository:** https://github.com/rogeriobarberi-sys/vehicles_env  
- **Portuguese README:** [README.pt-BR.md](README.pt-BR.md)

---

## Project Goals

- Build a **reproducible EDA workflow**
- Identify and document **data quality issues** (missing values, types, potential outliers)
- Create **interactive visualizations** to support analysis
- Publish a working web app as a **portfolio-ready project**

---

## Dataset

- File: `vehicles_us.csv`  
- Context: used vehicle listings with fields such as **price**, **odometer**, **model year**, **condition**, etc.

---

## App Features (Interactive EDA)

The Streamlit app allows the user to:

- View a **data preview** (table) after applying filters
- Inspect **missing values** by column
- Review **descriptive statistics** for numeric columns
- Interact with UI controls (e.g., **checkboxes**, filters)
- Explore at least two visualizations:
  - **Histogram** (example: `price` distribution)
  - **Scatter plot** (example: `price` vs `odometer`)

---

## Data Cleaning & Preprocessing (Documented Decisions)

This project avoids “hidden magic” by applying cleaning steps transparently.

### 1) Data types
- Validate numeric columns (e.g., `price`, `odometer`, `model_year`) as numeric types
- Confirm categorical columns (e.g., `condition`) as categories/strings

### 2) Missing values
- Measure missingness by column
- For visualizations that require complete values (e.g., scatter plot), rows with missing `x` or `y` are excluded **only for that chart**, not globally

### 3) Outliers (practical approach)
- Inspect extreme values (very high `price` / very high `odometer`)
- Avoid deleting rows “just to look clean”; apply filtering only when it improves interpretability and is explicitly explained in the app/notebook

> **Note:** Any filtering rules should be visible and justifiable. Portfolio credibility comes from clear decisions, not from “perfect-looking” charts.

---

## Key Findings (Replace with Your Real Results)

Add 3–6 bullets based on what you actually observe. Example structure:

- **Price distribution** is right-skewed (most listings are in lower price ranges)
- **Higher mileage** tends to correlate with **lower price**, with variation by condition
- **Condition** categories show clear separation in typical price ranges

---

## Tech Stack

- **Python**
- **Pandas**
- **Streamlit**
- **Plotly**

---

## How to Run Locally

1. Clone the repository:
   - `git clone https://github.com/rogeriobarberi-sys/vehicles_env.git`
2. Enter the project directory:
   - `cd vehicles_env`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Run the app:
   - `streamlit run app.py`

---

## Repository Structure

- `app.py` — Streamlit app (interactive EDA + charts)
- `EDA.ipynb` — notebook-based exploratory analysis
- `vehicles_us.csv` — dataset used by the app
- `requirements.txt` — Python dependencies
- `render.yaml` — deployment configuration for Render
- `.streamlit/` — Streamlit configuration (theme/settings)

---

## Notes

- The **Render link** above is the deployed version of the app.
- The notebook (`EDA.ipynb`) complements the app with a more detailed EDA narrative.

## Versão em português (PT-BR version)
A versão em português está em README.pt-BR.md.
