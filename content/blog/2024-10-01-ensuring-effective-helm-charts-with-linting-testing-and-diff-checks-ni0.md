---
title: "Ensuring Effective Helm Charts with Linting, Testing, and Diff Checks 🚀"
date: 2024-10-01T16:25:51+00:00
description: "When deploying applications to Kubernetes, using Helm charts is a great way to simplify the process...."
tags: ["kubernetes", "cloud", "github", "githubactions"]
draft: false
slug: "ensuring-effective-helm-charts-with-linting-testing-and-diff-checks-ni0"
devto_id: 2022055
devto_url: "https://dev.to/hkhelil/ensuring-effective-helm-charts-with-linting-testing-and-diff-checks-ni0"
---
When deploying applications to Kubernetes, using Helm charts is a great way to simplify the process. But how do you make sure your Helm charts are high-quality and won’t cause issues down the line? Don’t worry! In this guide, we’ll show you how to:

- Use **Helm Chart-Testing** for linting and validation 🕵️‍♀️
- Perform **Unit Testing** with the Helm Unit Test plugin 🔧
- Use **Helm Diff** to check changes before installing or upgrading 🚦

By following these steps, you’ll catch potential issues early and ensure smooth deployments. We’ll also build a fully tested **NGINX Helm chart** at the end!

## 1. Linting and Validation with Helm Chart-Testing 🛠️

Linting helps ensure your Helm charts follow best practices. For this, we use **[Helm Chart-Testing (ct)](https://github.com/helm/chart-testing)**, a more robust tool than the basic `helm lint`.

### Install Helm Chart-Testing

You can install it via Homebrew:

```bash
brew install helm chart-testing
```

Or via Docker:

```bash
docker pull quay.io/helmpack/chart-testing
```

### Running Helm Chart-Testing

Once installed, you can lint your chart:

```bash
ct lint --charts ./charts/
```

This performs validation checks and ensures your chart adheres to best practices before moving to the next step.

## 2. Unit Testing with Helm Unit Test Plugin 🔧

The **[Helm Unit Test plugin](https://github.com/quintush/helm-unittest)** helps test how your templates behave under different configurations. It’s an easy way to verify that your charts work as expected.

### Install Helm Unit Test Plugin

First, install the plugin:

```bash
helm plugin install https://github.com/quintush/helm-unittest
```

### Writing Unit Tests

Create a `tests/unittest.yaml` file to define tests. Here's an example:

```yaml
suite: Test suite for NGINX chart
templates:
  - deployment.yaml

tests:
  - it: Should render a valid Deployment resource
    set:
      replicaCount: 2
    asserts:
      - isKind:
          of: Deployment
      - equal:
          path: metadata.name
          value: nginx-deployment
```

### Running Unit Tests

Run the unit tests:

```bash
helm unittest ./charts/nginx
```

## 3. Validating Changes with Helm Diff 🔍

Before applying any changes to your Kubernetes cluster, it’s important to see what will change. The **[Helm Diff plugin](https://github.com/databus23/helm-diff)** lets you compare the existing state with the new deployment.

### Install Helm Diff Plugin

Install the plugin with:

```bash
helm plugin install https://github.com/databus23/helm-diff
```

### Using Helm Diff

Check the changes that will occur before upgrading:

```bash
helm diff upgrade nginx ./charts/nginx --values ./values.yaml
```

## 4. Example: NGINX Deployment Helm Chart 🚀

Here’s how you can apply everything we’ve discussed to deploy an NGINX server with Helm.

### Step 1: Create an NGINX Helm Chart

Create a basic NGINX chart:

```bash
helm create nginx
```

### Step 2: Customize the `deployment.yaml` Template

Edit the `nginx/templates/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "nginx.fullname" . }}
  labels:
    app: {{ include "nginx.name" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include "nginx.name" . }}
  template:
    metadata:
      labels:
        app: {{ include "nginx.name" . }}
    spec:
      containers:
      - name: nginx
        image: "nginx:stable"
        ports:
        - containerPort: 80
```

### Step 3: Write Unit Tests

Add unit tests in `tests/unittest.yaml`:

```yaml
suite: Test suite for NGINX chart
templates:
  - deployment.yaml

tests:
  - it: Should render an NGINX deployment with 3 replicas
    set:
      replicaCount: 3
    asserts:
      - isKind:
          of: Deployment
      - equal:
          path: metadata.name
          value: nginx
      - equal:
          path: spec.replicas
          value: 3
```

### Step 4: Run Lint, Unit Tests, and Helm Diff

- **Lint**: Run Helm Chart-Testing to check your chart:

  ```bash
  ct lint --charts ./nginx/
  ```

- **Unit Test**: Ensure your templates behave as expected:

  ```bash
  helm unittest ./nginx/
  ```

- **Diff**: Check the changes before upgrading:

  ```bash
  helm diff upgrade nginx ./nginx --values ./nginx/values.yaml
  ```

### Step 5: Deploy the Helm Chart

Finally, deploy your NGINX Helm chart:

```bash
helm install nginx ./nginx --values ./nginx/values.yaml
```

## 5. Example GitHub Action for Helm Linting, Testing, and Diffing 🛠️

Now that you’ve learned the basics, let’s automate the whole process using **GitHub Actions**! Below is an example workflow that automates linting, testing, and diff checks for your Helm charts. This ensures your charts are always validated before merging to the main branch.

```yaml
name: Helm Chart CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  helm-chart-testing:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v2
    
    - name: Set up Helm
      run: |
        curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
    
    - name: Install Helm plugins (Unit Test, Diff)
      run: |
        helm plugin install https://github.com/quintush/helm-unittest
        helm plugin install https://github.com/databus23/helm-diff
    
    - name: Run Helm Chart-Testing Lint
      run: |
        ct lint --charts ./nginx/
    
    - name: Run Helm Unit Tests
      run: |
        helm unittest ./nginx/
    
    - name: Check for Changes with Helm Diff
      run: |
        helm diff upgrade nginx ./nginx --values ./nginx/values.yaml
```

### Explanation:

1. **Trigger**: The action runs on every push or pull request to the `main` branch.
2. **Helm Setup**: Installs Helm and necessary plugins for unit testing and diff checks.
3. **Linting**: Runs Helm Chart-Testing lint on the chart.
4. **Unit Testing**: Runs Helm Unit Test to ensure templates behave as expected.
5. **Diff Check**: Compares the current Helm release with the proposed changes using Helm Diff.

## Conclusion 🎉

By combining **Helm Chart-Testing**, **Helm Unit Test**, and **Helm Diff**, you can ensure that your Helm charts are written effectively and behave as expected before deployment. With the example GitHub Action, you can automate this process and keep your CI/CD pipeline smooth.

Explore these awesome tools on GitHub:

- [Helm Chart-Testing](https://github.com/helm/chart-testing) 🛠️
- [Helm Unit Test Plugin](https://github.com/quintush/helm-unittest) 🔧
- [Helm Diff Plugin](https://github.com/databus23/helm-diff) 🔍

Integrate them into your CI/CD pipeline to ensure smoother Kubernetes deployments. Happy charting! 🚀
