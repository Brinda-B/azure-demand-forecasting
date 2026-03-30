import streamlit as st
import joblib
import pandas as pd

model = joblib.load("best_demand_forecast_model.pkl")

st.title("Azure Demand Forecasting Dashboard")

st.write("Enter input values:")

capacity = st.slider("Capacity Utilization", 0.0, 1.0, 0.8)
cost = st.number_input("Cost per Unit", value=0.1)
growth = st.number_input("Usage Growth Rate", value=0.05)
rolling = st.number_input("3 Month Avg Usage", value=5000)
lag1 = st.number_input("Last Month Usage", value=4800)
lag2 = st.number_input("2nd Last Month Usage", value=4700)
external = st.number_input("External Demand Score", value=85)

if st.button("Predict"):
    data = pd.DataFrame([{
        'capacity_utilization': capacity,
        'cost_per_unit': cost,
        'usage_growth_rate': growth,
        'rolling_3m_avg_usage': rolling,
        'lag_1_usage': lag1,
        'lag_2_usage': lag2,
        'external_demand_score': external
    }])

    result = model.predict(data)
    st.success(f"Predicted Demand: {result[0]}")