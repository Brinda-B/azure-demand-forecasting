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
- Plotly (Visualization)
- Google Colab
- GitHub

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

## Future Work

- Milestone 3: Train and evaluate forecasting models (ARIMA, XGBoost) using MAE, RMSE, and bias with backtesting.
- Milestone 4: Simulate model deployment and integrate forecasts with capacity planning logic.

---

## License

This project is licensed under the MIT License.
