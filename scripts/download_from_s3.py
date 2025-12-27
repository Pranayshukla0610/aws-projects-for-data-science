import boto3

# Create S3 client
s3 = boto3.client('s3')

# Replace with your actual bucket name
BUCKET_NAME = "sales-data-python-project-pranay"

# File path in S3
S3_FILE = "raw/bigmart.csv"

# Where to save the file locally (relative path)
LOCAL_FILE = "C:/Users/prana/OneDrive - CDE/Documents/aws-s3-sales-data-pipeline/data/bigmart.csv"

# Download file
s3.download_file(BUCKET_NAME, S3_FILE, LOCAL_FILE)

print("File downloaded successfully from S3")
