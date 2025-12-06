
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

# Initialize SparkSession
spark = SparkSession.builder.appName("Top10CustomersByBalance").getOrCreate()

# Load the dataset
file_path = "Churn_Modelling.csv"  # Update with the actual path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Get top 10 customers by balance
top_10_customers_by_balance = df.select("CustomerId", "Surname", "Balance") \
    .orderBy(desc("Balance")) \
    .limit(10)

# Show results
top_10_customers_by_balance.show()

# Stop SparkSession
spark.stop()
