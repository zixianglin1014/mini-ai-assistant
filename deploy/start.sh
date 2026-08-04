#!/bin/bash


echo "================================"
echo "Starting Mini AI Assistant"
echo "================================"


PROJECT_DIR=$(cd "$(dirname "$0")/.." && pwd)


cd $PROJECT_DIR


echo "Current directory:"
pwd


echo "Stopping old container..."

docker compose down


echo "Building image..."

docker compose build


echo "Starting service..."

docker compose up -d


echo "Checking status..."

docker ps


echo "================================"
echo "Mini AI Assistant Started"
echo "================================"
