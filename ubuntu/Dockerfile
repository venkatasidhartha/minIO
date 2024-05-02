# Use Ubuntu 22 as the base image
FROM ubuntu:22.04

# Install curl
RUN apt-get update && apt-get install -y curl

# Set up MinIO Client (mc)
RUN mkdir -p /root/minio-binaries && \
    curl https://dl.min.io/client/mc/release/linux-amd64/mc \
         --create-dirs \
         -o /root/minio-binaries/mc && \
    chmod +x /root/minio-binaries/mc && \
    echo "export PATH=\$PATH:/root/minio-binaries" >> /root/.bashrc

COPY S3_create_bucket_user.sh .
RUN chmod +x S3_create_bucket_user.sh
# RUN ./S3_create_bucket_user.sh 
# Entrypoint to start a shell
CMD ["sleep", "infinity"]
