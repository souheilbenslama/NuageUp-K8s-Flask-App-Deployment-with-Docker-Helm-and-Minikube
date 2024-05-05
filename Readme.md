the hello world Flask application

this repository contains a flask hello world application with all the required ressources for its deployment on a kubernetes cluster.

to test this application you need to start by creating a kubernetes cluster.

also you need to use a virtual environnment
you can run the application

```
flask run --host 0.0.0.0 app.py
```

flask

# prerequisite tools

- Docker
- Minikube
- Helm
- Flask
- Cilium or Calingo

to benefit from horizental pod autoscaling you need to enbale metrics server on your cluster

# local testing

# deployment

# how we assured sefl-healing in this app ?
