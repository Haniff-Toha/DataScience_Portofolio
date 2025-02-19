import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import geopandas as gpd
from matplotlib.lines import Line2D

# Load datasets (cached for performance)
@st.cache_data
def load_data():
    customers_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/customers_dataset.csv")
    geolocation_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/geolocation_dataset.csv")
    order_items_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/order_items_dataset.csv")
    order_payments_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/order_payments_dataset.csv")
    order_reviews_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/order_reviews_dataset.csv")
    orders_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/orders_dataset.csv", parse_dates=['order_purchase_timestamp', 'order_delivered_customer_date'])
    products_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/products_dataset.csv")
    product_category_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/product_category_name_translation.csv")
    sellers_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/sellers_dataset.csv")
    brazil_states = gpd.read_file("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/brazil_states/BRA_adm1.shp")
    return customers_df, geolocation_df, order_items_df, order_payments_df, order_reviews_df, orders_df, products_df, product_category_df, sellers_df, brazil_states

# Load data
customers_df, geolocation_df, order_items_df, order_payments_df, order_reviews_df, orders_df, products_df, product_category_df, sellers_df, brazil_states = load_data()

# Merge product and order item data
product_order_data = order_items_df.merge(products_df, on='product_id', how='inner')

# Merge English Translations for Categories
products_df = products_df.merge(product_category_df, on='product_category_name', how='left')
products_df['product_category_name'] = products_df['product_category_name_english'].fillna(
    products_df['product_category_name']
)

# Sidebar for navigation
with st.sidebar:
    st.image("E-Commerce-logo.png", width=200)
    st.sidebar.title("Navigation")
    analysis_type = st.sidebar.radio(
        "Select Analysis",
        ["Product Performance", "Revenue Analysis", "Delivery Times and Reviews", "Geographical Trends", "Customer Behavior"]
    )

st.title("Public E-Commerce Analysis Dashboard")

#=================================================================================================
if analysis_type == "Product Performance":
    st.header("Product Performance")
    # Add Range Date Selection
    st.sidebar.subheader("Date Range Selection")
    start_date = st.sidebar.date_input("Start Date", value=date(2017, 1, 1))
    end_date = st.sidebar.date_input("End Date", value=date(2018, 12, 31))

    # Filter data by selected date range
    filtered_orders = orders_df[
        (orders_df['order_purchase_timestamp'] >= pd.Timestamp(start_date)) &
        (orders_df['order_purchase_timestamp'] <= pd.Timestamp(end_date))
    ]
    # Merge product and order data for analysis
    product_order_data = order_items_df.merge(products_df, on='product_id', how='inner')
    filtered_data = product_order_data[product_order_data['order_id'].isin(filtered_orders['order_id'])]

    # Prepare Popularity and Revenue Data
    top_10_popularity = filtered_data['product_category_name'].value_counts().head(10).reset_index()
    top_10_popularity.columns = ['product_category_name', 'orders']

    category_revenue = filtered_data.groupby('product_category_name').agg(
        total_revenue=('price', 'sum')
    ).reset_index()

    combined_data = top_10_popularity.merge(category_revenue, on='product_category_name', how='left').fillna(0)
    combined_data = combined_data.sort_values(by='orders', ascending=False)

    # Plotly Dual-Axis Chart
    dual_fig = go.Figure()

    # Bar for Orders
    dual_fig.add_trace(go.Bar(
        x=combined_data['product_category_name'],
        y=combined_data['orders'],
        name="Number of Orders",
        marker_color='blue',
        text=combined_data['orders'],
        textposition='auto',
        yaxis="y1"
    ))

    # Line for Revenue
    dual_fig.add_trace(go.Scatter(
        x=combined_data['product_category_name'],
        y=combined_data['total_revenue'],
        name="Revenue (BRL)",
        mode='lines+markers',
        line=dict(color='red', width=2),
        text=combined_data['total_revenue'],
        textposition='top center',
        yaxis="y2"
    ))

    # Layout Adjustments
    dual_fig.update_layout(
        title="Top 10 Product Categories by Orders and Revenue",
        xaxis=dict(title="Product Category", tickangle=45),
        yaxis=dict(title="Number of Orders", showgrid=False, side="left"),
        yaxis2=dict(title="Revenue (BRL)", showgrid=False, side="right", overlaying="y"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        )
    )

    # Side-by-Side Charts for Popularity and Revenue
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 10 Categories by Popularity")
        fig_popularity = px.bar(
            top_10_popularity,
            x='product_category_name',
            y='orders',
            title="Top 10 Product Categories by Popularity",
            labels={"product_category_name": "Product Category", "orders": "Number of Orders"},
            text='orders'
        )
        fig_popularity.update_traces(textposition="outside")
        fig_popularity.update_layout(xaxis_tickangle=45)
        st.plotly_chart(fig_popularity, use_container_width=True)

    with col2:
        st.subheader("Top 10 Categories by Revenue")
        top_10_revenue = category_revenue.sort_values('total_revenue', ascending=False).head(10)
        fig_revenue = px.bar(
            top_10_revenue,
            x='product_category_name',
            y='total_revenue',
            title="Top 10 Product Categories by Revenue",
            labels={"product_category_name": "Product Category", "total_revenue": "Revenue (BRL)"},
            text='total_revenue',
            color_discrete_sequence=["green"]
        )
        fig_revenue.update_traces(texttemplate="R$ %{text:.2s}", textposition="outside")
        fig_revenue.update_layout(xaxis_tickangle=45)
        st.plotly_chart(fig_revenue, use_container_width=True)

    # Display Dual-Axis Chart
    st.subheader("Combined Orders and Revenue Chart")
    st.plotly_chart(dual_fig, use_container_width=True)


#=========================================================================================
elif analysis_type == "Revenue Analysis":
    st.header("Revenue Analysis")

    # Sidebar Date Selection
    st.sidebar.subheader("Date Range Selection")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2017-01-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2018-12-31"))

    # Filter data based on the selected date range
    revenue_data = order_items_df.merge(
        order_payments_df[['order_id', 'payment_value']], on='order_id', how='inner'
    ).merge(
        orders_df[['order_id', 'order_purchase_timestamp']], on='order_id', how='inner'
    )
    revenue_data = revenue_data[
        (revenue_data['order_purchase_timestamp'] >= pd.Timestamp(start_date)) &
        (revenue_data['order_purchase_timestamp'] <= pd.Timestamp(end_date))
    ]

    # Calculate Total Orders and Total Revenue
    total_orders = revenue_data['order_id'].nunique()
    total_revenue = revenue_data['payment_value'].sum()

    # Display Total Orders and Total Revenue
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Orders", f"{total_orders:,}")
    with col2:
        st.metric("Total Revenue (BRL)", f"R$ {total_revenue:,.2f}")

    # Monthly Revenue Calculation
    revenue_data['month'] = revenue_data['order_purchase_timestamp'].dt.to_period('M')
    monthly_revenue = revenue_data.groupby('month').agg(total_revenue=('payment_value', 'sum')).reset_index()

    # Convert 'month' to string format
    monthly_revenue['month_str'] = monthly_revenue['month'].astype(str)

    # Create Line Chart for Monthly Revenue using Plotly Express
    fig_revenue = px.line(
        monthly_revenue,
        x="month_str",  # Use the string representation of the month
        y="total_revenue",
        title="Monthly Revenue",
        labels={"month_str": "Month", "total_revenue": "Total Revenue (BRL)"}
    )

    st.plotly_chart(fig_revenue, use_container_width=True)

    # All-Time Revenue Trends with Quarterly Shading
    st.subheader("All-Time Revenue Trends (Fixed)")

    # Create year, quarter, and month columns
    all_revenue_data = order_items_df.merge(
        order_payments_df[['order_id', 'payment_value']], on='order_id', how='inner'
    ).merge(
        orders_df[['order_id', 'order_purchase_timestamp']], on='order_id', how='inner'
    )
    all_revenue_data['year'] = all_revenue_data['order_purchase_timestamp'].dt.year
    all_revenue_data['quarter'] = all_revenue_data['order_purchase_timestamp'].dt.quarter
    all_revenue_data['month'] = all_revenue_data['order_purchase_timestamp'].dt.month

    # Quarterly and Monthly Revenue Calculation
    revenue_quarterly = (
        all_revenue_data.groupby(['year', 'quarter'])['payment_value']
        .sum()
        .reset_index()
        .sort_values(['year', 'quarter'])
    )
    revenue_quarterly['Year-Quarter'] = (
        revenue_quarterly['year'].astype(str) + " Q" + revenue_quarterly['quarter'].astype(str)
    )
    revenue_monthly = (
        all_revenue_data.groupby(['year', 'month'])['payment_value']
        .sum()
        .reset_index()
        .sort_values(['year', 'month'])
    )
    revenue_monthly['Year-Month'] = (
        revenue_monthly['year'].astype(str) + "-" + revenue_monthly['month'].astype(str).str.zfill(2)
    )

    # Matplotlib Plot for Fixed All-Time Trends
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(
        revenue_monthly['Year-Month'], revenue_monthly['payment_value'],
        marker='o', linestyle='dashed', label="Monthly Revenue"
    )

    # Quarterly Shading
    quarter_colors = ['skyblue', 'lightgreen', 'lightcoral', 'red']
    for i, row in revenue_quarterly.iterrows():
        year, quarter = row['year'], row['quarter']
        start_month = (quarter - 1) * 3 + 1
        end_month = start_month + 2
        quarter_data = revenue_monthly[
            (revenue_monthly['year'] == year) &
            (revenue_monthly['month'] >= start_month) &
            (revenue_monthly['month'] <= end_month)
        ]
        if not quarter_data.empty:
            ax.fill_between(
                quarter_data['Year-Month'], 0, quarter_data['payment_value'],
                color=quarter_colors[quarter - 1], alpha=0.3
            )
            ax.text(
                quarter_data['Year-Month'].iloc[len(quarter_data) // 2],
                quarter_data['payment_value'].max() * 0.5,
                f"Q{quarter}-{year}",
                color='black', fontsize=10, ha='center', va='center'
            )

    # Formatting and Legend
    ax.set_title("Revenue Trends (All-Time)", fontsize=16)
    ax.set_xlabel("Year-Month", fontsize=12)
    ax.set_ylabel("Total Revenue (BRL)", fontsize=12)
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Revenue Improvement Calculation
    jan_aug_2017 = all_revenue_data[
        (all_revenue_data['order_purchase_timestamp'].dt.year == 2017) &
        (all_revenue_data['order_purchase_timestamp'].dt.month <= 8)
    ]['payment_value'].sum()
    jan_aug_2018 = all_revenue_data[
        (all_revenue_data['order_purchase_timestamp'].dt.year == 2018) &
        (all_revenue_data['order_purchase_timestamp'].dt.month <= 8)
    ]['payment_value'].sum()
    improvement = ((jan_aug_2018 - jan_aug_2017) / jan_aug_2017) * 100 if jan_aug_2017 != 0 else 0

    st.metric("**Revenue Improvement (Q1,Q2,Q3 2017 vs. Q1,Q2,Q3 2018):**", f"{improvement:.2f}%")



#=======================================================================================
elif analysis_type == "Delivery Times and Reviews":
  st.header("Delivery Times and Review Analysis")

  # Sidebar Date Selection
  st.sidebar.subheader("Date Range Selection")
  start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2017-01-01"))
  end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2018-12-31"))

  # Filter data based on the selected date range
  orders_delivery_review_df = orders_df.merge(order_reviews_df, on='order_id', how='left')
  orders_delivery_review_df['delivery_time'] = (
      orders_delivery_review_df['order_delivered_customer_date'] -
      orders_delivery_review_df['order_purchase_timestamp']
  ).dt.days

  filtered_data = orders_delivery_review_df[
      (orders_delivery_review_df['order_purchase_timestamp'] >= pd.Timestamp(start_date)) &
      (orders_delivery_review_df['order_purchase_timestamp'] <= pd.Timestamp(end_date))
  ]

  # Metrics: Total Reviews and Average Delivery Time
  total_reviews = filtered_data['order_id'].nunique()
  avg_delivery_time = filtered_data['delivery_time'].mean()

  col1, col2 = st.columns(2)
  with col1:
      st.metric("Total Reviews", f"{total_reviews:,}")
  with col2:
      st.metric("Average Delivery Time", f"{avg_delivery_time:.2f} days")

  # Total Reviews by Review Score
  total_score = filtered_data.groupby('review_score')['order_id'].count().reset_index()
  fig_reviews = px.bar(total_score, 
                       x='review_score', y='order_id', 
                       title='Total Reviews by Review Score',
                       text='order_id'
                       )

  # Average Delivery Time by Review Score
  avg_delivery_by_score = filtered_data.groupby('review_score')['delivery_time'].mean().reset_index()
  fig_delivery_time = px.bar(avg_delivery_by_score, 
                             x='review_score', y='delivery_time', 
                             title='Average Delivery Time by Review Score', 
                             color_discrete_sequence=["lightgreen"],
                             text='delivery_time'
                             )
  fig_delivery_time.update_traces(texttemplate="%{text:.2s} days", textposition="outside")

  # Display both charts side-by-side
  col1, col2 = st.columns(2)
  with col1:
      st.plotly_chart(fig_reviews, use_container_width=True)
  with col2:
      st.plotly_chart(fig_delivery_time, use_container_width=True)


#================================================================================================
elif analysis_type == "Geographical Trends":
    st.header("Geographical Trends")

    # Date range input for filtering
    start_date = st.date_input("Start Date", value=pd.to_datetime("2017-01-01"))
    end_date = st.date_input("End Date", value=pd.to_datetime("2022-12-31"))

    # Merge customers and orders data
    customer_order = orders_df.merge(customers_df, on="customer_id", how="left")
    geographical_customer_order_df = customer_order.merge(
        geolocation_df, 
        left_on="customer_zip_code_prefix", 
        right_on="geolocation_zip_code_prefix", 
        how="left"
    )
    geographical_customer_order_df = geographical_customer_order_df.merge(
        order_payments_df[['order_id', 'payment_value']], 
        on="order_id", 
        how="left"
    )

    # Filter the data based on the selected date range
    geographical_customer_order_df['order_purchase_timestamp'] = pd.to_datetime(geographical_customer_order_df['order_purchase_timestamp'])
    filtered_data = geographical_customer_order_df[
        (geographical_customer_order_df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) & 
        (geographical_customer_order_df['order_purchase_timestamp'] <= pd.to_datetime(end_date))
    ]

    # Group by state for total sales
    state_sales = filtered_data.groupby("customer_state")["payment_value"].sum().reset_index()

    # Group by state for customer distribution
    state_customers = filtered_data.groupby("customer_state")["customer_id"].nunique().reset_index()

    # Merge sales and customer data for top states analysis
    top_states_sales = state_sales.nlargest(5, 'payment_value')
    top_states_customers = state_customers.nlargest(5, 'customer_id')

    # Plotting the bar charts side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Total Sales by State
    ax1.bar(top_states_sales['customer_state'], top_states_sales['payment_value'], color='skyblue')
    ax1.set_title("Top 5 States by Total Sales")
    ax1.set_xlabel("State")
    ax1.set_ylabel("Total Sales (BRL)")
    for i, value in enumerate(top_states_sales['payment_value']):
        ax1.text(i, value + 1000000, f"{value:,.2f}", ha='center', fontsize=10)

    # Customer Distribution by State
    ax2.bar(top_states_customers['customer_state'], top_states_customers['customer_id'], color='lightgreen')
    ax2.set_title("Top 5 States by Customer Distribution")
    ax2.set_xlabel("State")
    ax2.set_ylabel("Customer Count")
    for i, value in enumerate(top_states_customers['customer_id']):
        ax2.text(i, value + 100, f"{value:,}", ha='center', fontsize=10)

    # Display charts side by side
    st.pyplot(fig)

    # Prepare for Map Visualization using Matplotlib
    # Extract state code correctly from shapefile
    brazil_states["state_code"] = brazil_states["HASC_1"].apply(lambda x: x.split(".")[-1])

    # Merge shapefile data with sales data
    brazil_map_data = brazil_states.merge(
        state_sales, 
        left_on="state_code", 
        right_on="customer_state", 
        how="left"
    )

    # Handle missing data (fill NaNs)
    brazil_map_data["payment_value"] = brazil_map_data["payment_value"].fillna(0)

    # Create the map using Matplotlib
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    # Plot the states with total sales as the color scale
    brazil_map_data.plot(
        column='payment_value',
        cmap='YlGnBu',
        linewidth=0.8,
        ax=ax,
        edgecolor='0.8',
        legend=True,
        legend_kwds={'label': "Total Sales (BRL)", 'orientation': "vertical"}
    )

    # Add state centroids with markers for customer distribution
    for _, row in brazil_map_data.iterrows():
        if row['geometry'] is not None:  # Skip missing geometries
            ax.text(
                row['geometry'].centroid.x,
                row['geometry'].centroid.y,
                row['state_code'],
                fontsize=8,
                ha='center',
                color='black',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.6)
            )
            ax.scatter(
                row['geometry'].centroid.x,
                row['geometry'].centroid.y,
                s=row['payment_value'] / 1000000,  # Adjust marker size based on total sales
                color='red',
                alpha=0.6
            )

    # Add titles and labels
    ax.set_title("Geographical Distribution of Sales and Customers in Brazil", fontsize=16)
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Customer Distribution',
            markerfacecolor='red', markersize=10, alpha=0.6)
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=10, title="Legend")
    ax.axis('off')  # Turn off the axes

    # Show the map
    st.pyplot(fig)


#========================================================================================================
elif analysis_type == "Customer Behavior":
    st.header("Customer Behavior (RFM Analysis)")

    # Sidebar Date Range Selection
    st.sidebar.subheader("Date Range Selection")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2017-01-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2018-12-31"))

    # Merge data for RFM analysis
    rfm_df = orders_df.merge(order_payments_df[['order_id', 'payment_value']], on='order_id', how='inner')
    rfm_df = rfm_df.groupby(by="customer_id", as_index=False).agg({
        "order_purchase_timestamp": "max",
        "order_id": "nunique",
        "payment_value": "sum"
    })
    rfm_df.columns = ["customer_id", "last_purchase", "frequency", "monetary"]
    
    # Filter RFM data based on selected date range
    rfm_df = rfm_df[rfm_df['last_purchase'] >= pd.Timestamp(start_date)]
    rfm_df = rfm_df[rfm_df['last_purchase'] <= pd.Timestamp(end_date)]
    
    rfm_df['recency'] = (orders_df['order_purchase_timestamp'].max() - rfm_df['last_purchase']).dt.days

    st.dataframe(rfm_df)
    st.subheader("Best Customers Based on RFM Parameters")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_recency = round(rfm_df.recency.mean(), 1)
        st.metric("Average Recency (days)", value=avg_recency)
    
    with col2:
        avg_frequency = round(rfm_df.frequency.mean(), 2)
        st.metric("Average Frequency", value=avg_frequency)
    
    with col3:
        avg_monetary = format_currency(rfm_df.monetary.mean(), "BRL", locale='es_CO') 
        st.metric("Average Monetary", value=avg_monetary)

      # Create separate bar charts for Recency, Frequency, and Monetary
    fig_recency = px.bar(
        rfm_df.sort_values(by="recency", ascending=True).head(10),
        x="customer_id",
        y="recency",
        title="Recency (Days)",
        color_discrete_sequence=["lightblue"],
        height=650
    )

    fig_frequency = px.bar(
        rfm_df.sort_values(by="frequency", ascending=False).head(10),
        x="customer_id",
        y="frequency",
        title="Frequency",
        color_discrete_sequence=["lightblue"],
        height=650
    )

    fig_monetary = px.bar(
        rfm_df.sort_values(by="monetary", ascending=False).head(10),
        x="customer_id",
        y="monetary",
        title="Monetary Value",
        color_discrete_sequence=["lightblue"],
        height=650
    )

    # Display the RFM charts side-by-side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.plotly_chart(fig_recency, use_container_width=True)
    with col2:
        st.plotly_chart(fig_frequency, use_container_width=True)
    with col3:
        st.plotly_chart(fig_monetary, use_container_width=True)

