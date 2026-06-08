import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Settings
st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

# Load the data file
df = pd.read_csv("mental_health.csv")

# App Title & Project Objectives
st.title("🧠 Employee Mental Health Analytics Dashboard")

# Quick Summary Numbers Section
st.subheader("📈 Quick Health Metrics")
m1, m2, m3 = st.columns(3)

with m1:
    st.metric(label="Total Employees Analyzed", value=len(df))
with m2:
    avg_hours = round(df["Work_Hours"].mean(), 1)
    st.metric(label="Average Weekly Work Hours", value=f"{avg_hours} hrs")
with m3:
    # Counts how many rows have a high stress indicator
    high_stress_count = len(df[df["Stress_Level"].astype(str).str.contains("High|Very High|4|5", case=False, na=False)])
    st.metric(label="High Stress Reports", value=high_stress_count)

st.write("---")

# Two Charts Side-by-Side
col1, col2 = st.columns(2)

with col1:
    st.subheader("💼 Mental Health Condition by Occupation")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x="Occupation", hue="Mental_Health_Condition", ax=ax, palette="Set2")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("📈 Stress Level vs Condition Severity")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x="Severity", hue="Stress_Level", ax=ax, palette="Pastel1")
    st.pyplot(fig)

st.write("---")

# Bottom Full-Width Chart
st.subheader("⏳ Work Hours vs Condition Severity Distribution")
fig, ax = plt.subplots(figsize=(12, 4))
sns.boxplot(data=df, x="Severity", y="Work_Hours", ax=ax, palette="Accent")
st.pyplot(fig)

st.write("---")

# Interactive Raw Data Explorer Table
st.subheader("📋 Explore the Raw Dataset")
st.markdown("Use the table below to scroll through, search, or filter the employee response data.")
st.dataframe(df, use_container_width=True)
