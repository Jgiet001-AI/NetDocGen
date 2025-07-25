#!/bin/bash

echo "🛑 Stopping NetDocGen..."

docker-compose down

echo "✅ NetDocGen stopped."
echo ""
echo "ℹ️  Note: Data is preserved in Docker volumes."
echo "   To completely remove all data: docker-compose down -v"