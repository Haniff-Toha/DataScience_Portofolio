# Flip Sentiment Analysis: Application Review Insights  
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=Jupyter)](https://github.com/Haniff-Toha/DataScience_Portofolio/blob/main/Flip%20(Indonesian%20Payment%20%26%20E-Money%20App)%20Sentiment%20Analysis/Sentimen%20Analisis%20Flip.ipynb)

---
## Business Understanding  
**Flip** is widely used for financial transactions, including e-money transfers, bill payments, and international remittances. As the fintech space in Indonesia grows rapidly, maintaining customer satisfaction is critical for sustaining growth and competitive advantage. User reviews serve as a valuable source of feedback for understanding customer sentiment and enhancing the app’s features and services.  

---
## Problem Statement  
Despite its popularity, **Flip** faces challenges in fully addressing user expectations. Common issues such as transaction delays, app usability concerns, and customer service experiences are often highlighted in reviews. However, these reviews are unstructured and challenging to analyze manually.  

Key challenges include:  
- Extracting meaningful insights from large volumes of unstructured text reviews.  
- Identifying specific areas where the app excels or falls short.  
- Addressing negative sentiment that could affect user retention and growth.  

---

## Project Goals and Objectives  
### Goals  
The primary goal of this project is to analyze user reviews of the Flip app and classify sentiments into **Positive**, **Neutral**, and **Negative** categories to uncover actionable insights.  

### Objectives  
1. **Sentiment Classification**: Categorize user reviews into positive, neutral, and negative sentiments based on review content.  
2. **Trend Identification**: Highlight recurring themes and trends in positive and negative reviews.  
3. **Actionable Insights**: Provide recommendations to improve customer experience and satisfaction.  
4. **Data-Driven Decision Making**: Support Flip’s product and customer service teams with insights derived from sentiment analysis.  

---

## Dataset  
- **Source**: User reviews collected from Flip's app listing on Google Play Store 
- **Features**:  
  - Review Text  
  - Review Score (0–5)  
  - Review Date  
  - Metadata (e.g., app version, device type)  
- **Size**: Approximately **10,000+ reviews** spanning multiple versions of the app.  

---
## Methodology  
1. **Data Collection**: Scraped reviews using automated tools and APIs.  
2. **Data Preprocessing**:  
   - Removed duplicates and irrelevant content.  
   - Tokenization, stopword removal, and stemming/lemmatization for Bahasa Indonesia.  
3. **Sentiment Classification**:  
   - Defined thresholds:  
     - Scores 4–5: Positive  
     - Score 3: Neutral  
     - Scores 1–2: Negative  
   - Used **machine learning models** (e.g., Logistic Regression, Naïve Bayes) and **pre-trained NLP models** (e.g., IndoBERT).  
4. **Visualization**: Created interactive dashboards to showcase sentiment trends and patterns.  

---
## Results  
### Sentiment Distribution by Labeling Method  
The project compared three methods for sentiment classification:  
1. **Lexicon Indonesia Library**  
2. **IndoBERT Pre-trained Model**  
3. **Manual Labeling Based on Review Score**  

#### Sentiment Distribution Summary:  
| Method                     | Negative | Neutral | Positive |  
|----------------------------|----------|---------|----------|  
| **Lexicon Indonesia**       | 6,964    | 2,016   | 5,281    |  
| **IndoBERT**                | 6,558    | 4,868   | 2,835    |  
| **Manual (Review Score)**   | 9,435    | 3,177   | 1,649    |  

### Key Observations  
- **Lexicon Indonesia** identified a more balanced distribution between positive and negative sentiments, with fewer neutral reviews.  
- **IndoBERT** showed a higher proportion of neutral reviews, indicating its ability to capture nuanced or ambiguous sentiments.  
- **Manual Labeling** based on review scores revealed the highest number of negative reviews. This suggests that many low ratings were directly associated with negative sentiments.  

### Insights from Sentiment Analysis  
1. **Recurring Issues in Negative Reviews**:  
   - Transaction delays  
   - Poor customer service responses  
   - App crashes or technical bugs  
2. **Highlights from Positive Reviews**:  
   - Low transaction fees  
   - Simple and user-friendly interface  
   - Reliable performance for basic transactions  

---

Here’s the updated **Predictive Modeling** section for your README file:  

---

## Predictive Modeling  

To predict the sentiment of user reviews, several machine learning models were implemented and evaluated using two different data splitting schemes (80:20 and 70:30 train-test splits). The models were evaluated based on their training and testing accuracy to assess their generalization capability.  

### Model Performance Summary  
| Model Training Scheme | Train Accuracy | Test Accuracy |  
|-------------------------------|----------------|---------------|  
| Logistic Regression (80:20)   | 0.904979       | 0.885384      |  
| Logistic Regression (70:30)   | 0.903025       | 0.875672      |  
| Support Vector Machine (80:20)| 0.952139       | 0.871714      |  
| Support Vector Machine (70:30)| 0.952815       | 0.869128      |  

### Observations  
1. **Logistic Regression**:  
   - Achieved strong generalization with high test accuracy.  
   - Shows consistent performance across both data splits.  
2. **Support Vector Machine (SVM)**:  
   - Demonstrated slightly higher training accuracy compared to Logistic Regression.  
   - Marginally lower test accuracy, indicating potential overfitting on training data.  
3. **Data Splitting Impact**:  
   - The 80:20 split generally yielded higher test accuracy, suggesting it retains a better balance between training the model and assessing its performance on unseen data.  

### Conclusion  
Logistic Regression was more robust and generalizable, making it the preferred model for this sentiment analysis task. While SVM performed better on training data, its slightly reduced test accuracy indicates overfitting.  

---
## Future Work  
1. **Topic Modeling**: Implement advanced NLP techniques like LDA to uncover hidden topics in reviews.  
2. **Sentiment by Feature**: Analyze sentiment trends based on app features (e.g., UI, customer support).  
3. **Longitudinal Analysis**: Track sentiment changes over time to assess the impact of new features or updates.  
4. **Multilingual Analysis**: Include reviews in English or other regional languages for broader insights.  
