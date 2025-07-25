# NetDocGen Kubernetes Deployment

This directory contains Kubernetes manifests for deploying NetDocGen using Kustomize.

## Directory Structure

```
k8s/
├── base/                    # Base configuration
│   ├── namespace.yaml      # Namespace definition
│   ├── postgres.yaml       # PostgreSQL database
│   ├── redis.yaml          # Redis cache
│   ├── minio.yaml          # MinIO object storage
│   ├── rabbitmq.yaml       # RabbitMQ message queue
│   ├── ollama.yaml         # Ollama AI service
│   ├── api.yaml            # API backend service
│   ├── parser.yaml         # Visio parser service
│   ├── generator.yaml      # Document generator service
│   ├── frontend.yaml       # React frontend
│   ├── ingress.yaml        # Ingress configuration
│   └── kustomization.yaml  # Kustomize configuration
└── overlays/               # Environment-specific configurations
    ├── development/        # Development environment
    ├── staging/            # Staging environment
    └── production/         # Production environment
```

## Prerequisites

1. Kubernetes cluster (1.24+)
2. kubectl configured
3. kustomize (or kubectl 1.14+)
4. NGINX Ingress Controller
5. cert-manager (for TLS certificates)

## Quick Start

### Development Environment

1. Build and apply the development configuration:
   ```bash
   kubectl apply -k k8s/overlays/development
   ```

2. Add to your `/etc/hosts`:
   ```
   127.0.0.1 netdocgen.local
   127.0.0.1 minio.netdocgen.local
   127.0.0.1 rabbitmq.netdocgen.local
   ```

3. Port forward if not using Ingress:
   ```bash
   # Frontend
   kubectl port-forward -n netdocgen-dev svc/dev-frontend 3000:80
   
   # API
   kubectl port-forward -n netdocgen-dev svc/dev-api 8000:8000
   
   # MinIO Console
   kubectl port-forward -n netdocgen-dev svc/dev-minio 9001:9001
   
   # RabbitMQ Management
   kubectl port-forward -n netdocgen-dev svc/dev-rabbitmq 15672:15672
   ```

### Production Environment

1. Update secrets in production overlay
2. Update ingress hosts
3. Apply the configuration:
   ```bash
   kubectl apply -k k8s/overlays/production
   ```

## Configuration

### Secrets Management

For production, create proper secrets:

```bash
# PostgreSQL password
kubectl create secret generic postgres-secret \
  --from-literal=POSTGRES_PASSWORD='secure-password' \
  -n netdocgen

# MinIO credentials
kubectl create secret generic minio-secret \
  --from-literal=MINIO_ROOT_USER='admin' \
  --from-literal=MINIO_ROOT_PASSWORD='secure-password' \
  -n netdocgen

# API secrets
kubectl create secret generic api-secret \
  --from-literal=SECRET_KEY='secure-jwt-secret' \
  --from-literal=MINIO_ACCESS_KEY='admin' \
  --from-literal=MINIO_SECRET_KEY='secure-password' \
  -n netdocgen
```

### Storage Classes

The manifests use default storage class. For production, consider:
- High-performance SSD for PostgreSQL
- Standard storage for MinIO
- Local SSD for Ollama models

### Resource Limits

Default resource limits are set for production. Adjust based on your needs:
- API: 2 replicas, 1Gi memory each
- Parser: 2 replicas, 1Gi memory each
- Generator: 2 replicas, 2Gi memory each
- Frontend: 2 replicas, 256Mi memory each

## Monitoring

### Metrics

Services expose Prometheus metrics:
- API: `:8000/metrics`
- Parser/Generator: Custom metrics via StatsD

### Health Checks

All services have liveness and readiness probes configured.

## Troubleshooting

### Check pod status
```bash
kubectl get pods -n netdocgen-dev
```

### View logs
```bash
kubectl logs -n netdocgen-dev deployment/dev-api
kubectl logs -n netdocgen-dev deployment/dev-parser
kubectl logs -n netdocgen-dev deployment/dev-generator
```

### Debug pod
```bash
kubectl exec -it -n netdocgen-dev deployment/dev-api -- /bin/bash
```

### Common Issues

1. **Database connection failed**
   - Check PostgreSQL pod is running
   - Verify DATABASE_URL in api ConfigMap
   - Check network policies

2. **MinIO upload failed**
   - Verify MinIO credentials match between services
   - Check MinIO pod has sufficient storage
   - Verify bucket creation

3. **RabbitMQ connection failed**
   - Check RabbitMQ pod is running
   - Verify credentials in ConfigMaps
   - Check queue declarations

## Scaling

### Horizontal scaling
```bash
# Scale API replicas
kubectl scale deployment dev-api --replicas=3 -n netdocgen-dev

# Scale parser workers
kubectl scale deployment dev-parser --replicas=5 -n netdocgen-dev
```

### Vertical scaling
Edit resource limits in overlays and reapply:
```bash
kubectl apply -k k8s/overlays/development
```

## Backup and Restore

### PostgreSQL backup
```bash
kubectl exec -n netdocgen-dev deployment/dev-postgres -- \
  pg_dump -U postgres netdocgen > backup.sql
```

### MinIO backup
Use MinIO client (mc) to backup buckets:
```bash
mc mirror minio/netdocgen ./backup/
```