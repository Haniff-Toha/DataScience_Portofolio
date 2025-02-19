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
    customers_df = pd.read_csv("https://raw.githubusercontent.com/Haniff-Toha/DataScience_Portofolio/refs/heads/main/E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/customers_dataset.csv", sep=',')
    geolocation_df = pd.read_csv("https://raw.githubusercontent.com/Haniff-Toha/DataScience_Portofolio/refs/heads/main/E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/customers_dataset.csv", sep=',')
    order_items_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/customers_dataset.csv", sep=',')
    order_payments_df = pd.read_csv("https://raw.githubusercontent.com/Haniff-Toha/DataScience_Portofolio/refs/heads/main/E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/customers_dataset.csv", sep=',')
    order_reviews_df = pd.read_csv("https://raw.githubusercontent.com/Haniff-Toha/DataScience_Portofolio/refs/heads/main/E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/order_reviews_dataset.csv", sep=',')
    orders_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/orders_dataset.csv", sep=',', parse_dates=['order_purchase_timestamp', 'order_delivered_customer_date'])
    products_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/products_dataset.csv", sep=',')
    product_category_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/product_category_name_translation.csv", sep=',')
    sellers_df = pd.read_csv("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/sellers_dataset.csv", sep=',')
    brazil_states = gpd.read_file("E-Commerce-Public-Dataset-EDA-Dashboard/dashboard/brazil_states/BRA_adm1.shp", sep=',')
    return customers_df, geolocation_df, order_items_df, order_payments_df, order_reviews_df, orders_df, products_df, product_category_df, sellers_df, brazil_states

# Load data
customers_df, geolocation_df, order_items_df, order_payments_df, order_reviews_df, orders_df, products_df, product_category_df, sellers_df, brazil_states = load_data()

st.dataframe(customers_df)
st.dataframe(geolocation_df)
st.dataframe(order_items_df)
st.dataframe(order_payments_df)
st.dataframe(order_reviews_df)
st.dataframe(orders_df)
st.dataframe(products_df)
st.dataframe(product_category_df)
st.dataframe(sellers_df)
