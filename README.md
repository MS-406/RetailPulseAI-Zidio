# RetailPulse AI - Customer Analytics and Demand Forecasting

RetailPulse AI is an end-to-end data science project for retail demand planning, customer segmentation, churn-risk detection, and inventory optimization. The project follows the Zidio Data Science and Analytics brief for the first two weeks of work and uses the provided Online Retail dataset.

## Project Objective

Retail businesses lose revenue when demand is poorly forecasted, customers at risk are missed, and stock decisions are made without data. This project turns transaction data into practical analytics outputs:

- Cleaned retail sales data ready for modeling
- RFM-based customer segmentation
- Daily demand forecasting outputs
- Churn-risk scores for customers
- Inventory reorder recommendations
- Drift checks and retraining policy

## Dataset Used

The project uses the provided `online_retail.csv` and `OnlineRetail.xlsx` files.

| Item | Value |
|---|---:|
| Raw rows | 541,909 |
| Raw columns | 8 |
| Cleaned transaction rows | 392,692 |
| Date range | 2010-12-01 to 2011-12-09 |
| Countries | 38 |
| Duplicate rows found | 5,268 |
| Missing descriptions | 1,454 |
| Missing customer IDs | 135,080 |
| Cancelled invoices | 9,288 |
| Negative quantity rows | 10,624 |
| Non-positive unit price rows | 2,517 |

## Missing Value and Cleaning Strategy

The project intentionally keeps the data-quality issues visible in the documentation and handles them before modeling:

- Rows with missing `CustomerID` are removed from RFM, segmentation, and churn modeling because they cannot be assigned to a known customer.
- Rows with missing `Description` are removed from product and inventory analysis.
- Duplicate rows are removed during cleaning.
- Cancelled invoices and rows with `Quantity <= 0` are excluded from demand forecasting and inventory recommendations.
- Rows with `UnitPrice <= 0` are excluded because they do not represent valid revenue transactions.
- `InvoiceDate` is parsed as a datetime field.
- `TotalPrice = Quantity * UnitPrice` is created for revenue analysis.

## Repository Structure

```text
RetailPulse-AI/
|-- data/
|   |-- raw/
|   |-- cleaned/
|-- exports/
|-- models/
|-- notebooks/
|-- reports/
|-- scripts/
|-- mlflow.db
|-- requirements.txt
|-- README.md
```

## Week 1 Status - Completed

Week 1 focused on data exploration and preparation.

| Day | Task from brief | Status | Output |
|---:|---|---|---|
| 1 | Dataset selection and initial EDA | Completed | `notebooks/01_eda.ipynb` |
| 2 | Data cleaning and feature engineering | Completed | `data/cleaned/cleaned_retail.csv` |
| 2 | Data validation checks | Completed | Cleaning rules documented in this README |
| 3 | Customer segmentation with K-Means and DBSCAN | Completed | `notebooks/02_customer_segmentation.ipynb`, `data/cleaned/rfm_customers.csv` |
| 4 | Time-series preparation | Completed | `notebooks/03_time_series_preparation.ipynb` |
| 5 | Baseline forecasting | Completed | `notebooks/04_demand_forecasting.ipynb`, `exports/forecast_results.csv` |
| 6 | LSTM implementation | Completed | `notebooks/05_lstm_model_implementation.ipynb`, `models/lstm_model.pth` |
| 7 | Week 1 checkpoint | Completed | `reports/week1_week2_completion_report.md` |

## Week 2 Status - Completed

Week 2 focused on advanced modeling, churn prediction, inventory logic, drift checks, and retraining planning.

| Day | Task from brief | Status | Output |
|---:|---|---|---|
| 8 | Hybrid forecasting model | Completed | `exports/week2_hybrid_forecast.csv` |
| 9 | Churn prediction model | Completed | `exports/week2_churn_predictions.csv` |
| 10 | Inventory optimization logic | Completed | `exports/week2_inventory_recommendations.csv` |
| 11 | Feature importance analysis | Completed | `exports/week2_feature_importance.csv` |
| 12 | Drift detection setup | Completed | `exports/week2_drift_checks.csv` |
| 13 | Automated retraining pipeline plan | Completed | `reports/week1_week2_completion_report.md` |
| 14 | Week 2 checkpoint | Completed | `reports/week1_week2_completion_report.md` |

## Week 2 Model Summary

The Week 2 pipeline is reproducible from:

```bash
python scripts/week2_pipeline.py
```

Generated outputs:

- `exports/week2_hybrid_forecast.csv`
- `exports/week2_customer_features.csv`
- `exports/week2_churn_predictions.csv`
- `exports/week2_inventory_recommendations.csv`
- `exports/week2_feature_importance.csv`
- `exports/week2_drift_checks.csv`
- `reports/week1_week2_completion_report.md`

Current Week 2 checkpoint metrics:

| Metric | Value |
|---|---:|
| Customers scored for churn | 3,370 |
| Churn model AUC-ROC | 0.715 |
| Churn model F1 | 0.644 |
| High-risk customers identified | 1,039 |
| Inventory SKUs scored | 2,953 |
| Recent hybrid forecast MAPE | 0.314 |
| Drift flags raised | 0 |

## Technology Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Data processing | Pandas, NumPy |
| Machine learning | Scikit-learn, PyTorch, Prophet-ready outputs |
| Segmentation | K-Means, DBSCAN |
| Experiment tracking | MLflow |
| Dashboard roadmap | Streamlit |
| Monitoring roadmap | Evidently AI-style drift checks |

## How to Run

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Week 2 reproducible pipeline:

```bash
python scripts/week2_pipeline.py
```

4. Review the completion report:

```text
reports/week1_week2_completion_report.md
```

## Current Project Milestone

- Week 1: Completed
- Week 2: Completed
- Week 3: Dashboard and analytics layer pending
- Week 4: Deployment and production polish pending

## Submission Notes

This README now reflects the Zidio brief requirements for Week 1 and Week 2, including missing-value handling, cleaned data preparation, modeling outputs, and documented next steps.
