#!/bin/bash

# Script to initialize Ollama with Phi-3 model

echo "Waiting for Ollama to be ready..."
sleep 5

# Get the actual container name
OLLAMA_CONTAINER=$(docker-compose ps -q ollama)

if [ -z "$OLLAMA_CONTAINER" ]; then
    echo "Error: Ollama container not found. Make sure docker-compose is running."
    exit 1
fi

# Pull the Phi-3 model
echo "Pulling Phi-3 model (this may take a few minutes)..."
docker exec -it $OLLAMA_CONTAINER ollama pull phi3

echo "✅ Phi-3 model is ready!"
echo "You can test it with: docker exec -it $OLLAMA_CONTAINER ollama run phi3"