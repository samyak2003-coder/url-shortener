# 🚀 URL Shortener - Kubernetes & Docker Deployment

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

#### 🚀 Start Docker Daemon
```sh
sudo systemctl start docker
docker-compose up  --build
```


#### ☸ Start Minikube (If using Minikube)
```sh
minikube start
minikube tunnel 
kubectl port-forward svc/url-shortener-service 8080:80 -n default

```


#### 4️⃣ Apply Kubernetes Configurations
```sh
kubectl apply -f k8s/
```

#### 7️⃣ Apply HPA for Auto Scaling
```sh
kubectl autoscale deployment url-shortener --cpu-percent=50 --min=1 --max=25
```
#### or use kubernetes metrics-server

#### 💥 Stress Test using Apache Benchmark (ab)
```sh
for i in {1..1000}; do curl -X POST -H "Content-Type: application/json" -d '{"long_url": "http://example.com"}' http://localhost:8080/shorten & done

kubectl get pods -w
```
