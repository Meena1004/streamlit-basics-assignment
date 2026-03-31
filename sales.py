import streamlit as st
import pandas as pd

st.title("Sales Summary Dashboard")
st.subheader("Filter sales data by category and view trends")
data = {
    "Product": ["Laptop", "Shirt", "Mobile", "Pants", "Tablet"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 2000, 30000, 2500, 15000]
}
df=pd.DataFrame(data)
st.sidebar.title("Filter option")
category=st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)
filter_data=df[df["Category"]==category]
st.write("Showing data for: ",category)
st.dataframe(filter_data)
st.line_chart(filter_data["Sales"])