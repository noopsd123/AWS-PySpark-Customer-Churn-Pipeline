# Customer Retention Intelligence: End-to-End Cloud Data Pipeline
**Scalable Big Data Analytics & Churn Prediction using AWS, PySpark, and Power BI**

![Project Status](https://img.shields.io/badge/Status-Completed-success) ![Tech Stack](https://img.shields.io/badge/AWS-S3%20%7C%20EC2%20%7C%20SageMaker-orange) ![Tech Stack](https://img.shields.io/badge/Tools-PySpark%20%7C%20PowerBI-blue)

## 📋 Executive Summary
**The Business Challenge:** Customer attrition (churn) is a critical revenue leak for banking institutions. The goal of this project was to move beyond simple analysis and engineer a scalable, cloud-native data pipeline capable of ingesting raw customer data, processing it at scale, and deploying a predictive model to identify at-risk clients.

**The Solution:** I architected an end-to-end pipeline using **AWS S3** for storage, **EC2/PySpark** for distributed processing, and **Amazon SageMaker** for automated machine learning.

**Key Results:**
* **Predictive Performance:** Achieved an **AUC-ROC of 0.87** and **Accuracy of 82.8%** in predicting customer churn.
* **Business Insight:** Identified that **inactive members account for 63.9% of all churned customers**, marking engagement as the #1 retention metric.
* **Scalability:** The pipeline is designed to handle distributed data processing, decoupled from local memory constraints.

---

## 📂 Data Source & Description
**Dataset:** Bank Customer Churn Modelling
**Volume:** 10,000 Records | 14 Attributes

To simulate a real-world banking scenario, I selected a dataset containing a mix of static demographic data and dynamic financial behaviors. The target variable is `Exited`, making this a classic binary classification problem.

| Feature Category | Attributes | Role in Analysis |
| :--- | :--- | :--- |
| **Target Variable** | `Exited` | **1 (Churned)** vs **0 (Retained)**. This is the label predicted by the SageMaker model. |
| **Financial Health** | `CreditScore`, `Balance`, `EstimatedSalary` | Used to determine if high-value customers are more likely to leave. |
| **Behavioral** | `Tenure`, `NumOfProducts`, `HasCrCard`, `IsActiveMember` | Key indicators of customer engagement and "stickiness." |
| **Demographics** | `Geography`, `Gender`, `Age` | Used for segmentation and identifying regional churn hotspots. |

---

## 🏗️ System Architecture & Workflow
The pipeline follows a modern cloud data engineering lifecycle, moving data from raw ingestion to actionable visualization.

<!-- Replace the path below with your actual architecture diagram image path -->
![AWS Pipeline Architecture](images/architecture_diagram.png)

1.  **Data Lake (AWS S3):** Raw customer data is ingested into an S3 bucket (`ndivekar-raw-data`) acting as the centralized landing zone.
2.  **Distributed Processing (AWS EC2 + PySpark):** An EC2 Linux instance hosts a PySpark cluster to clean, transform, and aggregate data. This ensures the system can scale to handle millions of rows without crashing local machines.
3.  **Machine Learning (Amazon SageMaker):** Processed data is fed into SageMaker Autopilot to train and tune binary classification models.
4.  **Business Intelligence (Power BI):** Final predictions and aggregations are visualized to track KPIs like churn by region and product holding.

---

## 🛠️ Tech Stack & Implementation

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Cloud Provider** | AWS | Ecosystem for storage, compute, and ML. |
| **Storage** | Amazon S3 | Stored raw (`.csv`) and processed data. |
| **Compute** | Amazon EC2 (Linux) | Hosted the Spark environment. |
| **ETL & Processing** | Apache Spark (PySpark) | Used for schema inference, missing value checks, and feature engineering (StringIndexing, MinMaxScaler). |
| **Machine Learning** | Amazon SageMaker | Automated model selection and hyperparameter tuning. |
| **Visualization** | Power BI | Dashboarding for stakeholder reporting. |

---

## 📊 Data Processing & Analysis (The "ETL" Layer)

### 1. Ingestion & Validation
The data was programmatically pulled from S3 into the PySpark environment using `boto3`. I implemented automated schema validation to ensure data integrity before processing.

### 2. Feature Engineering
To prepare the data for the Machine Learning model, I performed the following transformations in PySpark:
* **Categorical Encoding:** Applied `StringIndexer` to convert "Geography" and "Gender" into numerical indices for model consumption.
* **Normalization:** Applied `MinMaxScaler` to "Balance" and "EstimatedSalary" to standardize the range of features (0-1), preventing bias toward larger numbers in the model.

<!-- Replace with a screenshot of your PySpark code or dataframe schema -->
![PySpark ETL Process](images/pyspark_code.png)

---

## 🧠 Machine Learning Results (SageMaker)
I utilized **Amazon SageMaker Autopilot** to train a binary classification model targeting the `Exited` variable.

* **Best Model:** XGBoost (Ensemble)
* **Accuracy:** 82.8%
* **F1 Score:** 0.636 (Optimized for balance between Precision and Recall).

**Confusion Matrix / Sankey Analysis:**
The model is highly effective at identifying retained customers (Class 0), with a **Precision of 92.6%**. This gives the bank high confidence that customers predicted to "Stay" are indeed safe, allowing them to focus resources on the "At-Risk" segment.

<!-- Replace with your SageMaker metrics screenshot -->
![SageMaker Model Performance](images/sagemaker_metrics.png)

---

## 📉 Business Insights & Visualizations
Using **Power BI** and **Spark SQL**, I derived the following actionable insights for the stakeholders:

### 1. The "Inactive" Problem
* **Insight:** There is a direct correlation between member activity and churn. **63.9% of all exits comes from inactive members**.
* **Recommendation:** The marketing team should launch a re-engagement campaign (e.g., gamification or loyalty rewards) specifically targeting customers with "IsActiveMember = 0."

<!-- Replace with your 'Sum of Exited by IsActiveMember' chart -->
![Churn by Activity](images/churn_by_activity.png)

### 2. Geographic Hotspots
* **Insight:** Germany and France have significantly higher churn volumes (~800 exits each) compared to Spain (~400 exits).
* **Recommendation:** Regional managers in Germany and France need to investigate local competitive offers or service quality issues.

<!-- Replace with your 'Sum of Exited by Geography' chart -->
![Churn by Geography](images/churn_by_geography.png)

### 3. Product Saturation
* **Insight:** The vast majority of capital (Balance) is held by customers with only 1 product.
* **Recommendation:** There is a massive opportunity for cross-selling. Increasing the `NumOfProducts` per customer could increase stickiness and reduce churn.

---

## 💻 How to Reproduce this Project

**Prerequisites:**
* AWS Account (S3, EC2, SageMaker access)
* Python 3.x & PySpark installed on the EC2 instance

**Steps:**
1.  **Setup S3:** Upload the raw dataset to a bucket named `your-bucket-name`.
2.  **Configure EC2:** Launch a Linux EC2 instance and install Java and PySpark.
3.  **Run ETL:** Execute the `s3_data_ingestion.py` script to pull data and `normalize.py` to process features.
4.  **Upload:** Run the `upload.py` script to send processed data back to S3.
5.  **Train:** Point SageMaker Autopilot to the processed S3 bucket to initiate training.

---
**Author:** Noopur Shekhar Divekar
[Link to Portfolio / LinkedIn]
