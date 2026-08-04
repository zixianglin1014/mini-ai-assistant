#!/bin/bash


echo "Stopping Mini AI Assistant"


PROJECT_DIR=$(cd "$(dirname "$0")/.." && pwd)


cd $PROJECT_DIR


docker compose down


echo "Service stopped"
