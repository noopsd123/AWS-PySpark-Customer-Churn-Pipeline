from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession
spark = SparkSession.builder.appName("ActiveCustomersByRegion").getOrCreate()

# Load the dataset
file_path = "Churn_Modelling.csv"  # Update with the actual path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Count active customers by region
active_customers_by_region = df.filter(col("IsActiveMember") == 1) \
    .groupBy("Geography").count() \
    .withColumnRenamed("count", "ActiveCustomers")

# Show results
active_customers_by_region.show()

# Stop SparkSession
spark.stop()
