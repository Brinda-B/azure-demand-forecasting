# Azure Demand Forecasting

## Project Overview
This project focuses on forecasting Azure cloud service demand 
(Compute and Storage) using historical usage data along with 
external market indicators.

The goal is to improve capacity planning and cost optimization
by integrating internal Azure usage metrics with external economic variables.

---

## Dataset Description

The dataset contains the following columns:

- time_stamp – Date and time of record
- region – Azure deployment region (US-East, EU-Central)
- service_type – Type of service (Compute, Storage)
- usage_units – Total resource usage
- provisioned_capacity – Allocated system capacity
- cost_usd – Estimated cost in USD
- market_demand_index – External cloud demand indicator
- customer_growth – Growth rate of Azure customers
- regional_growth – Regional economic growth indicator

---

## Tools & Technologies Used

- Python
- Pandas
- NumPy
- XGBoost
- Joblib
- Streamlit
- Plotly (Visualization)
- Google Colab

---

## Milestone 1: Data Collection & Preparation

* Azure usage data generated and structured  
* External economic variables integrated  
* Data cleaned and validated  
* Final dataset prepared for forecasting models  

---

## Milestone 2: Feature Engineering

- Created demand drivers
- Added rolling and lag features
- Implemented seasonality detection
- Prepared model-ready dataset

---

### Engineered Features

- capacity_utilization
- cost_per_unit
- usage_growth_rate
- is_peak_season
- rolling_3m_avg_usage
- usage_spike_flag
- lag_1_usage
- lag_2_usage
- external_demand_score

---

## Milestone 3: Machine Learning Model Development

- Implemented multiple forecasting models including XGBoost, and ARIMA.
- Performed hyperparameter tuning using GridSearchCV for model optimization.
- Evaluated model performance using MAE, RMSE, and forecast bias.
- Compared model predictions against actual demand values.
- Visualized forecast performance for model comparison.
- Selected the best model based on RMSE

---

## Live Dashboard
Access the deployed dashboard here: 
https://azure-demand-forecasting-optimization.streamlit.app/

---

## Milestone 4: Forecast Integration & Capacity Planning

- Deployed the trained machine learning model using a Streamlit dashboard.
- Enabled real-time demand prediction through user input interface.
- Integrated model predictions into a simple interactive web application.
- Implemented dynamic input-based forecasting for simulation of real-world usage.
- Demonstrated model accessibility through a live deployed dashboard link.
  
---

## Documentation

- Agile project
- Defect Tracker
- Unit Testing
---

## License

This project is licensed under the MIT License.
