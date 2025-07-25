#!/bin/bash

# NetDocGen Kubernetes Deployment Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
ENVIRONMENT="development"
NAMESPACE="netdocgen-dev"
BUILD_IMAGES=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -e|--environment)
            ENVIRONMENT="$2"
            shift 2
            ;;
        -b|--build)
            BUILD_IMAGES=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [options]"
            echo "Options:"
            echo "  -e, --environment ENV    Environment to deploy (development, staging, production)"
            echo "  -b, --build             Build and push Docker images before deploying"
            echo "  -h, --help              Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Set namespace based on environment
case $ENVIRONMENT in
    development)
        NAMESPACE="netdocgen-dev"
        ;;
    staging)
        NAMESPACE="netdocgen-staging"
        ;;
    production)
        NAMESPACE="netdocgen"
        ;;
    *)
        echo -e "${RED}Invalid environment: $ENVIRONMENT${NC}"
        exit 1
        ;;
esac

echo -e "${GREEN}Deploying NetDocGen to $ENVIRONMENT environment${NC}"

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    echo -e "${RED}kubectl is not installed${NC}"
    exit 1
fi

# Check if kustomize is available
if ! kubectl kustomize --help &> /dev/null; then
    echo -e "${RED}kustomize is not available${NC}"
    exit 1
fi

# Build and push images if requested
if [ "$BUILD_IMAGES" = true ]; then
    echo -e "${YELLOW}Building Docker images...${NC}"
    
    # Build API image
    docker build -t ghcr.io/jgiet001-ai/netdocgen-api:latest ./api
    docker push ghcr.io/jgiet001-ai/netdocgen-api:latest
    
    # Build Parser image
    docker build -t ghcr.io/jgiet001-ai/netdocgen-parser:latest ./parser
    docker push ghcr.io/jgiet001-ai/netdocgen-parser:latest
    
    # Build Generator image
    docker build -t ghcr.io/jgiet001-ai/netdocgen-generator:latest ./generator
    docker push ghcr.io/jgiet001-ai/netdocgen-generator:latest
    
    # Build Frontend image
    docker build -t ghcr.io/jgiet001-ai/netdocgen-frontend:latest ./frontend
    docker push ghcr.io/jgiet001-ai/netdocgen-frontend:latest
    
    echo -e "${GREEN}Images built and pushed successfully${NC}"
fi

# Check if overlay exists
if [ ! -d "k8s/overlays/$ENVIRONMENT" ]; then
    echo -e "${RED}Overlay for $ENVIRONMENT does not exist${NC}"
    exit 1
fi

# Dry run first
echo -e "${YELLOW}Running dry-run...${NC}"
kubectl apply -k k8s/overlays/$ENVIRONMENT --dry-run=client

# Apply the configuration
echo -e "${YELLOW}Applying Kubernetes configuration...${NC}"
kubectl apply -k k8s/overlays/$ENVIRONMENT

# Wait for deployments
echo -e "${YELLOW}Waiting for deployments to be ready...${NC}"
kubectl wait --for=condition=available --timeout=300s \
    deployment -l app.kubernetes.io/part-of=netdocgen \
    -n $NAMESPACE

# Show status
echo -e "${GREEN}Deployment complete!${NC}"
echo ""
echo "Status:"
kubectl get pods -n $NAMESPACE
echo ""
echo "Services:"
kubectl get svc -n $NAMESPACE
echo ""

# Show access information
if [ "$ENVIRONMENT" = "development" ]; then
    echo -e "${GREEN}Access information:${NC}"
    echo "Add to /etc/hosts:"
    echo "127.0.0.1 netdocgen.local minio.netdocgen.local rabbitmq.netdocgen.local"
    echo ""
    echo "Or use port forwarding:"
    echo "kubectl port-forward -n $NAMESPACE svc/dev-frontend 3000:80"
    echo "kubectl port-forward -n $NAMESPACE svc/dev-api 8000:8000"
    echo "kubectl port-forward -n $NAMESPACE svc/dev-minio 9001:9001"
    echo "kubectl port-forward -n $NAMESPACE svc/dev-rabbitmq 15672:15672"
fi