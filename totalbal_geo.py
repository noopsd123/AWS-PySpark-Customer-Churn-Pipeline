from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

# Initialize SparkSession
spark = SparkSession.builder.appName("TotalBalanceByGeography").getOrCreate()

# Load the dataset
file_path = "Churn_Modelling.csv"  # Update with the actual path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Compute total balance by geography
total_balance_by_geography = df.groupBy("Geography").agg(_sum("Balance").alias("TotalBalance"))

# Show results
total_balance_by_geography.show()

# Stop SparkSession
spark.stop()
