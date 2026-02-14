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
- region – Azure deployment region (US-East, US-West, EU-Central, Asia-South)
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

## Future Work

- Feature Engineering & Data Wrangling
- Machine Learning Model Development
- Forecast Integration & Capacity Planning

---

## License

This project is licensed under the MIT License.
