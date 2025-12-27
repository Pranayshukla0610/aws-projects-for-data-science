import boto3
s3 = boto3.client('s3')
BUCKET_NAME = "sales-data-python-project-pranay"

LOCAL_FILE = "C:/Users/prana/OneDrive - CDE/Documents/aws-s3-sales-data-pipeline/data/bigmart.csv"
S3_FILE = "raw/bigmart.csv"

s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_FILE)
print("File uploaded successfully to S3")


