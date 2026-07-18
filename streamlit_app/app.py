import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="UPI Growth Dashboard", layout="wide")
df = pd.read_csv("../data/upi_features.csv", parse_dates=["date"])

st.title("UPI Growth & Digital Payment Behavior Dashboard")

# Sidebar filters
years = st.sidebar.multiselect("Select Year(s)", sorted(df["year"].unique()), default=sorted(df["year"].unique()))
df_filtered = df[df["year"].isin(years)]

# KPI row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Volume (Mn)", f"{df_filtered['txn_volume_mn'].sum():,.0f}")
col2.metric("Total Value (₹ Cr)", f"{df_filtered['txn_value_cr'].sum():,.0f}")
col3.metric("Avg Txn Value (₹)", f"{df_filtered['avg_txn_value_rs'].mean():,.0f}")
col4.metric("Banks Live (latest)", int(df_filtered['banks_live'].iloc[-1]))

# Line chart
fig1 = px.line(df_filtered, x="date", y=["txn_volume_mn","txn_value_cr"], title="Volume & Value Over Time")
st.plotly_chart(fig1, use_container_width=True)

# Growth bar chart
fig2 = px.bar(df_filtered, x="date", y="volume_mom_%", title="Month-over-Month Volume Growth %")
st.plotly_chart(fig2, use_container_width=True)

# Banks vs volume scatter
fig3 = px.scatter(df_filtered, x="banks_live", y="txn_volume_mn", title="Banks Live vs Transaction Volume")
st.plotly_chart(fig3, use_container_width=True)

st.dataframe(df_filtered)