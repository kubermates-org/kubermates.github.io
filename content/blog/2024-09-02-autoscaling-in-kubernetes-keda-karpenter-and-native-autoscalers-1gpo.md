---
title: "Autoscaling in Kubernetes: KEDA, Karpenter, and Native Autoscalers"
date: 2024-09-02T11:41:41+00:00
description: "Autoscaling is a critical component of any robust Kubernetes environment, ensuring your applications..."
tags: ["kubernetes", "cloud", "opensource", "aws"]
draft: false
slug: "autoscaling-in-kubernetes-keda-karpenter-and-native-autoscalers-1gpo"
devto_id: 1977165
devto_url: "https://dev.to/hkhelil/autoscaling-in-kubernetes-keda-karpenter-and-native-autoscalers-1gpo"
---
Autoscaling is a critical component of any robust Kubernetes environment, ensuring your applications and infrastructure can dynamically adjust to meet demand. In this guide, we'll explore three powerful autoscaling tools: **KEDA** for event-driven pod autoscaling, **Karpenter** for dynamic node scaling, and Kubernetes' native autoscalers (HPA and VPA). We'll dive into how to use them effectively, with plenty of examples to get you started. 🚀

## Introduction to KEDA 🚀

KEDA (Kubernetes-based Event Driven Autoscaling) allows you to scale applications based on custom event metrics, not just CPU or memory usage. It’s ideal for scenarios where workloads are triggered by external events, such as message queues, databases, or HTTP requests. Whether you're processing incoming orders, reacting to sensor data, or scaling based on custom Prometheus metrics, KEDA has you covered! 💥

## How to Use KEDA in Kubernetes

Setting up KEDA involves a few key steps:

### 1. Installing KEDA 🎉

Install KEDA using Helm:

```bash
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
helm install keda kedacore/keda --namespace keda --create-namespace
```

Verify the installation:

```bash
kubectl get pods -n keda
```

### 2. Setting Up a ScaledObject Example 🎯

Here’s an example `ScaledObject` for scaling an app based on an Azure Service Bus queue:

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: azure-servicebus-queue-scaler
  namespace: default
spec:
  scaleTargetRef:
    name: my-app
  minReplicaCount: 0
  maxReplicaCount: 10
  triggers:
  - type: azure-servicebus
    metadata:
      queueName: my-queue
      connection: "SERVICEBUS_CONNECTION_STRING"
      queueLength: "5"
```

This configuration scales `my-app` based on the number of messages in `my-queue`. If there are five or more messages, KEDA will scale up the pods. If there are no messages, it can even scale down to zero, saving resources! 🛑

### 3. Deploying Your Application 🛠️

Deploy your application as usual, ensuring it’s configured to process events from the source you defined in your `ScaledObject`.

## Other KEDA Examples to Explore 🔍

**Scaling with RabbitMQ** 🐰

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: rabbitmq-queue-scaler
  namespace: default
spec:
  scaleTargetRef:
    name: my-rabbitmq-app
  triggers:
  - type: rabbitmq
    metadata:
      queueName: my-queue
      host: "amqp://guest:guest@rabbitmq.default.svc.cluster.local:5672"
      queueLength: "10"
```

**Scaling with Prometheus** 📊

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: prometheus-scaler
  namespace: default
spec:
  scaleTargetRef:
    name: my-prometheus-app
  triggers:
  - type: prometheus
    metadata:
      serverAddress: "http://prometheus.default.svc.cluster.local:9090"
      metricName: http_requests_total
      threshold: "100"
```

## Native Kubernetes Autoscalers: HPA and VPA 🤖

Kubernetes offers two primary autoscalers out of the box:

### Horizontal Pod Autoscaler (HPA)

The **HPA** scales pods horizontally based on CPU or memory usage:

```bash
kubectl autoscale deployment my-app --cpu-percent=50 --min=1 --max=10
```

This command sets up an autoscaler for the `my-app` deployment that scales between 1 and 10 pods, aiming to keep CPU usage at 50%. ⚖️

### Vertical Pod Autoscaler (VPA)

The **VPA** optimizes resource requests for containers, adjusting CPU and memory allocations as needed:

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind:       Deployment
    name:       my-app
  updatePolicy:
    updateMode: "Auto"
```

## KEDA vs. Kubernetes Default Autoscalers: A Quick Comparison 🥊

| Feature                        | Kubernetes HPA/VPA                        | KEDA                                           |
|--------------------------------|-------------------------------------------|------------------------------------------------|
| **Scaling Metrics**            | CPU and memory                            | Custom metrics from event sources 📈           |
| **Event-driven Autoscaling**   | No                                        | Yes 📨                                         |
| **Scale to Zero**              | No                                        | Yes 🛑                                         |
| **Trigger Sources**            | Limited                                   | Extensive (e.g., queues, databases, APIs) 🌐   |
| **Setup Complexity**           | Simple                                    | Slightly more complex but very flexible 🔧     |

## Introduction to Karpenter: Dynamic Node Scaling 🌩️

Karpenter is an open-source Kubernetes cluster autoscaler designed by AWS. It dynamically provisions and manages nodes to ensure your cluster has the capacity to run all required pods. Unlike the Kubernetes Cluster Autoscaler, Karpenter is faster and more flexible, making it ideal for environments that use diverse instance types or spot instances. 🌟

## How to Use Karpenter

### 1. Install Karpenter 🛠️

To install Karpenter, follow these steps:

1. Set up the IAM role and service account for Karpenter (if you're on AWS).
2. Install the Karpenter controller:

```bash
helm repo add karpenter https://charts.karpenter.sh
helm repo update
helm install karpenter karpenter/karpenter --namespace karpenter --create-namespace
```

3. Apply a Provisioner configuration that defines how Karpenter should scale nodes.

### 2. Configure a Provisioner Example ⚙️

Here’s an example of a Karpenter `Provisioner` that uses spot instances:

```yaml
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: default
spec:
  requirements:
    - key: "node.kubernetes.io/instance-type"
      operator: In
      values: ["t3a.medium", "t3a.large"]
    - key: "karpenter.sh/capacity-type"
      operator: In
      values: ["spot"]
  provider:
    cluster:
      name: my-cluster
    endpoint: https://EKS_CLUSTER_ENDPOINT
  ttlSecondsAfterEmpty: 30
```

This `Provisioner` tells Karpenter to scale using spot instances of types `t3a.medium` and `t3a.large`. The `ttlSecondsAfterEmpty` field ensures that nodes are terminated 30 seconds after they become empty, optimizing cost efficiency. 💸

### 3. Deploy a Workload to Trigger Scaling 🚀

Deploy an application that requires more resources than your current nodes provide:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: large-app
spec:
  replicas: 10
  template:
    spec:
      containers:
      - name: large-container
        image: large-app-image
        resources:
          requests:
            cpu: "500m"
            memory: "512Mi"
```

When this deployment is applied, Karpenter will automatically provision additional nodes to accommodate the increased resource demand.

## KEDA vs. Karpenter: A Synergistic Approach ⚖️

- **KEDA** scales **pods** within a Kubernetes cluster based on event-driven metrics, while **Karpenter** scales **nodes** to ensure there’s enough capacity to run those pods.
- If KEDA triggers a rapid scale-up of pods due to a surge in events (like an influx of messages in a queue), Karpenter can quickly provision additional nodes to handle the increased load.
- Using both KEDA and Karpenter together ensures your Kubernetes environment is highly responsive, scalable, and cost-efficient.

## When to Use KEDA, Karpenter, or Both?

- **KEDA** is ideal for event-driven pod autoscaling, especially in microservices, queue processing, or real-time data streams.
- **Karpenter** excels at dynamically scaling nodes, especially in cloud environments with diverse instance types or where cost optimization is critical.
- **Together**: KEDA manages your application scaling, while Karpenter ensures your cluster infrastructure scales to support it.

## Conclusion 🎯

KEDA, Karpenter, and Kubernetes' native autoscalers each address different scaling needs. KEDA excels at event-driven pod scaling, Kubernetes HPA and VPA provide standard resource-based scaling, and Karpenter optimizes node-level scaling. By leveraging these tools together, you can build a Kubernetes environment that is both highly responsive and cost-efficient, perfect for modern, dynamic workloads.

Happy clustering !
