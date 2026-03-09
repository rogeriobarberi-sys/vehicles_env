## Data Cleaning & Preprocessing (Documented Decisions)

The purpose of this stage is to keep the analysis **reproducible** and the criteria **transparent**, avoiding changes that could distort results.

### 1) Data types
- Validate and standardize numeric columns (e.g., `price`, `odometer`, `model_year`) as numeric types when applicable
- Confirm categorical columns (e.g., `condition`) as text/categories

### 2) Missing values
- Measure missingness by column
- For visualizations that require complete pairs (e.g., scatter plots), rows with missing `x` or `y` values are removed **only for that chart**, preserving the dataset for other analyses

### 3) Extreme values (outliers) — criteria-driven approach
- Inspect extreme values (e.g., very high prices / very high mileage) to assess plausibility and their impact on chart readability
- Apply filtering only with **clear analytical justification** (e.g., improving interpretability without introducing bias), keeping the rules explicit in the app/notebook

> **Note:** Any exclusion or filtering rules should be transparent and justified so the analysis can be reviewed by third parties.

## Versão em português (PT-BR version)
A versão em português está em README.pt-BR.md.
