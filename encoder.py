from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CreateNewEncodedDataset") \
    .getOrCreate()

# Load the dataset
file_path = "Churn_Modelling.csv"  # Update with the actual path
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Columns to encode
categorical_columns = ["Geography", "Gender"]

# Apply StringIndexer to each categorical column
for column in categorical_columns:
    output_column = f"{column}_Index"
    # Drop the column if it already exists
    if output_column in df.columns:
        df = df.drop(output_column)
    indexer = StringIndexer(inputCol=column, outputCol=output_column)
    df = indexer.fit(df).transform(df)

# Save the encoded dataset to a new CSV file
encoded_file_path = "Churn_Modelling_Encoded.csv"  # Update the path as needed
df.write.csv(encoded_file_path, header=True, mode="overwrite")

# Show the resulting dataset
df.show(10)

# Stop SparkSession
spark.stop()
