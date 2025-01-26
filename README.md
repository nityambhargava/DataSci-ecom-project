# **Customer Clustering and Insights Analysis**

## NOTE: 
The inferences and analysis made by through the visualizations is located in ./reports/Analysis-data-sci-project

## **Project Overview**  
This project focuses on analyzing customer similarity data, conducting exploratory data analysis (EDA), and clustering customers using the K-means algorithm. The primary objective is to derive actionable business insights from customer segmentation and regional patterns to improve business strategies.  

---

## **Table of Contents**  
- [Introduction](#introduction)  
- [Data Description](#data-description)  
- [Approach and Methodology](#approach-and-methodology)  
  - [1. Exploratory Data Analysis (EDA)](#1-exploratory-data-analysis-eda)  
  - [2. Clustering Analysis](#2-clustering-analysis)  
  - [3. Visualization](#3-visualization)  
- [Insights Derived](#insights-derived)  
- [Results](#results)  
- [Dependencies](#dependencies)  
- [How to Run](#how-to-run)  
- [Conclusion](#conclusion)  

---

## **Introduction**  
Understanding customer behavior through clustering and segmentation enables businesses to identify key patterns and optimize marketing strategies. This project leverages customer similarity scores and regional data to:  
1. Perform clustering using K-means.  
2. Analyze regional distribution of customers.  
3. Extract insights to support targeted marketing and sales strategies.  

---

## **Data Description**  
The dataset includes customer IDs, similarity scores, and regions. Key columns:  
- **CustomerID**: Unique identifier for customers.  
- **SimilarCustomer1, Score1**: Closest similar customer and corresponding similarity score.  
- **SimilarCustomer2, Score2**: Second closest similar customer and corresponding score.  
- **SimilarCustomer3, Score3**: Third closest similar customer and corresponding score.  
- **Region**: Geographical region of the customer.  

---

## **Approach and Methodology**

### **1. Exploratory Data Analysis (EDA)**  
- Analyzed the distribution of customers across different regions.  
- Visualized the percentage and count of customers by region using bar plots.  

### **2. Clustering Analysis**  
- Applied the **K-means algorithm** to segment customers based on similarity scores.  
- Determined the optimal number of clusters using the **Elbow Method** (based on inertia values).  

### **3. Visualization**  
- **Regional Analysis**: Bar charts to show customer distribution by region.  
- **Cluster Visualization**: Scatter plots for cluster assignment.  

---

## **Insights Derived**  
1. **High Customer Concentration in South America**: South America has the largest share of customers (30%).  
2. **Market Expansion Opportunity in Asia**: Asia has the lowest percentage, indicating potential for growth.  
3. **Distinct Clusters**: Clustering shows clear customer groupings based on similarity, aiding personalized marketing strategies.  
4. **Balanced Distribution in Europe and North America**: These regions exhibit steady engagement, suggesting robust customer bases.  
5. **Strategic Prioritization**: The high number of customers in South America can be leveraged for upselling and targeted campaigns.  

---

## **Results**  
- **Optimal Clusters**: Identified using the Elbow Method.  
- **Customer Segmentation**: Customers grouped into meaningful clusters based on similarity scores.  
- **Regional Analysis**: Insights revealed potential growth areas (Asia) and key market strengths (South America).  

---

## **Dependencies**  
Ensure the following libraries are installed before running the project:  

```bash
pip install pandas matplotlib seaborn scikit-learn
```  

---

## **How to Run**

1. Clone this repository:  
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```  

2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Run the **EDA script** to explore the data and visualize insights:  
   ```bash
   python EDA.py
   ```  

4. Execute the **Clustering script** to perform customer segmentation:  
   ```bash
   python Clustering.py
   ```  

5. Check the generated visualizations for insights and cluster details.  

---

## **Conclusion**  
This project highlights how clustering and regional analysis can inform business decisions. By identifying key markets and understanding customer patterns, companies can allocate resources more effectively and design tailored strategies for customer engagement and growth.

For questions, suggestions, or feedback, please feel free to open an issue or submit a pull request.  

---  

### **Sample Visualizations**  
1. Percentage of customers by region:

 
![image](https://github.com/user-attachments/assets/50ad5e6f-64be-4a19-9647-fd0702be2568)

2. Correlation Matrix:

![image](https://github.com/user-attachments/assets/dfcb624e-8c2f-4d78-b89d-9b38bb56b4d5)

3. Clustering graphs:

![image](https://github.com/user-attachments/assets/5004ecf9-c2f2-4bc5-a3a9-569f2b1cdb28)

---
