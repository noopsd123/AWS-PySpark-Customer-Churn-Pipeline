import boto3
import os

def upload_folder_content_as_file(local_folder, s3_bucket, s3_filename):
    s3_client = boto3.client('s3')
    
    # 1. Find the actual CSV file inside the folder
    try:
        files = os.listdir(local_folder)
        # Filter for files that end in .csv and ignore hidden/success files
        csv_files = [f for f in files if f.endswith('.csv') and not f.startswith('_') and not f.startswith('.')]
        
        if not csv_files:
            print(f"Error: No .csv files found inside {local_folder}")
            print(f"Contents found: {files}")
            return

        # We grab the first valid CSV found (usually part-00000...)
        actual_file_name = csv_files[0]
        local_file_path = os.path.join(local_folder, actual_file_name)
        
        print(f"Found actual file: {local_file_path}")
        print(f"Uploading to s3://{s3_bucket}/{s3_filename}...")

        # 2. Upload it
        with open(local_file_path, 'rb') as data:
            s3_client.upload_fileobj(data, s3_bucket, s3_filename)
            
        print("Success! Upload complete.")

    except Exception as e:
        print(f"Error processing folder: {e}")

# --- PARAMETERS ---
folder_name = "Churn_Modelling_Normalized.csv"  # The folder causing the error
bucket_target = "ndivekar-processed-data"
s3_key_name = "Churn_Modelling_Normalized.csv"  # The clean name for S3

# --- EXECUTE ---
if os.path.isdir(folder_name):
    upload_folder_content_as_file(folder_name, bucket_target, s3_key_name)
else:
    print(f"Error: '{folder_name}' is not a directory. Please check your path.")
