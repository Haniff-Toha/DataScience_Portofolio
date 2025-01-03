# Haniff's Data Science Portfolio

<p>👋😁 Hello! I'm Haniff, a Wanna Be Data Scientist, passionate about solving real-world problems through data. My curiosity and enthusiasm for data-driven technologies have grown stronger, and I'm on a mission to leverage data to make informed decisions and drive meaning and impactful change in this dynamic and evolving field.</p>


-------------------
> Full Documentation provide end-to-end Data Science Flow

> In this portofolio I've already done:
* Predictive Analysis
* Recomendation System
* NLP
* Dashboarding
-------------------

## [📌Loan Risk Profiling Based on Customer Behaviors](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Loan%20Risk%20Profiling%20Based%20on%20Customer%20Behaviors)

[![Full Documentaion!](https://img.shields.io/badge/Full-Documentation-1abc9c.svg)](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Loan%20Risk%20Profiling%20Based%20on%20Customer%20Behaviors)

<p>Insight Co. Ltd. is a rapidly growing fintech company that provides loan services that helps people from all levels get the funds they need and make fortune from interest rates. As the company continues to expand, this company face the challenge of a rising number of loan applications, which has led to time-consuming and costly assessments by our team. Also this company had default rate of 12.3%, which needs to minimize the risks for maintaining the stability of company's cash flow.</p>

### Business understanding
- *Problem*
  - Company must have a sophisticated system in place to proactively identify and assess potential Non Performing Loan Customers by utilizing cutting-edge predictive analytics and risk assessment tools.
- *Goals and Objective*
  - Build a model that help assessment team to assess loan applicant.
  - With historical data, the model could set a new standard for performing loan and non performing loan customer.

### Solution 
- We develop a model to classify Non Performing and Performing loan customer, and also a scorecard based on feature to give a credit scoring for company's loan applicants.
- We suggest the business flow as Partial Auto-reject & Auto-approve.

### _Business Recomendation_
Based on our Exploratory Data Analysis;
- We suggest the company to expanding the business to cities with high scorecard values.
- Conducting a campaign for performing loan customers based on the criteria obtained from the EDA (Exploratory Data Analysis).

---------------------------
## 📌[Improving Employee Retention by Predicting Employee Attrition Using ML](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/HR%20Employee%20Attrition%20Analysis%20and%20Prediction)
[![Full Documentaion!](https://img.shields.io/badge/Full-Documentation-1abc9c.svg)](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Improving%20Employee%20Retention%20by%20Predicting%20Employee%20Attrition%20Using%20ML)

<p>Employee attrition is a significant concern for organizations, leading to increased recruitment and training costs, as well as disruptions in workforce stability. This project employs machine learning techniques to address the challenge by accurately predicting employee attrition, identifying key factors influencing it, and providing actionable recommendations for enhancing retention strategies.</p>

### Business Understanding
- *Problem*
  - Employee attrition is a major challenge for organizations, leading to increased recruitment costs, loss of expertise, and workplace disruption. Proactively identifying employees at risk of leaving and understanding the reasons for attrition are critical for designing effective retention strategies.  

- *Goals and Objectives*: 
This project aims to address employee attrition using data-driven insights and predictive analytics by:
  - Identifying employees at risk of leaving through predictive modeling.  
  - Uncovering key factors contributing to attrition using exploratory data analysis (EDA).  
  - Providing actionable recommendations to reduce turnover and improve retention.  
  - Quantifying the financial impact of attrition and demonstrating cost-saving opportunities.  
  - Integrating predictive solutions into HR workflows for real-time monitoring and intervention.  

### **Solution: Key Insights and Recommendations**

### **1. Model Performance**  
The **CatBoost** model was identified as the best-performing algorithm, balancing the trade-offs between minimizing **False Negatives (FN)** and **False Positives (FP)**. This ensures accurate identification of high-risk employees while avoiding unnecessary interventions.

- **Confusion Matrix for CatBoost**  
  ![Confusion Matrix](HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/cm_catboost.png)

- **Model Comparison**  
  ![Model Comparison](HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/algoritma_comp.png)

### **2. Feature Importance**  
Using **SHAP (SHapley Additive exPlanations)** values, the most influential factors driving attrition were identified:

- **StockOptionLevel**: Lower levels correlate with higher attrition, emphasizing the importance of equity incentives.
- **JobLevel**: Higher job levels show reduced attrition, possibly due to better compensation or responsibilities.
- **Overtime**: Employees with frequent overtime are at higher risk, indicating the need for workload management.
- **WorkLifeBalance**: Poor work-life balance strongly predicts attrition, underscoring its role in employee satisfaction.

- **SHAP Analysis Visualization**  
  ![SHAP Values](HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/shap_cb.png)

### **3. Exploratory Data Analysis Insights**

#### **Career Development**
- Majority of employees are at **Entry Level** and **Junior Level**, with attrition rates of **26.3%** and **14.7%**, respectively.
- **Recommendation**:
  - Structured career pathways.
  - Performance-based incentives and rotational opportunities.  

  ![Attrition by Job Level](HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/eda_attrition_joblevel.png)

---

#### **Work-Life Balance**
- Overtime and poor work-life balance are significant attrition drivers.
- **Recommendation**:
  - Reduce overtime by distributing workload evenly.
  - Offer flexible work schedules and remote options.

  ![Overtime and Work-Life Balance](HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/eda_attrition_ovt_wlb.png)


#### **Compensation and Stock Options**

<div style="display: flex; justify-content: space-between; align-items: center;">
    <img src="HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/eda_attrition_income.png" alt="Attrition by Monthly Income" style="width: 45%;"/>
    <img src="HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/eda_attrition_stock.png" alt="Stock Option Levels" style="width: 53%;"/>
</div>

- Employees with lower monthly income and stock option levels exhibit higher attrition.
- **Recommendation**:
  - Competitive salary adjustments.
  - Expand stock option programs to entry and junior-level employees.

### **Future Directions**
![Rekomendasi Implementasi Model](HR%20Employee%20Attrition%20Analysis%20and%20Prediction/predictive_analysis_image/implement_recom.png)
1. **Predictive Analytics Integration**:
   - Implement the CatBoost model into HR workflows for real-time monitoring.
   - Develop a dashboard to track and visualize trends.

2. **Model Maintenance**: Periodic retraining to adapt to changing organizational dynamics.

3. **Continuous Evaluation**: Regularly assess the effectiveness of implemented retention strategies.

### **Impact**
By addressing key attrition drivers and implementing data-driven HR policies, the organization can:
- Achieve a more stable and engaged workforce.
- Reduce turnover costs.
- Foster a supportive and productive work environment.


--------------------------
## 📌[Indonesian Farmer's E-Commerce Product Recommendation System](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Product%20Recommendation%20System)
[![Full Documentaion!](https://img.shields.io/badge/Full-Documentation-1abc9c.svg)](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Product%20Recommendation%20System)

<p>E-commerce has become the backbone of the digital economy, but with the increasing number of product choices, customers often feel overwhelmed in finding what they need. This recommendation system project aims to address this challenge by offering relevant product suggestions based on user preferences, enhancing the overall shopping experience. Recommendation systems have become a crucial component across industries, especially in e-commerce, to help customers navigate the vast array of options available. This project is significant as it enables personalized user experiences, which can ultimately improve customer satisfaction, retention, and company revenue. Research has shown that recommendation systems can boost sales conversions, and by leveraging available data, companies can gain better insights into customer behavior.</p>

### Business Understanding
#### Problem
- **Challenge**: In the e-commerce industry, customers often face difficulties in finding products relevant to their preferences due to the overwhelming number of choices.
- **Business Need**: Develop a recommendation system to enhance user experience by suggesting relevant products and increase sales conversions.

#### Goals and Objectives
- **Accurate Product Recommendations**: Develop a system that provides accurate product recommendations.
- **Personalization**: Utilize content-based filtering and collaborative filtering to create personalized experiences.
- **Performance Evaluation**: Evaluate the system's effectiveness with appropriate metrics like MAE, MSE, and Precision@K.


### Solution

The project employs **two recommendation techniques**:

1. **Content-Based Filtering**: 
   - Focuses on product attributes like descriptions, categories, and features.
   - Uses **Cosine Similarity** to calculate similarity between products.

2. **Collaborative Filtering**:
   - Uses **user-item interaction data** (e.g., reviews, ratings) to make recommendations based on patterns and similarities between users and products.
   - Implemented using **Singular Value Decomposition (SVD)**.

### Key Findings & Visualizations

#### **Univariate Analysis**:

##### 1. **Rating Distribution**: 
- **Key Insight**: Most products have a high average rating (close to 5 stars), indicating customer satisfaction. The dataset shows skewness towards higher ratings.
  
- **Visualization**: Average Rating Distribution for Products
  ![Average Rating Distribution](Product%20Recommendation%20System/product_recommendation_image/eda_uni_prod_rat.png)

##### 2. **Product Category Distribution**:
- **Key Insight**: Categories like "Alat dan Mesin Pertanian" (Agricultural Tools) are the most frequent, highlighting high demand in the agricultural sector.
  
- **Visualization**: Product Category Distribution
  ![Product Category Distribution](Product%20Recommendation%20System/product_recommendation_image/eda_uni_prod_cat.png)

#### **User Reviews Analysis**:

##### 1. **User Ratings Distribution**:
- **Key Insight**: **Rating 5** is the most common, with a significant number of 2-star ratings indicating dissatisfaction. Few extreme low ratings (1-star), suggesting most users are either satisfied or moderately dissatisfied.

- **Visualization**: User Rating Distribution
  ![User Rating Distribution](Product%20Recommendation%20System/product_recommendation_image/eda_uni_user_rat.png)

##### 2. **Popular Product Categories**:
- **Key Insight**: **Sarana dan Peralatan Irigasi** (Irrigation Equipment) shows the highest number of reviews, indicating high demand.
  
- **Visualization**: User Category Frequency
  ![User Category Frequency](Product%20Recommendation%20System/product_recommendation_image/eda_uni_user_cat.png)

#### **Bivariate Analysis**:

##### 1. **Rating Frequency for Top 5 Products**:
- **Key Insight**: The **Alat dan Mesin Pertanian** category has a mix of high ratings (4, 5) and a significant number of moderate dissatisfaction (rating 2), showing areas for product improvement.

- **Visualization**: Rating Frequency for Top 5 Products
  ![Top Products Rating Frequency](Product%20Recommendation%20System/product_recommendation_image/eda_biv_user_top5.png)


### Business Recommendation

Based on the **Exploratory Data Analysis (EDA)**:
1. **High Demand Products**: Focus marketing efforts on highly rated and frequently sold products in categories like **Alat dan Mesin Pertanian** (Agricultural Tools) and **Sarana dan Peralatan Irigasi** (Irrigation Equipment).
2. **Improvement Areas**: Products with significant **2-star reviews** (e.g., Agricultural Equipment) should be evaluated for quality improvements or better customer service.
3. **Personalization Opportunities**: The use of collaborative filtering can lead to higher sales across diverse product categories, encouraging users to discover new product types.

### Model Evaluation

#### **Content-Based Filtering**:
- **MAE**: 0.03, **MSE**: 0.0081, **RMSE**: 0.09  
- **Precision@K**: 0.8, **NDCG@K**: 1.0  
- **Insights**: High accuracy within the same category but lacks cross-category recommendations.

#### **Collaborative Filtering** (SVD):
- **MAE**: 0.504, **MSE**: 0.703, **RMSE**: 0.838  
- **Precision@K**: 1.0, **NDCG@K**: 1.0  
- **Insights**: Can recommend products across different categories, making it more versatile for discovering new items.

#### **Model Comparison**:
- **Content-Based**: Best for **category-specific recommendations** but limited in scope.
- **Collaborative Filtering**: Better for **diverse product recommendations**, broadening user exposure across categories.

### Conclusion

This recommendation system successfully meets the goal of **personalized product recommendations**, offering users tailored experiences while increasing product discoverability. The combination of **Content-Based Filtering** and **Collaborative Filtering** provides both **accuracy** and **diversity**, allowing the system to adapt to user preferences while also promoting a range of products.

#### Key Takeaways:
- **Content-Based Filtering** offers high accuracy for recommendations within the same category.
- **Collaborative Filtering** provides a **wider scope**, making it more suitable for encouraging cross-category product discovery.


--------------------------------

## 📌[Flip (Indonesian Payment & E-Money App) Sentiment Analysis](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Flip%20(Indonesian%20Payment%20%26%20E-Money%20App)%20Sentiment%20Analysis)
[![Full Documentaion!](https://img.shields.io/badge/Full-Documentation-1abc9c.svg)](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Flip%20(Indonesian%20Payment%20%26%20E-Money%20App)%20Sentiment%20Analysis)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=Jupyter)](https://github.com/Haniff-Toha/DataScience_Portofolio/blob/main/Flip%20(Indonesian%20Payment%20%26%20E-Money%20App)%20Sentiment%20Analysis/Sentimen%20Analisis%20Flip.ipynb)

<p>Report still under develpoment - please walk through the jupyter notebook</p>

### Business understanding
- *Problem*
  - -.
- *Goals and Objective*
  - -.

### Solution 


---------------------------
## 📌 [Brazilian E-Commerce RFM Analysis, EDA, and Dashboarding](https://github.com/Haniff-Toha/DataScience_Portofolio/blob/main/E-Commerce-Public-Dataset-EDA-Dashboard)
[![Full Documentaion!](https://img.shields.io/badge/Full-Documentation-1abc9c.svg)](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/E-Commerce-Public-Dataset-EDA-Dashboard)
[![Streamlit Dashboard!](https://img.shields.io/badge/Streamlit-Dashboard-orange.svg)](https://datascienceportofolio-3tx46xtd99g9hjqskj9xau.streamlit.app/)

This project is a data analysis and visualization dashboard built using **Streamlit**, focused on analyzing various trends in e-commerce data, including product performance, geographical sales distribution, customer behavior, and review analysis. The dashboard provides an interactive interface to explore key metrics, such as:

- **Product Performance**: Analysis of top-performing products based on sales and customer ratings.
- **Revenue Analysis**: Analysis of sales trends over time with a breakdown by months and quarters.
- **Delivery and Review Analysis**: Insights into delivery times and their correlation with customer review scores.
- **Geographical Trends**: Exploration of sales distribution and customer concentration across different states in Brazil.
- **Customer Behavior Analysis**: Exploration of customer behavior through recency, frequency, and monetary (RFM) analysis.

The data used for this analysis comes from a Brazilian e-commerce dataset that includes order, customer, payment, and geographical information.

### Business Understanding
- *Problem*  
  - E-commerce companies face challenges in understanding product performance, customer behavior, and sales trends, which hinders data-driven decision-making. The lack of clear insights into geographical sales, delivery times, and review impacts further complicates strategic planning.  

- *Goals and Objectives*  
  - Provide a comprehensive analysis of e-commerce data to uncover hidden trends and patterns.  
  - Deliver actionable insights into product performance, revenue growth, and customer satisfaction.  
  - Enable businesses to make informed decisions on inventory, delivery logistics, and marketing strategies.  
  - Enhance customer segmentation using RFM analysis to improve retention and value.  

### **Solution and Key Features**  
The solution involves creating an interactive Streamlit dashboard that:  
- Visualizes key metrics such as sales, reviews, and delivery times.  
- Provides dynamic filters for exploring data trends by date range and categories.  
- Enables businesses to optimize strategies based on geographical and customer insights.

#### **1. Product Performance Analysis**  
- **Key Insights**: Displays the **Top 5 Products by Sales** and **Top 5 Products by Ratings**.  
- **Visuals**:  
  - Bar charts for sales and ratings.  
  - Interactive date range filters.  
- **Purpose**: Identifies high-performing products and areas for improvement.  

#### **2. Revenue Analysis**  
- **Key Insights**:  
  - Monthly and quarterly revenue breakdowns.  
  - Sales comparisons across time periods.  
- **Visuals**:  
  - Line charts with shaded regions for quarterly trends.  
  - Interactive filtering for date ranges.  
- **Purpose**: Tracks revenue growth and seasonal patterns.  

#### **3. Delivery Time and Review Analysis**  
- **Key Insights**:  
  - Correlation between delivery times and review scores.  
  - Trends in customer satisfaction based on delivery efficiency.  
- **Visuals**:  
  - Displays charts that compare **total reviews by customer review score** and **average delivery time by review score**.
  - Highlights trends that indicate how delivery times correlate with customer ratings.
  - Interactive filtering based on review scores and time periods. 
- **Purpose**: Improves logistics to enhance customer satisfaction.  

#### **4. Geographical Trends**  
- **Key Insights**:  
  - Top-performing states by sales and customer distribution.  
  - Visual representation of geographical trends.  
- **Visuals**:
  - Interactive bar charts showing the **Top 5 States by Total Sales** and **Top 5 States by Customer Distribution**.
  - A geographical map visualizes sales distribution and customer concentrations across Brazil.
  - Date range filter allows users to see how the trends change over time.
- **Purpose**: Enables targeted marketing and regional strategy optimization.  

#### **5. Customer Behavior Analysis**  
- **Key Insights**:  
  - **RFM Analysis**: Explores customer behavior by analyzing:
     - **Recency**: How recently a customer made a purchase.
     - **Frequency**: How often the customer makes purchases.
     - **Monetary**: The total value of purchases made by the customer.
  - Provides insights on customer segmentation and behavior patterns.
- **Visuals**:  
  - Bar Chart presenting Top 5 for most recent, most frequent, and most given valued customer
- **Purpose**: Enhances customer retention and loyalty strategies.  

--------------------------
## 📌Comming Soon (6)
[![Full Documentaion!](https://img.shields.io/badge/Full-Documentation-1abc9c.svg)](https://github.com/Haniff-Toha/DataScience_Portofolio/tree/main/Loan%20Risk%20Profiling%20Based%20on%20Customer%20Behaviors)
<p>-</p>

### Business understanding
- *Problem*
  - -.
- *Goals and Objective*
  - -.

### Solution 
- -.

### _Business Recomendation_
Based on our Exploratory Data Analysis;
- -.
