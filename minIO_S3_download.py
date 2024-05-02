import boto3

# MinIO server endpoint (replace with your MinIO server URL)
minio_endpoint = 'http://localhost:9000'
# Access key and secret key for MinIO (replace with your credentials)
access_key = '9SgvtY5OQIiMS5K28NOc'
secret_key = 'FSm8bCUkGY6bj4Ox84nIIJKkvOp5wjgzzI6Kxb1g'
# Bucket name where the file is located
bucket_name = 'splitamong'
# Object key (name of the file in the bucket)
object_key = 'dummy2.txt'
# File path to save the downloaded file
file_path = '/home/frappe/minIO/dummy3.txt'  # Replace with the path where you want to save the file

# Create a MinIO client
s3_client = boto3.client('s3', endpoint_url=minio_endpoint,
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key)

# Download file from the bucket
try:
    s3_client.download_file(bucket_name, object_key, file_path)
    print("File downloaded successfully!")
except Exception as e:
    print("Error downloading file:", e)
