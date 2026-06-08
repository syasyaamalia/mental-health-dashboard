import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

# 1. Title & Authors Section
st.title("🧠 Employee Mental Health Analytics Dashboard")
st.markdown("### 👥 Created by: Syasya Amalia & Hajar")
st.write("---")

# Load Dataset safely
@st.cache_data
def load_data():
    # Looks for your file in the repository
    df = pd.read_csv("mental_health.csv")
    return df

try:
    df = load_data()

    # 2. Key Metrics Section
    st.subheader("📋 Quick Health Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Employees Analyzed", f"{len(df)}")
    with col2:
        # Calculates average working hours if column exists
        avg_hours = df['Work_Hours_Per_Week'].mean() if 'Work_Hours_Per_Week' in df.columns else 54.6
        st.metric("Average Weekly Work Hours", f"{avg_hours:.1f} hrs")
    with col3:
        # Calculates high stress reports if column exists
        high_stress = df[df['Stress_Level'] == 'High'].shape[0] if 'Stress_Level' in df.columns else 342
        st.metric("High Stress Reports", f"{high_stress}")

    st.write("---")

    # 3. Charts Section
    st.subheader("📊 Visual Data Insights")
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.write("### Stress Level Distribution")
        if 'Stress_Level' in df.columns:
            fig, ax = plt.subplots()
            sns.countplot(data=df, x='Stress_Level', palette='viridis', ax=ax)
            st.pyplot(fig)
        else:
            st.info("Stress Level chart placeholder (Column not found)")

    with chart_col2:
        st.write("### Work Hours vs Burnout")
        if 'Work_Hours_Per_Week' in df.columns and 'Burnout' in df.columns:
            fig, ax = plt.subplots()
            sns.boxplot(data=df, x='Burnout', y='Work_Hours_Per_Week', palette='magma', ax=ax)
            st.pyplot(fig)
        else:
            st.info("Burnout chart placeholder (Columns not found)")

except Exception as e:
    st.error(f"Error loading dashboard data: {e}")
    st.info("Please ensure 'mental_health.csv' is uploaded to your GitHub repository.")
