
---

# MinIO Docker Setup

This repository contains a Docker setup for running MinIO with Docker Compose.

## Getting Started

1. Clone this repository to your local machine.

2. Navigate to the repository directory.

3. Run the following command to start the MinIO server:

   ```bash
   docker-compose up -d --build
   ```

   This command will build the Docker images if they don't exist and start the MinIO server.

4. Once the containers are up and running, execute the following command to access the scripter container:

   ```bash
   docker exec -it minio_scripter_1 bash
   ```

5. Within the scripter container, run the script to create buckets and users:

   ```bash
   ./S3_create_bucket_user.sh
   ```

6. To shut down and remove all containers and volumes created by Docker Compose, run:

   ```bash
   docker-compose down -v
   ```

## Additional Cleanup Commands

1. Remove all Docker images:

   ```bash
   docker rmi $(docker images -qa) -f
   ```

   This command will forcefully remove all Docker images from your system.

2. Remove all Docker volumes:

   ```bash
   docker volume rm $(docker volume ls -q) -f
   ```

   Use this command to remove all Docker volumes.

---

Feel free to customize the instructions further to fit your specific setup or requirements.
