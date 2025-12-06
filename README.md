# Customer Retention Intelligence: End-to-End Cloud Data Pipeline
Scalable Big Data Analytics & Churn Prediction using AWS, PySpark, and Power BI

## Executive Summary

The Business Challenge: Customer attrition (churn) is a critical revenue leak for banking institutions. The goal of this project was to move beyond simple analysis and engineer a scalable, cloud-native data pipeline capable of ingesting raw customer data, processing it at scale, and deploying a predictive model to identify at-risk clients.

The Solution: I architected an end-to-end pipeline using AWS S3 for storage, EC2/PySpark for distributed processing, and Amazon SageMaker for automated machine learning.

## Key Results:

Predictive Performance: Achieved an AUC-ROC of 0.87 and Accuracy of 82.8% in predicting customer churn.

Business Insight: Identified that inactive members account for 63.9% of all churned customers, marking engagement as the #1 retention metric.

Scalability: The pipeline is designed to handle distributed data processing, decoupled from local memory constraints.

## Data Source & Description

Dataset: Bank Customer Churn Modelling
Volume: 10,000 Records | 14 Attributes

To simulate a real-world banking scenario, I selected a dataset containing a mix of static demographic data and dynamic financial behaviors. Unique identifiers include CustomerId and Surname, while core demographic data covers Geography, Gender, and Age. Financial health is represented by CreditScore, Balance, and EstimatedSalary, alongside behavioral metrics such as Tenure, NumOfProducts, HasCrCard, and IsActiveMember. The target variable is Exited, making this a classic binary classification problem.






