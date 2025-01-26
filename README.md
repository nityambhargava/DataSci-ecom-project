Customer Clustering and Insights Analysis
Project Overview
This project aims to analyze customer similarity data, perform exploratory data analysis (EDA), and cluster customers based on their similarity scores using K-means clustering. The primary goal is to derive actionable business insights from the clustering results and regional customer distribution patterns.

Table of Contents
Introduction
Data Description
Approach and Methodology
Analysis and Insights
Results
Dependencies
How to Run the Project
Conclusion
Introduction
In this project, customer similarity scores were analyzed to segment customers into distinct clusters, identify key patterns, and extract actionable business insights. This segmentation provides valuable inputs for targeted marketing strategies and enhances customer satisfaction.

Data Description
The dataset contains customer IDs and their similarity scores with three other customers, along with regions. Key columns include:

CustomerID
SimilarCustomer1, Score1
SimilarCustomer2, Score2
SimilarCustomer3, Score3
Region
Approach and Methodology
1. Exploratory Data Analysis (EDA)
Analyzed the regional distribution of customers to understand geographical segmentation.
Visualized customer percentages and counts by region.
2. Clustering Analysis
Used the K-means clustering algorithm to segment customers based on similarity scores.
Identified the optimal number of clusters using the Elbow Method, plotted for interpretability.
3. Visualization
Bar charts for regional analysis.
Scatterplots and cluster assignments for similarity-based clustering.
Tools and Libraries
Python, Pandas, Matplotlib, Seaborn, Scikit-learn
Analysis and Insights
Customer Concentration: South America has the highest proportion of customers (30%).
Market Opportunities: Asia has the lowest percentage, highlighting potential for expansion.
Cluster Patterns: Clusters indicate distinct customer similarity groupings, providing scope for tailored marketing strategies.
Regional Strengths: Europe and North America exhibit balanced distribution, suggesting steady engagement.
Customer Engagement: High customer numbers in South America can drive stronger sales strategies.
Results
Optimal number of clusters: Determined through the Elbow Method.
Clear customer segmentation based on similarity scores.
Regional analysis revealed South America as a key market and Asia as an area of opportunity.
Dependencies
Python 3.x
Required Libraries:
bash
Copy
Edit
pip install pandas matplotlib seaborn scikit-learn
How to Run the Project
Clone this repository:
bash
Copy
Edit
git clone <repository_url>
cd <repository_folder>
Install dependencies as listed above.
Run the EDA file for exploratory analysis and insights:
bash
Copy
Edit
python EDA.py
Execute the clustering file to perform K-means clustering:
bash
Copy
Edit
python Clustering.py
View results and insights from the generated visualizations and outputs.
Conclusion
This project highlights the importance of customer segmentation and regional analysis for driving targeted marketing and business strategies. The clustering approach provides a structured methodology for understanding customer behavior and optimizing resource allocation.

For any questions or suggestions, feel free to open an issue or contact us.
