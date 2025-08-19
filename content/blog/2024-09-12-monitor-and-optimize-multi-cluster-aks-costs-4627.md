---
title: "Monitor and Optimize Multi-Cluster AKS Costs 💰"
date: 2024-09-12T07:42:06+00:00
description: As businesses scale their Kubernetes workloads across multiple Azure Kubernetes Service (AKS)...
tags: ["kubernetes", "cloud", "azure", "finops"]
draft: false
slug: "monitor-and-optimize-multi-cluster-aks-costs-4627"
devto_id: 1996432
devto_url: "https://dev.to/hkhelil/monitor-and-optimize-multi-cluster-aks-costs-4627"
---
As businesses scale their Kubernetes workloads across multiple Azure Kubernetes Service (AKS) clusters, managing and optimizing cloud costs becomes critical. Deploying and managing observability tools such as KubeCost and OpenTelemetry (OTel) across multiple clusters can be simplified using [AKS Fleet Manager](https://github.com/Azure/fleet/blob/main/docs/concepts/README.md), Microsoft Managed Prometheus, and Grafana.

This guide will explain how to:

1. Deploy **KubeCost** and **OpenTelemetry** across multiple AKS clusters using **AKS Fleet Manager**.  
2. Expose metrics through OpenTelemetry.  
3. Centralize monitoring via **Managed Prometheus** and **Grafana**.

You’ll gain a single-pane-of-glass view into your multi-cluster environment, enabling more efficient resource utilization and cost management.

## What is KubeCost? 🧮

**KubeCost** is an open-source cost management tool that provides real-time visibility into your Kubernetes spend. It gives a granular breakdown (namespaces, deployments, services, pods) so you can optimize resource usage and reduce expenses.

## Why Use AKS Fleet Manager? 🌐

[**AKS Fleet Manager**](https://github.com/Azure/fleet/blob/main/docs/concepts/README.md) simplifies multi-cluster Kubernetes management by providing a centralized way to define governance, policies, and monitoring. Instead of manually configuring each cluster, you can orchestrate deployments (like KubeCost and OpenTelemetry) across multiple AKS clusters at once.

## Why Use OpenTelemetry, Managed Prometheus, and Grafana? 📊

- **OpenTelemetry (OTel)**: Standardizes observability, collecting metrics, logs, and traces from Kubernetes workloads and exposing them to monitoring systems (like Prometheus).  
- **Microsoft Managed Prometheus**: A fully managed Prometheus service that removes the overhead of maintaining Prometheus infrastructure.  
- **Grafana**: A robust visualization tool that integrates with Prometheus to present metrics in customizable dashboards.

Using these in conjunction with AKS Fleet Manager allows you to centrally monitor, troubleshoot, and optimize costs across your entire AKS fleet.

## Step-by-Step: Deploy KubeCost and OpenTelemetry with AKS Fleet Manager 🔧

### Step 1: Create and Register AKS Clusters

1. **Create your AKS clusters** (using CLI or Portal).  
2. **Register each AKS cluster** with AKS Fleet Manager. (See also: [MemberCluster docs](https://github.com/Azure/fleet/blob/main/docs/concepts/MemberCluster/README.md))

#### 1.1 Create AKS Clusters

Example using the Azure CLI:

```bash
# Create a resource group for AKS Fleet Manager
az group create --name myFleetResourceGroup --location eastus

# Create two AKS clusters in different resource groups
az aks create \
  --resource-group myResourceGroup1 \
  --name myAKSCluster1 \
  --node-count 3 \
  --enable-managed-identity \
  --generate-ssh-keys

az aks create \
  --resource-group myResourceGroup2 \
  --name myAKSCluster2 \
  --node-count 3 \
  --enable-managed-identity \
  --generate-ssh-keys
```

#### 1.2 Register Clusters with AKS Fleet Manager

Once your clusters are ready, register them with your existing Fleet Manager instance:

```bash
# Register the first AKS cluster with Fleet Manager
az fleet member create \
  --resource-group myFleetResourceGroup \
  --fleet-name myFleetManager \
  --name myAKSCluster1 \
  --member-cluster-id /subscriptions/{subscription-id}/resourceGroups/myResourceGroup1/providers/Microsoft.ContainerService/managedClusters/myAKSCluster1

# Register the second AKS cluster
az fleet member create \
  --resource-group myFleetResourceGroup \
  --fleet-name myFleetManager \
  --name myAKSCluster2 \
  --member-cluster-id /subscriptions/{subscription-id}/resourceGroups/myResourceGroup2/providers/Microsoft.ContainerService/managedClusters/myAKSCluster2
```

> **Note**: Replace `{subscription-id}` with your actual subscription ID.

### Step 2: Create HelmRelease Manifests for KubeCost and OpenTelemetry

AKS Fleet Manager uses Flux-like semantics for delivering resources to your member clusters. You can define **HelmRelease** manifests to install KubeCost and the OTel Collector and then use [**ClusterResourcePlacement**](https://github.com/Azure/fleet/blob/main/docs/concepts/ClusterResourcePlacement/README.md) to distribute them to your clusters.

#### 2.1 Define a HelmRelease for KubeCost

Create a file named `kubecost-helmrelease.yaml`:

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: kubecost
  namespace: kubecost
spec:
  releaseName: kubecost
  chart:
    repository: https://kubecost.github.io/cost-analyzer/
    name: cost-analyzer
    version: 1.90.1
  interval: 1m
  install:
    createNamespace: true
  values:
    kubecostProductConfigs:
      prometheus: true
    networkPolicy:
      enabled: true
```

This HelmRelease configures KubeCost in a `kubecost` namespace.

#### 2.2 Define a HelmRelease for OpenTelemetry

Create a file named `otel-collector-helmrelease.yaml`:

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: otel-collector
  namespace: otel-collector
spec:
  releaseName: otel-collector
  chart:
    repository: https://open-telemetry.github.io/opentelemetry-helm-charts
    name: opentelemetry-collector
    version: 0.31.0
  interval: 1m
  install:
    createNamespace: true
  values:
    config:
      receivers:
        prometheus:
          scrape_configs:
            - job_name: 'kubecost'
              metrics_path: /metrics
              static_configs:
                - targets: ['kubecost-cost-analyzer.kubecost.svc.cluster.local:9090']
      exporters:
        otlp:
          endpoint: "managed-prometheus-endpoint:4317"  # Update with your actual endpoint
          tls:
            insecure: true
      service:
        pipelines:
          metrics:
            receivers: [prometheus]
            exporters: [otlp]
```

This config sets up the OpenTelemetry Collector to scrape metrics from KubeCost and forward them to your Managed Prometheus endpoint.

### Step 3: Create a ClusterResourcePlacement to Distribute HelmReleases

Now that you have your HelmReleases defined, use a **ClusterResourcePlacement** to distribute them to the clusters managed by AKS Fleet Manager. (See also: [ClusterResourcePlacement docs](https://github.com/Azure/fleet/blob/main/docs/concepts/ClusterResourcePlacement/README.md))

Create a file named `crp-kubecost-otel.yaml`:

```yaml
apiVersion: fleet.azure.com/v1alpha1
kind: ClusterResourcePlacement
metadata:
  name: cost-and-otel-placement
spec:
  # Select all clusters in your Fleet, or specify labels under 'matchLabels'
  clusterSelector:
    matchLabels: {}

  # (Optional) Additional policy or scheduling parameters can go here
  # policy:
  #   ...

  resourceSelectors:
    # Reference the KubeCost HelmRelease
    - kind: HelmRelease
      apiVersion: helm.toolkit.fluxcd.io/v2
      name: kubecost
      namespace: kubecost

    # Reference the OTel HelmRelease
    - kind: HelmRelease
      apiVersion: helm.toolkit.fluxcd.io/v2
      name: otel-collector
      namespace: otel-collector
```

### Step 4: Apply These Resources to Your Fleet Manager

You can now apply these files to the **Fleet Manager** cluster, which is typically the control plane for your multi-cluster environment.

```bash
# Apply the HelmRelease for KubeCost
kubectl apply -f kubecost-helmrelease.yaml

# Apply the HelmRelease for OTel Collector
kubectl apply -f otel-collector-helmrelease.yaml

# Apply the ClusterResourcePlacement
kubectl apply -f crp-kubecost-otel.yaml
```

AKS Fleet Manager will propagate these HelmReleases to each selected cluster (based on the `clusterSelector`) and install KubeCost and OpenTelemetry automatically.

### Step 5: Configure Microsoft Managed Prometheus

With the OpenTelemetry Collector set up in each cluster, Managed Prometheus will receive metrics from the OTLP endpoint.

1. In the **Azure Portal**, go to **Monitoring** > **Metrics** in each AKS cluster.  
2. **Enable Managed Prometheus** for each cluster.  

Once enabled, your Managed Prometheus instance will begin receiving metrics from each cluster via OpenTelemetry.

### Step 6: Set Up Centralized Visualization in Managed Grafana

To visualize metrics and costs across your AKS fleet, set up Managed Grafana to connect to Managed Prometheus.

1. **Create a Managed Grafana Workspace**  
   - In the Azure portal, navigate to **Azure Managed Grafana** and create a workspace.

2. **Add a Prometheus Data Source**  
   - In the Grafana instance, go to **Configuration** > **Data Sources**.  
   - Add **Prometheus** as a data source and provide the Managed Prometheus endpoint URL.

3. **Import KubeCost Dashboards**  
   - In Grafana, go to **Dashboards** > **Manage** > **Import**.  
   - Use KubeCost’s provided dashboard IDs or JSON files to import their predefined dashboards for cost analysis.

### Step 7: Monitor and Analyze Costs Across Clusters 📈

With everything configured, you can now:

- **View Cost Allocations** by namespaces, deployments, or pods using KubeCost metrics.  
- **Track Metrics** (CPU, memory, etc.) from all clusters in a single Grafana instance.  
- **Identify Inefficiencies** and optimize resource usage using dashboards and Prometheus queries.

Example PromQL query for **cost allocation by namespace**:

```promql
sum(kubecost_allocation{label_namespace!=""}) by (label_namespace)
```

Example PromQL query for **cross-cluster cost efficiency by deployment**:

```promql
sum(rate(kubecost_allocation{label_deployment!=""}[5m])) by (label_deployment, cluster) 
/ 
sum(rate(container_cpu_usage_seconds_total{job="kubelet", container!="POD"}[5m])) by (pod, namespace, cluster)
```

### Step 8: Implement Best Practices for Security and Performance 🔒

- **Enable TLS** for communication between OpenTelemetry Collectors and Managed Prometheus (remove `insecure: true` in production).  
- **Limit Network Access** to ensure that only authorized users and systems can access Prometheus and Grafana endpoints.  
- **Set Resource Limits** on your OpenTelemetry Collectors and KubeCost Pods to prevent resource overuse.

## Conclusion 🎯

By leveraging [**AKS Fleet Manager**](https://github.com/Azure/fleet/blob/main/docs/concepts/README.md) with [**ClusterResourcePlacement**](https://github.com/Azure/fleet/blob/main/docs/concepts/ClusterResourcePlacement/README.md) to distribute HelmReleases for **KubeCost** and **OpenTelemetry**, and centralizing metrics in **Managed Prometheus** and **Grafana**, you’ll streamline cost management and observability across multiple AKS clusters.

- **Single-Pane Monitoring**: All cost and performance data in one place.  
- **Simplicity at Scale**: AKS Fleet Manager handles deploying resources to multiple clusters.  
- **Actionable Insights**: Use Grafana dashboards to pinpoint inefficiencies and optimize usage.

Start implementing this multi-cluster monitoring solution today to gain comprehensive control over your Kubernetes spending!

**Happy clustering!** 🌟
