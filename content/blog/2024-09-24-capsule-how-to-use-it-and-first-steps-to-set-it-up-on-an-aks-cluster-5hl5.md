---
title: "Capsule: How to Use It and First Steps to Set It Up on an AKS Cluster 🚀"
date: 2024-09-24T19:24:03+00:00
description: "Capsule is an awesome, open-source solution that helps you manage multiple tenants in Kubernetes..."
tags: ["kubernetes", "cloud", "azure", "cloudnative"]
draft: false
slug: "capsule-how-to-use-it-and-first-steps-to-set-it-up-on-an-aks-cluster-5hl5"
devto_id: 2013406
devto_url: "https://dev.to/hkhelil/capsule-how-to-use-it-and-first-steps-to-set-it-up-on-an-aks-cluster-5hl5"
---
Capsule is an awesome, open-source solution that helps you manage multiple tenants in Kubernetes clusters, making it super easy to handle multi-tenancy. Whether you’re running Kubernetes for a big company or providing services for others, Capsule ensures your clusters stay organized and secure!

In this guide, we’ll dive into what Capsule is, why it’s a great choice, and show you how to set it up on an Azure Kubernetes Service (AKS) cluster. Ready? Let’s go! 🎉

## What is Capsule? 🤔

Capsule adds an extra layer on top of Kubernetes, making it easier for you to manage multiple tenants. These tenants get their own space, resources, and security without interfering with each other. Some cool features of Capsule include:

- **Tenant Isolation**: Each tenant gets its own sandbox, so they don’t step on each other’s toes. 🚧
- **Resource Quotas**: You can limit how much CPU, memory, and other resources each tenant can use. No more hogging! 🐷
- **Namespace Management**: Tenants can create and manage their own namespaces, keeping things tidy. 🗂️
- **Security Policies**: Capsule ensures that each tenant has its own security settings, keeping everything safe. 🔒
- **Cluster Sharing**: You can share the same Kubernetes cluster with multiple tenants while keeping them separated. 🌐

## Why Should You Use Capsule? 💡

1. **Multi-tenancy Made Easy**: Capsule makes managing tenants a breeze, giving you better control over shared clusters.
2. **Efficient Resource Use**: Share resources among tenants without worrying about one tenant taking everything.
3. **Top-notch Security**: Keep tenants isolated with network and security policies.
4. **Centralized Management**: Simplifies managing Kubernetes resources by organizing them under tenants.

### Capsule’s Architecture

Capsule operates as a Kubernetes controller, managing tenants using Capsule Custom Resource Definitions (CRDs). When you create a new tenant, Capsule links it to specific namespaces, ensuring isolation. Plus, it enforces policies to keep everything in check. Easy-peasy! 🌟

## Setting Up Capsule on an AKS Cluster 🔧

Let’s walk through the steps of getting Capsule up and running on your AKS cluster.

### Prerequisites ✅

Make sure you have the following set up:

1. **Azure CLI**: Installed and logged in to your Azure account.
2. **kubectl**: Installed and configured to work with your AKS cluster.
3. **Helm**: Installed for managing packages in Kubernetes.

### Step 1: Create Your AKS Cluster ☁️

If you don’t have an AKS cluster yet, create one using Azure CLI:

```bash
az aks create --resource-group <RESOURCE_GROUP> --name <CLUSTER_NAME> --node-count 3 --enable-managed-identity --generate-ssh-keys
```

Now connect to your AKS cluster:

```bash
az aks get-credentials --resource-group <RESOURCE_GROUP> --name <CLUSTER_NAME>
```

Check that you’re connected by listing your nodes:

```bash
kubectl get nodes
```

### Step 2: Install Cert-Manager 🔑

Capsule requires **cert-manager** to handle certificates for webhooks. Install cert-manager using Helm:

```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.10.1 --set installCRDs=true
```

Ensure that cert-manager is running:

```bash
kubectl get pods --namespace cert-manager
```

### Step 3: Install Capsule 🎯

Now let’s install Capsule! You can use Helm for this:

```bash
helm repo add clastix https://clastix.github.io/charts
helm repo update
helm install capsule clastix/capsule --namespace capsule-system --create-namespace
```

Check that Capsule is installed:

```bash
kubectl get pods --namespace capsule-system
```

### Step 4: Create a Tenant 🏢

With Capsule installed, let’s create your first tenant! Here's an example of a `Tenant` resource:

```yaml
apiVersion: capsule.clastix.io/v1alpha1
kind: Tenant
metadata:
  name: my-tenant
spec:
  owners:
    - kind: User
      name: john@example.com
  namespacesMetadata:
    additionalMetadata:
      labels:
        owner: john@example.com
```

Save this as `tenant.yaml` and apply it:

```bash
kubectl apply -f tenant.yaml
```

Boom! You’ve just created your first tenant 🎉

### Step 5: Verify Your Tenant 🧐

To confirm your tenant was created, run:

```bash
kubectl get tenants
```

You should see your brand-new tenant listed!

### Step 6: Set Resource Limits 💪

Capsule allows you to assign resource quotas to each tenant. Update the tenant definition to include CPU and memory limits:

```yaml
spec:
  resourceQuotas:
    - hard:
        requests.cpu: "4"
        requests.memory: "8Gi"
        limits.cpu: "8"
        limits.memory: "16Gi"
```

Apply the updated tenant:

```bash
kubectl apply -f tenant.yaml
```

This makes sure your tenant stays within its resource limits! 🎛️

### Step 7: Let Tenants Manage Their Namespaces 📂

You can let tenants create and manage their namespaces! Add the following to your tenant definition:

```yaml
spec:
  namespacesMetadata:
    additionalMetadata:
      annotations:
        capsule.clastix.io/allowed-namespaces-range: "^mytenant-.*"
```

This ensures tenants can only create namespaces with a specific prefix, keeping things organized!

## Examples for a Shared Kubernetes Cluster 🌍

In a shared Kubernetes cluster, tenants can coexist but maintain separation in terms of resources and namespaces. Capsule helps ensure this, but let’s look at a few examples of how you can configure a shared cluster.

### 1. Shared Infrastructure for Multiple Teams 🏢

Imagine you're running Kubernetes for multiple development teams, like Team A and Team B, on a shared AKS cluster. Capsule allows you to create separate tenants for each team, and each team can manage its own namespaces, but they can’t interfere with each other.

Here’s how you can define tenants for both teams:

```yaml
apiVersion: capsule.clastix.io/v1alpha1
kind: Tenant
metadata:
  name: team-a
spec:
  owners:
    - kind: User
      name: team-a-admin@example.com
  namespacesMetadata:
    additionalMetadata:
      labels:
        team: team-a
---
apiVersion: capsule.clastix.io/v1alpha1
kind: Tenant
metadata:
  name: team-b
spec:
  owners:
    - kind: User
      name: team-b-admin@example.com
  namespacesMetadata:
    additionalMetadata:
      labels:
        team: team-b
```

Each team gets its own tenant with an admin user who can manage the namespaces. You can also set resource quotas for each team to prevent overuse:

```yaml
spec:
  resourceQuotas:
    - hard:
        requests.cpu: "6"
        requests.memory: "10Gi"
        limits.cpu: "12"
        limits.memory: "20Gi"
```

### 2. Tenant-Specific Network Policies 🔐

In a shared environment, you might want to restrict network access between tenants. With Capsule, you can set network policies that prevent one tenant from communicating with another tenant’s resources:

```yaml
spec:
  networkPolicies:
    egress:
      - to:
          namespaceSelector:
            matchLabels:
              capsule.clastix.io/tenant: team-a
        ports:
          - protocol: TCP
            port: 80
```

This ensures that only specific network traffic is allowed between tenants, keeping resources safe and secure.

### 3. Shared Services Across Tenants ⚙️

Sometimes, tenants need access to shared services (like a database). Capsule allows for such shared services while maintaining isolation for other resources:

```yaml
spec:
  additionalRoleBindings:
    - roleRef:
        apiGroup: rbac.authorization.k8s.io
        kind: ClusterRole
        name: shared-service-access
      subjects:
        - kind: User
          name: team-a
        - kind: User
          name: team-b
```

This allows Team A and Team B to access a shared database service without violating the isolation of other resources within the cluster.

## Wrapping Up 🎁

Capsule is a fantastic tool for managing multi-tenancy in Kubernetes. With features like tenant isolation, resource quotas, and namespace control, it takes the complexity out of handling multiple users or teams in a single cluster.

By following the steps in this guide, you’ve set up Capsule on your AKS cluster and created your first tenant! Now you can manage tenants with ease and scale your Kubernetes infrastructure confidently. 🌟

Happy clustering !
