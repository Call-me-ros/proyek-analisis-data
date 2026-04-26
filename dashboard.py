import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Helper function untuk menyiapkan berbagai dataframe
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='order_purchase_timestamp').agg({
        "order_id": "nunique",
        "price": "sum"
    })
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        "order_id": "order_count",
        "price": "revenue"
    }, inplace=True)
    return daily_orders_df

# 1. Load Data
all_df = pd.read_parquet("all_data.parquet")
datetime_columns = ["order_purchase_timestamp", "order_delivered_customer_date"]
all_df.sort_values(by="order_purchase_timestamp", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# 2. Membuat Sidebar untuk Filter
min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()

with st.sidebar:
    # Menambahkan logo perusahaan (opsional)
    st.title("E-Commerce Dashboard")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                (all_df["order_purchase_timestamp"] <= str(end_date))]

# 3. Menyiapkan Dataframe untuk Visualisasi
daily_orders_df = create_daily_orders_df(main_df)

# 4. Header Utama
st.header('E-Commerce Performance Dashboard')

# 5. Metrik Utama (Revenue & Orders)
col1, col2 = st.columns(2)

with col1:
    total_orders = daily_orders_df.order_count.sum()
    st.metric("Total Orders", value=total_orders)

with col2:
    total_revenue = format_currency(daily_orders_df.revenue.sum(), "BRL", locale='pt_BR') 
    st.metric("Total Revenue", value=total_revenue)

# 6. Visualisasi: Revenue per State
st.subheader("Revenue by State")
fig, ax = plt.subplots(figsize=(16, 8))
state_revenue = main_df.groupby("customer_state").price.sum().sort_values(ascending=False).reset_index()
sns.barplot(x="price", y="customer_state", data=state_revenue.head(10), palette="viridis", ax=ax)
ax.set_xlabel(None)
ax.set_ylabel(None)
st.pyplot(fig)

# 7. Visualisasi: Product Performance
st.subheader("Top Product Categories")
fig, ax = plt.subplots(figsize=(16, 8))
product_perf = main_df.groupby("product_category_name_english").order_id.nunique().sort_values(ascending=False).reset_index()
sns.barplot(x="order_id", y="product_category_name_english", data=product_perf.head(10), palette="magma", ax=ax)
ax.set_xlabel("Number of Orders")
ax.set_ylabel(None)
st.pyplot(fig)
