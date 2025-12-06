from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CheckMissingValues") \
    .getOrCreate()

# Load the dataset into a PySpark DataFrame
file_path = "Churn_Modelling.csv"  # Update with the actual path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the schema of the dataset
print("Schema of the dataset:")
df.printSchema()

# Count rows with null values for each column
print("Count of missing (null) values per column:")
missing_values = df.select(
    [(col(c).isNull().cast("int").alias(c)) for c in df.columns]
).select(
    [_sum(c).alias(c) for c in df.columns]
)

missing_values.show()

# Stop SparkSession
spark.stop()
