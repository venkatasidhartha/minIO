#!/bin/bash

# MinIO server endpoint
MINIO_ENDPOINT="http://minio1:9000"
# Alias for MinIO server
MINIO_ALIAS="minioadmin"
# Username for the new user
USERNAME="splitamoung"
# Password for the new user
PASSWORD="splitamoung"
# Bucket name
BUCKETNAME="splitamoung"

mc alias set minioadmin http://minio1:9000 minioadmin minioadmin


# Create bucket
mc mb ${MINIO_ALIAS}/${BUCKETNAME}

# Add user
mc admin user add ${MINIO_ALIAS} ${USERNAME} ${PASSWORD}

# Create policy JSON file
cat <<EOF > policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": ["arn:aws:s3:::${BUCKETNAME}/*"]
    }
  ]
}
EOF

mc admin user list ${MINIO_ALIAS}

# Add policy to MinIO server
mc admin policy create ${MINIO_ALIAS} readwrite-policy policy.json

# Set policy for user
mc admin policy attach ${MINIO_ALIAS} readwrite-policy --user=${USERNAME}

echo "User '${USERNAME}' has been added and granted read/write permissions to bucket '${BUCKETNAME}'."

