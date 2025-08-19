---
title: "Understanding Pod Topology Spread Constraints and Node Affinity in Kubernetes"
date: 2024-08-15T14:26:38+00:00
description: "When you're running applications in Kubernetes, it's important to think about where your Pods (the..."
tags: ["kubernetes", "devops", "cloud"]
draft: false
slug: "understanding-pod-topology-spread-constraints-and-node-affinity-in-kubernetes-49a2"
devto_id: 1960316
devto_url: "https://dev.to/hkhelil/understanding-pod-topology-spread-constraints-and-node-affinity-in-kubernetes-49a2"
---
When you're running applications in Kubernetes, it's important to think about where your Pods (the units that make up your application) are placed in your cluster. Getting this right helps keep your application available, resilient, and running smoothly. Two tools that can help you do this are **Pod Topology Spread Constraints** and **Node Affinity**. Let’s break these down with some easy-to-understand examples.

## 1. Pod Topology Spread Constraints

Think of **Pod Topology Spread Constraints** as a way to tell Kubernetes, "Hey, I want my Pods spread out evenly across different parts of my cluster." This helps prevent all your Pods from ending up in the same spot, which could be a problem if that spot has an issue.

### When Would You Use This?
Let’s say you have an app that needs to be up and running, even if one part of your cloud infrastructure goes down. You want your Pods to be spread across different availability zones (basically, different parts of the cloud) so that even if one zone has a problem, your app keeps running in the others.

### Here’s How You Do It:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app-deployment
spec:
  replicas: 6
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              app: web-app
      containers:
        - name: web-app
          image: nginx
```

**What’s Happening Here?**
- **`topologyKey`**: We’re asking Kubernetes to spread Pods across different availability zones (`topology.kubernetes.io/zone`).
- **`maxSkew`**: This makes sure that the difference in the number of Pods across zones doesn’t go above 1. So if one zone has 3 Pods, the others will have either 2 or 3.
- **`whenUnsatisfiable`**: If Kubernetes can’t satisfy this spread, it simply won’t schedule new Pods.

### Want to Dive Deeper?
Check out the [Kubernetes documentation on Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/).

## 2. Node Affinity

Now, let’s talk about **Node Affinity**. This feature lets you tell Kubernetes, "I want my Pods to run on specific nodes that meet certain criteria." It’s like saying, "Put my Pods on nodes that have the best hardware for the job."

### When Would You Use This?
Imagine you have a workload that needs super-fast storage, like SSDs. You want to make sure your Pods only run on nodes that have SSDs.

### Here’s How You Do It:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: disktype
                operator: In
                values:
                  - ssd
  containers:
    - name: my-app
      image: nginx
```

**What’s Happening Here?**
- **`nodeAffinity`**: This tells Kubernetes to schedule Pods only on nodes with SSDs (`disktype=ssd`).
- **`requiredDuringSchedulingIgnoredDuringExecution`**: It’s a strict rule—if no nodes with SSDs are available, the Pods won’t be scheduled.

### Want to Learn More?
Check out the [Kubernetes documentation on Node Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity).

## Putting It All Together

Sometimes, you’ll want to use both **Pod Topology Spread Constraints** and **Node Affinity** together. For example, you might want your Pods to run on SSD-equipped nodes and be evenly spread across multiple availability zones.

### Here’s an Example of Using Both:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: distributed-app-deployment
spec:
  replicas: 6
  selector:
    matchLabels:
      app: distributed-app
  template:
    metadata:
      labels:
        app: distributed-app
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: disktype
                    operator: In
                    values:
                      - ssd
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              app: distributed-app
      containers:
        - name: distributed-app
          image: nginx
```

**Why Use Both?**
- **Node Affinity** ensures your Pods land on nodes with the right hardware (like SSDs).
- **Pod Topology Spread Constraints** make sure those Pods are spread out across different zones, so your app stays up even if one zone goes down.

## Wrapping Up

Understanding how to use **Pod Topology Spread Constraints** and **Node Affinity** can really help you get the most out of your Kubernetes cluster. By using these tools, you can make sure your applications are not only running on the best nodes but are also distributed in a way that keeps them highly available and resilient.

For more detailed information, check out the official Kubernetes documentation:
- [Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/)
- [Node Affinity and Anti-Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity)

Happy clustering!
