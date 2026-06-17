import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation", page_icon="👥", layout="wide")

st.title("👥 Customer Segmentation & Churn Risk")
st.markdown("Analyze customer behavior clusters and identify high-value users at risk of churning.")

@st.cache_data
def load_customer_data():
    try:
        # Load the churn predictions and RFM data
        churn = pd.read_csv('exports/week2_churn_predictions.csv')
        # Load RFM (from week 1/2) if available, otherwise just use churn features
        try:
            rfm = pd.read_csv('data/cleaned/rfm_customers.csv')
            df = pd.merge(churn, rfm[['CustomerID', 'Cluster']], on='CustomerID', how='left')
        except:
            df = churn.copy()
            df['Cluster'] = 'Unknown'
            
        return df
    except Exception as e:
        st.error(f"Could not load customer data. Error: {e}")
        return None

df = load_customer_data()

if df is not None:
    st.sidebar.header("Filter Customers")
    risk_filter = st.sidebar.multiselect("Select Churn Risk Levels:", 
                                         options=['High', 'Medium', 'Low'],
                                         default=['High', 'Medium', 'Low'])
    
    # Filter data based on selection
    filtered_df = df[df['churn_segment'].isin(risk_filter)]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Customer Monetary Value vs Recency (Colored by Risk)")
        # Scatter plot of Recency vs Monetary, colored by Churn Risk
        fig1 = px.scatter(filtered_df, x='recency', y='monetary', 
                          color='churn_segment', 
                          size='frequency',
                          hover_data=['CustomerID'],
                          color_discrete_map={'High': 'red', 'Medium': 'orange', 'Low': 'green'},
                          title="RFM Scatter Plot",
                          log_y=True)
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        st.subheader("Risk Distribution")
        risk_counts = filtered_df['churn_segment'].value_counts().reset_index()
        risk_counts.columns = ['Risk Level', 'Count']
        fig2 = px.pie(risk_counts, values='Count', names='Risk Level', 
                      color='Risk Level',
                      color_discrete_map={'High': 'red', 'Medium': 'orange', 'Low': 'green'},
                      hole=0.4)
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()
    
    st.subheader("High-Risk Retention Targets")
    st.markdown("These are the most valuable customers who are currently predicted to churn. **Action required:** Targeted retention campaigns.")
    
    # Filter high risk, sort by monetary value
    retention_targets = df[df['churn_segment'] == 'High'].sort_values('monetary', ascending=False)
    
    st.dataframe(
        retention_targets[['CustomerID', 'monetary', 'recency', 'frequency', 'churn_probability']].head(20).style.background_gradient(cmap='Reds', subset=['churn_probability']),
        use_container_width=True
    )
    
    st.download_button(
        label="Download Retention List CSV",
        data=retention_targets.to_csv(index=False).encode('utf-8'),
        file_name="high_value_retention_targets.csv",
        mime="text/csv"
    )
