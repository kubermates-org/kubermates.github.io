---
title: "🎨 Hacking the Helm Operator with Flux: Creating Self-Installable Services for Easier App Deployment"
date: 2024-08-28T08:01:26+00:00
description: "Managing applications in Kubernetes can be tricky, but with tools like Helm, operators, and Flux, you..."
tags: ["kubernetes", "cloud", "opensource", "programming"]
draft: false
slug: "hacking-the-helm-operator-with-flux-creating-self-installable-services-for-easier-app-deployment-5a8l"
devto_id: 1965864
devto_url: "https://dev.to/hkhelil/hacking-the-helm-operator-with-flux-creating-self-installable-services-for-easier-app-deployment-5a8l"
---
Managing applications in Kubernetes can be tricky, but with tools like Helm, operators, and Flux, you can make the process smoother and even fun! In this guide, we'll walk you through how to hack the Helm Operator using the Operator SDK and Flux to create powerful, self-installable services that make deploying apps like NGINX, Apache Tomcat, and even Redis a breeze. 🌬️

By the end, you'll have your very own GitOps-powered system, making deployments as simple as pushing to a Git repository. Let's dive in!

## 🛠️ Prerequisites

Before we start, make sure you have:

- A Kubernetes cluster (Minikube, kind, or a cloud provider like GKE, AKS, or EKS).
- Helm installed.
- Flux installed and configured.
- Operator SDK installed.

## 🌐 What’s the Helm Operator?

The Helm Operator, part of the Flux ecosystem, helps manage Helm charts in Kubernetes using declarative YAML files. But with a little creativity and the Operator SDK, you can turn the Helm Operator into something even more powerful—an operator that not only manages Helm charts but also automates complex tasks, making your services self-installable! 🎉

## 🎉 Example 1: Deploying NGINX with a Custom Helm Operator

Let's start by deploying an NGINX web server. NGINX is a lightweight, high-performance web server, and it’s perfect for this demonstration.

### Step 1: Scaffold a New Helm-Based Operator

First, create a new Helm-based operator:

```bash
operator-sdk init --plugins helm --domain mydomain.com --group web --version v1 --kind NGINXOperator
```

This sets up the basic structure of your operator.

### Step 2: Add the NGINX Helm Chart

Now, grab the official NGINX Helm chart and place it in your project:

```bash
mkdir -p helm-charts/nginx
helm pull bitnami/nginx --untar --untardir helm-charts/nginx
```

Your folder structure should look like this:

```
.
├── config
│   └── ... (Kubernetes manifests and configs)
├── helm-charts
│   └── nginx
│       └── ... (NGINX Helm chart files)
├── controllers
│   └── ... (Operator logic)
├── Dockerfile
├── Makefile
└── PROJECT
```

### Step 3: Customize the Operator

Time to hack! 🎨 You can customize the reconciliation logic to add extra steps, like configuring SSL or setting up custom logging.

Here’s an example of adding a custom pre-install job:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: configure-nginx
spec:
  template:
    spec:
      containers:
      - name: configure
        image: busybox
        command: ['sh', '-c', 'echo "Custom NGINX configuration applied!"']
      restartPolicy: OnFailure
```

### Step 4: Integrate with Flux for GitOps

Now, create a `HelmRelease` resource for Flux to deploy NGINX:

```yaml
apiVersion: helm.fluxcd.io/v1
kind: HelmRelease
metadata:
  name: nginx-release
  namespace: default
spec:
  releaseName: nginx
  chart:
    git: git@github.com:myorg/nginx-helm-chart.git
    ref: master
    path: helm-charts/nginx
  values:
    service:
      type: LoadBalancer
    replicaCount: 2
```

Push this file to your Git repo, and Flux will automatically deploy NGINX. 🌟

### Step 5: Deploy and Test

Deploy your operator and check if NGINX is running:

```bash
make deploy
```

Check the service by accessing the LoadBalancer IP in your browser. Your NGINX server should be up and running!

## 🐱‍💻 Example 2: Deploying Apache Tomcat with a Custom Helm Operator

Next, let’s deploy Apache Tomcat, a widely-used web server and servlet container.

### Step 1: Scaffold a New Helm-Based Operator

Create a new operator for Apache Tomcat:

```bash
operator-sdk init --plugins helm --domain mydomain.com --group web --version v1 --kind TomcatOperator
```

### Step 2: Add the Tomcat Helm Chart

Download and place the Tomcat Helm chart in your project:

```bash
mkdir -p helm-charts/tomcat
helm pull bitnami/tomcat --untar --untardir helm-charts/tomcat
```

Your folder structure now looks like this:

```
.
├── config
├── helm-charts
│   ├── nginx
│   │   └── ... (NGINX Helm chart files)
│   └── tomcat
│       └── ... (Tomcat Helm chart files)
├── controllers
├── Dockerfile
├── Makefile
└── PROJECT
```

### Step 3: Customize the Operator

Customize the Helm chart by adding your specific configurations, like setting Java options or integrating with a database.

Here’s an example of setting a custom Java option:

```yaml
env:
  - name: JAVA_OPTS
    value: "-Dcustom.property=value"
```

### Step 4: Integrate with Flux for GitOps

Create a `HelmRelease` for deploying Tomcat with Flux:

```yaml
apiVersion: helm.fluxcd.io/v1
kind: HelmRelease
metadata:
  name: tomcat-release
  namespace: default
spec:
  releaseName: tomcat
  chart:
    git: git@github.com:myorg/tomcat-helm-chart.git
    ref: master
    path: helm-charts/tomcat
  values:
    service:
      type: LoadBalancer
    replicaCount: 2
    image:
      repository: bitnami/tomcat
      tag: "9.0.48"
```

### Step 5: Deploy and Test

Deploy your Tomcat operator and verify it’s working:

```bash
make deploy
```

Access Tomcat by hitting the LoadBalancer IP in your browser, and you should see the familiar Tomcat homepage. 🚀

## 🧠 Example 3: Deploying Redis with a Custom Helm Operator

Finally, let’s deploy Redis, a popular in-memory data structure store.

### Step 1: Scaffold a New Helm-Based Operator

Create a new operator for Redis:

```bash
operator-sdk init --plugins helm --domain mydomain.com --group data --version v1 --kind RedisOperator
```

### Step 2: Add the Redis Helm Chart

Download and place the Redis Helm chart:

```bash
mkdir -p helm-charts/redis
helm pull bitnami/redis --untar --untardir helm-charts/redis
```

Your folder structure now includes Redis:

```
.
├── config
├── helm-charts
│   ├── nginx
│   ├── tomcat
│   └── redis
│       └── ... (Redis Helm chart files)
├── controllers
├── Dockerfile
├── Makefile
└── PROJECT
```

### Step 3: Customize the Operator

You might want to customize the Redis deployment for high availability, set up persistence, or tweak performance settings.

For example, enabling persistence:

```yaml
persistence:
  enabled: true
  size: 8Gi
  storageClass: "standard"
```

### Step 4: Integrate with Flux for GitOps

Create a `HelmRelease` for deploying Redis:

```yaml
apiVersion: helm.fluxcd.io/v1
kind: HelmRelease
metadata:
  name: redis-release
  namespace: default
spec:
  releaseName: redis
  chart:
    git: git@github.com:myorg/redis-helm-chart.git
    ref: master
    path: helm-charts/redis
  values:
    cluster:
      enabled: true
    replica:
      replicaCount: 3
```

### Step 5: Deploy and Test

Deploy your Redis operator and check its status:

```bash
make deploy
```

Your Redis instance should be running, with persistence and replication enabled! 🎉

## 🎁 Making Services Self-Installable

To make your services truly self-installable:

- **Automate Dependencies**: Ensure all dependencies, like databases or SSL certs, are automatically handled by the operator.
- **Self-Configuration**: Use ConfigMaps and Secrets to automatically configure services based on the environment.
- **Scalability**: Implement autoscaling features directly in your Helm charts or operator logic.

## 📚 Conclusion

By hacking the Helm Operator using the Operator SDK and integrating with Flux, you can create self-installable services that make deploying and managing applications like NGINX, Apache Tomcat, and Redis effortless. This approach embraces GitOps principles, ensuring your Kubernetes deployments are reliable, scalable, and consistent.

So go ahead, try out these examples, customize them, and see how this powerful combination can simplify your cloud-native journey. Happy clustering! 🚀
