# End-to-End-Book-Recommender-System

## Workflow

- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-End-Book-Recommender-System.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n books python=3.7.10 -y
```

```bash
conda activate books
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


Now run,
```bash
streamlit run app.py
```


# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t entbappy/stapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 entbappy/stapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push entbappy/stapp:latest 
```

```bash
docker rmi entbappy/stapp:latest
```

```bash
docker pull entbappy/stapp
```



Absolutely! Here's a `README.md` tailored for your **End-to-End Book Recommender System**, incorporating everything you've shared—CI/CD pipeline, Docker, SonarQube, Trivy, Streamlit, and Kubernetes.

```markdown
# 📚 End-to-End Book Recommender System

A full-stack, containerized book recommendation engine built with Streamlit and deployed via Kubernetes. This project integrates robust DevSecOps practices—including static code analysis, container scanning, and automated deployment—using Jenkins, SonarQube, Trivy, Terraform, and Docker.

---

## 🚀 Features

- ✅ Interactive UI powered by **Streamlit**
- ✅ Static code analysis via **SonarQube**
- ✅ Vulnerability scanning with **Trivy**
- ✅ Continuous Integration/Delivery through **Jenkins**
- ✅ Dockerized and deployed via **Kubernetes**
- ✅ Infrastructure provisioning with **Terraform**

---

## 🧪 Tech Stack

| Layer            | Tools                                  |
|------------------|-----------------------------------------|
| Frontend         | Streamlit (runs on port `8501`)         |
| CI/CD            | Jenkins Pipelines                       |
| Static Analysis  | SonarQube + Quality Gate enforcement    |
| Container Image  | Docker (DockerHub: `lmen776/book-recommender`) |
| Security Scan    | Trivy (output saved as `trivy.txt`)     |
| Deployment       | Kubernetes Deployment + Service + Ingress |
| Infra Provision  | Terraform                               |

---

## ⚙️ Jenkins Pipeline Stages

1. **Checkout Code** from GitHub  
2. **SonarQube Analysis**  
3. **Wait for Quality Gate**  
4. **Trivy File System Scan**  
5. **Docker Build & Push**  
6. **Deploy to Container** (exposes Streamlit on port `8501`)

---

## 🐳 Docker

```bash
docker build -t book-recommender .
docker tag book-recommender lmen776/book-recommender:latest
docker push lmen776/book-recommender:latest
```

---

## ☸️ Kubernetes Deployment

### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: book-recommender-deployment
  labels:
    app: book-recommender
spec:
  replicas: 2
  selector:
    matchLabels:
      app: book-recommender
  template:
    metadata:
      labels:
        app: book-recommender
    spec:
      containers:
      - name: book-recommender
        image: lmen776/book-recommender:latest
        ports:
        - containerPort: 8501
```

### Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: book-recommender-service
spec:
  selector:
    app: book-recommender
  ports:
  - port: 80
    targetPort: 8501
  type: LoadBalancer
```

### Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-book-recommender
spec:
  rules:
  - host: "domain.com"
    http:
      paths:
      - pathType: Prefix
        path: "/test"
        backend:
          service:
            name: book-recommender-service
            port:
              number: 8501
  - host: "*.domain.com"
    http:
      paths:
      - pathType: Prefix
        path: "/test"
        backend:
          service:
            name: book-recommender-service
            port:
              number: 8501
```

---

## 📦 Terraform

Use Terraform to provision your Kubernetes cluster (GKE, EKS, or AKS) directly from a Jenkins pipeline:

```bash
terraform init
terraform plan -out=tfplan
terraform apply -auto-approve tfplan
```

---

## 🔐 Security Considerations

- SonarQube Quality Gate enforces code health before progressing.
- Trivy scans ensure image vulnerabilities are flagged before deploy.
- Secure registry and credential handling via Jenkins Credentials Binding.

---

## 👤 Author

**longmen2022**  
Feel free to fork, contribute, and customize this pipeline for your own data science and ML apps!

---

## 📝 License

[MIT](LICENSE)
```

Want me to generate badges for CI status, DockerHub pulls, or expand this into GitHub Pages-style documentation? I’d love to level it up with you! 💡✨📖  




