#!/bin/bash


echo "===== Mini AI Assistant Deploy ====="



echo "Stopping old container..."

docker compose down



echo "Building image..."

docker compose build



echo "Starting service..."

docker compose up -d



echo "Checking status..."

docker ps



echo "Health check..."

curl http://localhost:8000/health



echo ""

echo "Deploy finished."
