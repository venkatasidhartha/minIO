import boto3

# MinIO server endpoint (replace with your MinIO server URL)
minio_endpoint = 'http://localhost:9000'
# IAM user credentials
username = 'splitamoung'
password = 'splitamoung'
# Bucket name where the file will be uploaded
bucket_name = 'splitamoung'
# Local file path
local_file_path = '/home/frappe/minIO/dummy2.txt'
# Destination object key (name of the file in the bucket)
destination_object_key = 'dummy2.txt'

# Create a session with IAM credentials
session = boto3.session.Session()
s3_client = session.client('s3', endpoint_url=minio_endpoint,
                            aws_access_key_id=username,
                            aws_secret_access_key=password)

# Upload file to the bucket
try:
    with open(local_file_path, 'rb') as file_data:
        s3_client.upload_fileobj(file_data, bucket_name, destination_object_key)
    print("File uploaded successfully.")
except Exception as e:
    print("Error uploading file:", e)
