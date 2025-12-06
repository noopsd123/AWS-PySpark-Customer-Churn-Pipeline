from pyspark.sql import SparkSession
from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import udf
from pyspark.ml.linalg import DenseVector
from pyspark.sql.types import DoubleType

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("NormalizeColumns") \
    .getOrCreate()

# Load the dataset
file_path = "Churn_Modelling_Encoded.csv"  
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Prepare columns to normalize
columns_to_normalize = ["Balance", "EstimatedSalary"]

# Create VectorAssembler for MinMaxScaler input
assembler = VectorAssembler(inputCols=columns_to_normalize, outputCol="features")
df_vectorized = assembler.transform(df)

# Apply MinMaxScaler
scaler = MinMaxScaler(inputCol="features", outputCol="scaledFeatures")
scaler_model = scaler.fit(df_vectorized)
df_scaled = scaler_model.transform(df_vectorized)

# Define UDFs to extract normalized values
def extract_first_element(vector):
    return float(vector[0])

def extract_second_element(vector):
    return float(vector[1])

udf_extract_first = udf(extract_first_element, DoubleType())
udf_extract_second = udf(extract_second_element, DoubleType())

# Create new normalized columns
df_normalized = df_scaled.withColumn("Normalized_Balance", udf_extract_first("scaledFeatures")) \
                         .withColumn("Normalized_EstimatedSalary", udf_extract_second("scaledFeatures"))

# Drop the unsupported columns before saving
df_final = df_normalized.drop("features", "scaledFeatures")

# Show the resulting DataFrame
df_final.show(10)

# Save the normalized dataset
normalized_file_path = "Churn_Modelling_Normalized.csv"
df_final.write.csv(normalized_file_path, header=True, mode="overwrite")

# Stop SparkSession
spark.stop()
