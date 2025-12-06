from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Initialize SparkSession
spark = SparkSession.builder.appName("AverageBalanceByTenure").getOrCreate()

# Load the dataset
file_path = "Churn_Modelling.csv"  # Update with the actual path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Compute average balance by tenure
average_balance_by_tenure = df.groupBy("Tenure").agg(avg("Balance").alias("AverageBalance"))

# Show results
average_balance_by_tenure.show()

# Stop SparkSession
spark.stop()
