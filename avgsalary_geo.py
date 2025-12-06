from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Initialize SparkSession
spark = SparkSession.builder.appName("AverageSalaryByGeography").getOrCreate()

# Load the dataset
file_path = "Churn_Modelling.csv"  # Update with the actual path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Compute average salary by geography
average_salary_by_geography = df.groupBy("Geography").agg(avg("EstimatedSalary").alias("AverageSalary"))

# Show results
average_salary_by_geography.show()

# Stop SparkSession
spark.stop()
