import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="RetailPulse AI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
<style>
    .metric-card {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #4CAF50;
    }
    .metric-label {
        font-size: 1rem;
        color: #B0BEC5;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛒 RetailPulse AI Executive Dashboard")
st.markdown("Welcome to the RetailPulse AI platform. Use the sidebar to navigate through our predictive models and interactive analytics.")

# Load High-Level Data
@st.cache_data
def load_kpi_data():
    try:
        sales = pd.read_csv('data/cleaned/cleaned_retail.csv')
        churn = pd.read_csv('exports/week2_churn_predictions.csv')
        return sales, churn
    except Exception as e:
        st.error("Data not found. Please ensure Week 1 and 2 pipelines have been run.")
        return None, None

sales_df, churn_df = load_kpi_data()

if sales_df is not None and churn_df is not None:
    st.subheader("Global Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = sales_df['TotalPrice'].sum()
        st.markdown(f'<div class="metric-card"><div class="metric-value">${total_revenue:,.0f}</div><div class="metric-label">Total Historical Revenue</div></div>', unsafe_allow_html=True)
        
    with col2:
        total_orders = sales_df['InvoiceNo'].nunique()
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_orders:,}</div><div class="metric-label">Total Transactions</div></div>', unsafe_allow_html=True)
        
    with col3:
        total_customers = churn_df.shape[0]
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_customers:,}</div><div class="metric-label">Active Customers</div></div>', unsafe_allow_html=True)
        
    with col4:
        high_risk = churn_df[churn_df['churn_segment'] == 'High'].shape[0]
        churn_rate = (high_risk / total_customers) * 100
        st.markdown(f'<div class="metric-card"><div class="metric-value">{churn_rate:.1f}%</div><div class="metric-label">High Churn Risk Rate</div></div>', unsafe_allow_html=True)

st.divider()

st.markdown("""
### 🚀 Modules Available:
1. **Demand Forecasting (Day 16):** View future 30-day sales demand with hybrid modeling and run what-if simulations.
2. **Customer Segmentation & Churn (Day 17):** Identify high-value customers and target high-risk churners.

*Project built for the Zidio Data Science 28-Days Execution Plan.*
""")
