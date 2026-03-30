import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = joblib.load("best_demand_forecast_model.pkl")

# Page settings
st.set_page_config(page_title="Azure Demand Dashboard", layout="wide")

st.title("Azure Demand Forecasting Dashboard")

st.sidebar.header("Input Features")

capacity = st.sidebar.slider("Capacity Utilization", 0.0, 1.0, 0.8)
cost = st.sidebar.number_input("Cost per Unit", value=0.1)
growth = st.sidebar.number_input("Usage Growth Rate", value=0.05)
rolling = st.sidebar.number_input("3 Month Avg Usage", value=5000)
lag1 = st.sidebar.number_input("Last Month Usage", value=4800)
lag2 = st.sidebar.number_input("2nd Last Month Usage", value=4700)
external = st.sidebar.number_input("External Demand Score", value=85)

region = st.sidebar.selectbox("Region", ["US-East", "EU-Central"])
service = st.sidebar.selectbox("Service Type", ["Compute", "Storage"])


tab1, tab2 = st.tabs(["📊 Prediction", "📈 Analysis"])

with tab1:
    st.subheader("Demand Prediction")

    if st.button("Predict Demand"):

        # Prepare input data
        data = pd.DataFrame([{
            'capacity_utilization': capacity,
            'cost_per_unit': cost,
            'usage_growth_rate': growth,
            'rolling_3m_avg_usage': rolling,
            'lag_1_usage': lag1,
            'lag_2_usage': lag2,
            'external_demand_score': external
        }])

        # Prediction
        result = model.predict(data)

        st.success(f"Predicted Demand: {round(result[0], 2)} units")

        # 📊 Demand Trend Graph
        st.subheader("Demand Trend")

        values = [lag2, lag1, result[0]]
        labels = ["2 Months Ago", "Last Month", "Predicted"]

        fig, ax = plt.subplots()  
        ax.plot(labels, values, marker='o')
        ax.set_ylabel("Usage Units")
        ax.set_title("Demand Trend Over Time")

        st.pyplot(fig)

with tab2:
    st.subheader("Feature Comparison")

    features = [
        "Capacity", "Cost", "Growth",
        "Rolling Avg", "Lag1", "Lag2", "External"
    ]

    values = [
        capacity, cost, growth,
        rolling, lag1, lag2, external
    ]

    fig2, ax2 = plt.subplots()   
    ax2.bar(features, values)
    ax2.set_title("Input Feature Distribution")
    ax2.set_ylabel("Values")

    st.pyplot(fig2)

    st.subheader("Selected Configuration")
    st.write(f"Region: {region}")
    st.write(f"Service: {service}")