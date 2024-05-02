import boto3

# MinIO server endpoint (replace with your MinIO server URL)
minio_endpoint = 'http://localhost:9000'
# Access key and secret key for MinIO (replace with your credentials)
access_key = '9SgvtY5OQIiMS5K28NOc'
secret_key = 'FSm8bCUkGY6bj4Ox84nIIJKkvOp5wjgzzI6Kxb1g'
# Bucket name where you want to upload the file
bucket_name = 'splitamong'
# File path of the file you want to upload
file_path = '/home/frappe/minIO/dummy2.txt'
# Object key (name of the file in the bucket)
object_key = 'profile/dummy2.txt'

# Create a MinIO client
s3_client = boto3.client('s3', endpoint_url=minio_endpoint,
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key)

# Upload file to the bucket
try:
    response = s3_client.upload_file(file_path, bucket_name, object_key)
    object_url = f"{minio_endpoint}/{bucket_name}/{object_key}"
    print(object_url)
    print("File uploaded successfully!")
except Exception as e:
    print("Error uploading file:", e)

# http://localhost:9000/splitamong/dummy.txt