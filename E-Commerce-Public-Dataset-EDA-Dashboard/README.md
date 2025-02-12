# E-Commerce Public Dataset EDA and Streamlit Dashboard

## Overview

This project is a data analysis and visualization dashboard built using **Streamlit**, focused on analyzing various trends in e-commerce data, including product performance, geographical sales distribution, customer behavior, and review analysis. The dashboard provides an interactive interface to explore key metrics, such as:

- **Product Performance**: Analysis of top-performing products based on sales and customer ratings.
- **Revenue Analysis**: Analysis of sales trends over time with a breakdown by months and quarters.
- **Delivery and Review Analysis**: Insights into delivery times and their correlation with customer review scores.
- **Geographical Trends**: Exploration of sales distribution and customer concentration across different states in Brazil.
- **Customer Behavior Analysis**: Exploration of customer behavior through recency, frequency, and monetary (RFM) analysis.

The data used for this analysis comes from a Brazilian e-commerce dataset that includes order, customer, payment, and geographical information.

---

## Prerequisites

To run the Streamlit dashboard locally, ensure you have the following installed:

1. **Python 3.7+**  
2. **Streamlit**  
3. **Pandas**  
4. **Matplotlib**  
5. **GeoPandas**  
6. **Folium** (optional, if map interaction is required)

### Install the required packages:

```bash
pip install streamlit pandas matplotlib geopandas folium
```

---

## Running the Dashboard

1. Clone or download the repository.
   
   ```bash
   git clone <[repository_url](https://github.com/Haniff-Toha/DataScience_Portofolio/edit/main/E-Commerce-Public-Dataset-EDA-Dashboard/)>
   ```

2. Navigate to the project directory.
   
   ```bash
   mkdir proyek_analisis_data
   cd proyek_analisis_data
   pipenv install
   pipenv shell
   pip install -r requirements.txt
   ```

3. Run the Streamlit app.

   ```bash
   streamlit run E-Commerce-public-dashboard.py
   ```

4. Open the local URL provided in the terminal (usually `http://localhost:8501`) to access the dashboard.

---

## Features

### 1. **Product Performance Analysis**
   - Displays the **Top 5 Products by Sales** and **Top 5 Products by Rating**.
   - Provides bar charts visualizing product sales and ratings, which can be filtered interactively based on a selected date range.
   - Insights on the performance of each product are shown dynamically.

### 2. **Revenue Analysis**
   - Analyzes **sales trends over time** by showing monthly and quarterly revenue breakdowns.
   - Displays total revenue by month and quarter, with shaded regions indicating the quarters.
   - Provides a comparison of sales improvements between different time periods (e.g., Jan-Aug 2017 vs. Jan-Aug 2018).
   - Allows users to filter the data by specific dates and observe how revenue trends evolve.

### 3. **Delivery Time and Review Analysis**
   - Displays charts that compare **total reviews by customer review score** and **average delivery time by review score**.
   - Highlights trends that indicate how delivery times correlate with customer ratings.
   - Interactive filtering based on review scores and time periods.

### 4. **Geographical Trends**
   - Interactive bar charts showing the **Top 5 States by Total Sales** and **Top 5 States by Customer Distribution**.
   - A geographical map visualizes sales distribution and customer concentrations across Brazil.
   - Date range filter allows users to see how the trends change over time.

### 5. **Customer Behavior Analysis**
   - **RFM Analysis**: Explores customer behavior by analyzing:
     - **Recency**: How recently a customer made a purchase.
     - **Frequency**: How often the customer makes purchases.
     - **Monetary**: The total value of purchases made by the customer.
   - Provides insights on customer segmentation and behavior patterns.
   - Visualizations help in understanding customer loyalty and value.

---

## Data Sources

The analysis is based on the following datasets:

- **Orders**: Contains information about each order, including order IDs, customer details, products, and dates.
- **Customers**: Customer details such as location and demographic information.
- **Geolocation**: Geographical data for mapping orders to regions in Brazil.
- **Payments**: Details of payment transactions for each order, including payment values.

---

## Brief Explanation of the Analysis

### Product Performance Analysis

In this section, we analyze product performance by looking at two key metrics:
- **Sales by Product**: The total sales for each product, calculated by summing the payment values of all orders for that product.
- **Customer Ratings**: The average customer ratings for each product, grouped by product category.

This section includes two bar charts:
- **Top 5 Products by Total Sales**: Shows which products have the highest sales figures.
- **Top 5 Products by Customer Ratings**: Displays the products that received the best customer ratings.

Both charts are dynamic, updating based on the selected date range.

### Revenue Analysis

The **Revenue Analysis** section provides an overview of sales trends over time:
- **Monthly Revenue**: A line chart that shows total revenue by month.
- **Quarterly Revenue**: A line chart with shaded regions indicating quarterly sales.

The section also includes a comparison of revenue performance between different periods (e.g., Jan-Aug 2017 vs. Jan-Aug 2018), highlighting any improvements or changes in sales trends.

### Delivery Time and Review Analysis

In this section, we explore the relationship between **delivery times** and **customer review scores**:
- **Total Reviews by Customer Review Score**: A bar chart that shows the total number of reviews for each score (1-5 stars).
- **Average Delivery Time by Review Score**: A bar chart displaying the average delivery time for orders, grouped by review score.

An interactive filter allows users to examine how these metrics change over different time periods.

### Geographical Trends

This section focuses on the geographical distribution of sales and customers across Brazil. It includes:
- **Top 5 States by Total Sales**: A bar chart that ranks states based on total sales revenue.
- **Top 5 States by Customer Distribution**: A bar chart that ranks states based on the number of unique customers.

Additionally, a **geographical map** is displayed using Matplotlib, which visualizes the total sales for each state using a color scale, with customer concentrations marked with red circles.

### Customer Behavior Analysis

In this section, we perform **RFM (Recency, Frequency, Monetary)** analysis to understand customer behavior:
- **Recency**: How recent a customer's last purchase was.
- **Frequency**: How often a customer makes a purchase.
- **Monetary**: The total amount of money a customer has spent.

This analysis helps in identifying customer segments, such as high-value or loyal customers, and provides insights into retention and targeting strategies. The RFM analysis can be visualized with bar charts and heatmaps.

---

## File Structure

```
.
├── dashboard              
│   ├── E-Commerce-public-dashboard.py        # Main Streamlit application
│   ├── E-Commerce-logo.png
│   ├── customers_dataset.csv
│   ├── geolocation_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── product_category_name_translation.csv
│   ├── orders_dataset.csv
│   ├── products_dataset.csv
│   └── sellers_dataset.csv
├── E-Commerce-Public-Dataset                 # Directory containing datasets
│   ├── customers_dataset.csv
│   ├── geolocation_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── product_category_name_translation.csv
│   ├── orders_dataset.csv
│   ├── products_dataset.csv
│   └──sellers_dataset.csv
├── brazil_states                # Directory for map visualization
│   ├── BRA_adm1.cpg
│   ├── BRA_adm1.csv
│   ├── BRA_adm1.dbf
│   ├── BRA_adm1.prj
│   ├── BRA_adm1.shp
│   └──BRA_adm1.shx
├── submission_MH.ipynb           #Main Notebook for Analysis
├── README.md    
└── requirements.txt     # Python package dependencies
```

---

## License

This project is licensed under the submission for Dicoding Academy