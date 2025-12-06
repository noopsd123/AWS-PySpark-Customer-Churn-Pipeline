from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("DataAnalysisUsingSparkSQL") \
    .getOrCreate()

# Load the dataset
file_path = "Churn_Modelling.csv"  
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Register the DataFrame as a temporary SQL table
df.createOrReplaceTempView("churn_data")

# Query 1: Identify top-performing regions (by total Balance)
query1 = """
SELECT Geography, SUM(Balance) AS TotalBalance
FROM churn_data
GROUP BY Geography
ORDER BY TotalBalance DESC
"""
top_regions = spark.sql(query1)
print("Top-performing regions:")
top_regions.show()

# Query 2: Analyze month-over-month revenue growth (based on Balance and Tenure)
query2 = """
SELECT Tenure AS Month, SUM(Balance) AS TotalBalance
FROM churn_data
GROUP BY Tenure
ORDER BY Month
"""
monthly_revenue_growth = spark.sql(query2)
print("Month-over-month revenue growth:")
monthly_revenue_growth.show()

# Query 3: Determine the most popular product categories (by NumOfProducts)
query3 = """
SELECT NumOfProducts, COUNT(*) AS CustomerCount
FROM churn_data
GROUP BY NumOfProducts
ORDER BY CustomerCount DESC
"""
popular_products = spark.sql(query3)
print("Most popular product categories:")
popular_products.show()

# Query 4: Average Estimated Salary by Gender
query4 = """
SELECT Gender, AVG(EstimatedSalary) AS AverageSalary
FROM churn_data
GROUP BY Gender
"""
average_salary_gender = spark.sql(query4)
print("Average Estimated Salary by Gender:")
average_salary_gender.show()

# Query 5: Percentage of active customers by region
query5 = """
SELECT Geography, 
       COUNT(*) AS TotalCustomers,
       SUM(CASE WHEN IsActiveMember = 1 THEN 1 ELSE 0 END) AS ActiveCustomers,
       (SUM(CASE WHEN IsActiveMember = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS ActivePercentage
FROM churn_data
GROUP BY Geography
ORDER BY ActivePercentage DESC
"""
active_customers_percentage = spark.sql(query5)
print("Percentage of active customers by region:")
active_customers_percentage.show()

# Stop SparkSession
spark.stop()
