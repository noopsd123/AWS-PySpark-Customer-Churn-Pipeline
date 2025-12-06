import boto3
from pyspark.sql import SparkSession

# Initialize S3 client
s3_client = boto3.client('s3')

# S3 Bucket and File Details
bucket_name = "ndivekar-raw-data"
file_key = "Churn_Modelling.csv"
local_file_path = "Churn_Modelling.csv"

# Step 1: Download the dataset from S3
try:
    print(f"Downloading {file_key} from bucket {bucket_name}...")
    s3_client.download_file(bucket_name, file_key, local_file_path)
    print(f"File downloaded to {local_file_path}")
except Exception as e:
    print(f"Error downloading file: {e}")
    exit(1)

# Step 2: Initialize PySpark Session
spark = SparkSession.builder \
    .appName("S3DataIngestion") \
    .getOrCreate()

# Step 3: Load the Dataset into PySpark
try:
    print(f"Loading dataset into PySpark from {local_file_path}...")
    df = spark.read.csv(local_file_path, header=True, inferSchema=True)
    print("Dataset loaded successfully!")

    # Step 4: Inspect the Dataset
    print("Schema of the dataset:")
    df.printSchema()

    print("Sample rows from the dataset:")
    df.show(5)

except Exception as e:
    print(f"Error loading dataset into PySpark: {e}")
finally:
    spark.stop()

