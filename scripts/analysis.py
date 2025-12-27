import pandas as pd

# Load downloaded data
df = pd.read_csv("C:/Users/prana/OneDrive - CDE/Documents/aws-s3-sales-data-pipeline/data/bigmart.csv")

# Data cleaning: remove duplicates, fill missing values
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Save cleaned data locally
df.to_csv("../output/cleaned_data.csv", index=False)

# Basic sales analysis
total_sales = df["Item_Outlet_Sales"].sum()
average_sales = df["Item_Outlet_Sales"].mean()
sales_by_outlet = df.groupby("Outlet_Type")["Item_Outlet_Sales"].sum()

# Save summary to text file
with open("../output/summary_stats.txt", "w") as f:
    f.write(f"Total Sales: {total_sales}\n")
    f.write(f"Average Sales: {average_sales}\n\n")
    f.write("Sales by Outlet Type:\n")
    f.write(sales_by_outlet.to_string())

print("Data cleaning and analysis completed.")

import boto3

s3 = boto3.client('s3')

BUCKET_NAME = "sales-data-python-project-pranay"

# Upload cleaned data
s3.upload_file("../output/cleaned_data.csv", BUCKET_NAME, "processed/cleaned_data.csv")

# Upload summary stats
s3.upload_file("../output/summary_stats.txt", BUCKET_NAME, "processed/summary_stats.txt")

print("Cleaned data and summary uploaded to S3.")

