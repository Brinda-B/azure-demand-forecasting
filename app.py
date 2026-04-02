import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# Load model
model = joblib.load("best_demand_forecast_model.pkl")

st.set_page_config(layout="wide")
st.title("AZURE CAPACITY INTELLIGENCE")

st.sidebar.header("Filters")

regions = st.sidebar.multiselect("Regions",
    ["East US", "West US", "Central US", "East Asia", "Germany West Central"],
    default=["East US", "Central US"]
)

service = st.sidebar.multiselect("Service Type",
    ["Compute", "Storage"],
    default=["Compute"]
)

year = st.sidebar.multiselect("Year",
    [2022, 2023, 2024],
    default=[2023]
)

threshold = st.sidebar.slider("Capacity Risk Threshold", 0.0, 1.0, 0.65)

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 KPI Overview",
    "📈 Demand Trends",
    "🌍 Regional Analysis",
    "📂 Upload CSV"
])

with tab1:
    st.subheader("Executive KPIs")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cost", "$20.29M")
    col2.metric("Wasted Cost", "$16.78M")
    col3.metric("Avg Utilization", "54.7%")
    col4.metric("Total Incidents", "624")

    st.markdown("---")

    st.subheader("Prediction Section")

    capacity = st.slider("Capacity Utilization", 0.0, 1.0, 0.8)
    cost = st.number_input("Cost per Unit", value=0.1)
    growth = st.number_input("Growth Rate", value=0.05)
    rolling = st.number_input("3 Month Avg Usage", value=5000)
    lag1 = st.number_input("Last Month Usage", value=4800)
    lag2 = st.number_input("2nd Last Month Usage", value=4700)
    external = st.number_input("External Score", value=85)

    if st.button("Predict Demand"):
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
        st.success(f"Predicted Demand: {round(result[0],2)}")

with tab2:
    st.subheader("Usage & Demand Over Time")

    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Usage": [4000, 4200, 4300, 4500, 4700, 4800]
    })

    fig = px.line(df, x="Month", y="Usage", title="Monthly Usage Trend")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Growth Rate")

    growth_df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Growth": [0.02, 0.03, 0.025, 0.04, 0.035, 0.05]
    })

    fig2 = px.bar(growth_df, x="Month", y="Growth", title="Growth Rate")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Regional Capacity Analysis")

    df_region = pd.DataFrame({
        "Region": ["East US", "Central US", "West US"],
        "Utilization": [60, 55, 70],
        "Waste": [20, 25, 15],
        "Cost": [200, 180, 220]
    })

    fig3 = px.scatter(df_region,
                      x="Utilization",
                      y="Waste",
                      size="Cost",
                      color="Region",
                      title="Utilization vs Waste")

    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Top Regions by Waste")

    fig4 = px.bar(df_region, x="Region", y="Waste")
    st.plotly_chart(fig4, use_container_width=True)

with tab4:
    st.subheader("Upload CSV for Batch Prediction")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("📄 Input Data", df.head())

        try:
            predictions = model.predict(df)
            df["Predicted Demand"] = predictions

            st.write("✅ Output with Predictions", df)

        except Exception as e:
            st.error("⚠️ Error: Ensure your CSV has correct feature columns")