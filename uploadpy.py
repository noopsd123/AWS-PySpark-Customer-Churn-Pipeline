import os
import boto3

def upload_py_files_to_s3(local_directory, s3_bucket_name, s3_prefix=""):
    """
    Uploads all .py files from a local directory to an S3 bucket.

    :param local_directory: The local directory containing .py files
    :param s3_bucket_name: Target S3 bucket name
    :param s3_prefix: Optional prefix to add to S3 keys
    """
    # Initialize S3 client
    s3_client = boto3.client('s3')

    # Walk through the local directory
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            if file.endswith('.py'):  # Check if the file is a Python script
                local_file_path = os.path.join(root, file)  # Full local file path
                # Create S3 key by stripping the local directory prefix
                relative_path = os.path.relpath(local_file_path, local_directory)
                s3_file_key = os.path.join(s3_prefix, relative_path).replace("\\", "/")  # Use forward slashes for S3 keys

                try:
                    print(f"Uploading {local_file_path} to s3://{s3_bucket_name}/{s3_file_key}...")
                    s3_client.upload_file(local_file_path, s3_bucket_name, s3_file_key)
                    print(f"Uploaded {local_file_path} successfully.")
                except Exception as e:
                    print(f"Failed to upload {local_file_path}: {e}")

# Parameters
local_directory = "."  
s3_bucket_name = "ndivekar-raw-data"  
s3_prefix = "python-scripts/"  

# Upload .py files to S3
upload_py_files_to_s3(local_directory, s3_bucket_name, s3_prefix)
