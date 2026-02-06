import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("airbnbBerlin.csv")

# Clean Price column (if needed)
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)

st.title("🏠 Airbnb Data Dashboard")

# -------- Sidebar Filters --------
st.sidebar.header("Filters")

# Neighbourhood filter
neighbourhoods = df['neighbourhood'].dropna().unique()
selected_neighbourhood = st.sidebar.selectbox("Select Neighbourhood", neighbourhoods)

# Room type selector
room_types = df['Room Type'].dropna().unique()
selected_room = st.sidebar.selectbox("Select Room Type", room_types)

# Price range slider
min_price = int(df['Price'].min())
max_price = int(df['Price'].max())
price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))

# Apply filters
filtered_df = df[
    (df['neighbourhood'] == selected_neighbourhood) &
    (df['Room Type'] == selected_room) &
    (df['Price'] >= price_range[0]) &
    (df['Price'] <= price_range[1])
]

st.write("### Filtered Data")
st.dataframe(filtered_df)

# -------- Correlation Heatmap --------
st.write("### Correlation Heatmap")

numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
st.pyplot(plt)
