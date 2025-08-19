---
title: "Essential Tips for Setting Resource Limits in Kubernetes 📈"
date: 2024-08-19T07:31:56+00:00
description: "Introduction   Kubernetes is like the ultimate conductor 🎶 in an orchestra, ensuring that..."
tags: ["kubernetes", "cloud", "devops", "finops"]
draft: false
slug: "essential-tips-for-setting-resource-limits-in-kubernetes-3b54"
devto_id: 1960723
devto_url: "https://dev.to/hkhelil/essential-tips-for-setting-resource-limits-in-kubernetes-3b54"
---
## Introduction

Kubernetes is like the ultimate conductor 🎶 in an orchestra, ensuring that all your applications (the musicians) play in harmony without hogging too many resources (the instruments). But if you don't set the right limits, things can get out of tune quickly! 🎻 Setting the right resource limitations in Kubernetes helps keep everything running smoothly, preventing any one application from using too much CPU or memory and leaving the rest high and dry.

In this article, we'll explore how to set up these resource limitations in Kubernetes in a way that’s both practical and easy to understand. I'll also throw in some examples to help you get started.

## What Are Resource Requests and Limits? 🤔

Before we dive in, let’s break down what we’re talking about:

1. **Resource Requests**: Think of this as your app saying, "I need at least this much CPU and memory to work properly." Kubernetes uses these requests to decide where to run your app.

2. **Resource Limits**: This is more like, "Okay, but this is the maximum you can use!" If your app tries to use more than this, Kubernetes will step in and put a stop to it, either by slowing things down (throttling) or restarting the app.

## Why Setting Resource Limits Matters 🎯

Setting resource limits isn’t just about keeping things neat and tidy—it’s about making sure everything runs smoothly without any nasty surprises. Here’s why it’s important:

- **Balanced Resource Use**: By setting limits, you make sure your apps share the available resources fairly, preventing one app from hogging everything.
  
- **Preventing Issues**: Without limits, one misbehaving app could bring down others by using up all the CPU or memory.

- **Cost Control**: In cloud environments, more resources often mean more money. 💰 Proper limits help avoid overspending.

## How the Kubernetes Scheduler Works 🧠

Before diving into how to set these limits, it's helpful to understand how the Kubernetes scheduler plays a role when setting resource requests and limits. The scheduler is the brain that decides which node in your cluster will run each pod. Here’s how it works:

1. **Scheduling Based on Resource Requests**: 
    When you deploy a pod, the scheduler looks at the resource requests (the minimum CPU and memory your app needs) and finds a node with enough available resources to meet those requests. If a node can’t meet the requests for a pod, the scheduler won’t place the pod there.

2. **Node Selection**:
    The scheduler considers various factors to choose the best node, such as:
    - **Available Resources**: Does the node have enough free CPU and memory to handle the pod’s requests?
    - **Taints and Tolerations**: Are there any special rules (taints) on the nodes that the pod can tolerate?
    - **Node Affinity/Anti-Affinity**: Are there preferences set for the pod to run on certain nodes or avoid others?

3. **Pod Placement**:
    Once a suitable node is found, the pod is placed there. This means that if your pod requests 500m of CPU and 1Gi of memory, the scheduler will ensure it’s placed on a node that can offer at least that much.

4. **Handling Resource Limits**:
    After a pod is running, the Kubernetes system ensures it doesn’t exceed its resource limits. If a pod tries to use more CPU than its limit, it might get throttled, meaning it’s slowed down to prevent overuse. If it tries to use more memory than allowed, the pod could be terminated and restarted.

**Example**:

Imagine you have a cluster with three nodes:

- **Node A**: 4 CPUs, 8Gi memory
- **Node B**: 2 CPUs, 4Gi memory
- **Node C**: 8 CPUs, 16Gi memory

You deploy a pod with the following configuration:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app-pod
spec:
  containers:
  - name: my-app-container
    image: my-app-image
    resources:
      requests:
        memory: "1Gi"
        cpu: "500m"
      limits:
        memory: "2Gi"
        cpu: "1"
```

Here’s what happens:

- **Resource Request Check**: The scheduler sees that your pod requests 500m (0.5 CPU) and 1Gi of memory.
- **Node Evaluation**:
  - Node A: Plenty of resources available (4 CPUs, 8Gi memory)—this node is a good candidate.
  - Node B: Also available, but with fewer resources (2 CPUs, 4Gi memory)—still a good candidate but less preferred if other nodes have more resources.
  - Node C: More than enough resources (8 CPUs, 16Gi memory)—ideal for heavier workloads but might be overkill for this pod.
- **Node Selection**: The scheduler might choose Node A because it has enough resources and leaves Node C’s larger capacity for more demanding pods.
- **Pod Placement**: Your pod is placed on Node A. If it tries to use more than 1 CPU or 2Gi of memory, Kubernetes will enforce the limits you set.

## How to Stress Test Your Pod for Better Resource Adjustment 🧪

Stress testing your pod is a great way to understand its behavior under different loads and make informed decisions about resource requests and limits. Here’s how you can do it:

1. **Use Stress Tools Inside the Pod**

   You can use tools like `stress` or `stress-ng` within your container to generate load on the CPU and memory. These tools can simulate high usage, helping you see how your pod performs under pressure.

   **Example**:

   First, ensure you have `stress` installed in your container. You can do this by using a base image like `alpine` and installing `stress`:

   ```Dockerfile
   FROM alpine:latest
   RUN apk add --no-cache stress
   ```

   Then, run a pod with this image and execute the stress test:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: stress-test-pod
   spec:
     containers:
     - name: stress-container
       image: your-custom-image
       command: ["stress"]
       args: ["--cpu", "2", "--vm", "1", "--vm-bytes", "512M", "--timeout", "60s"]
       resources:
         requests:
           memory: "256Mi"
           cpu: "500m"
         limits:
           memory: "1Gi"
           cpu: "1"
   ```

   In this example:
   - `--cpu 2` generates CPU load on 2 cores.
   - `--vm 1` and `--vm-bytes 512M` allocate 512MB of memory.
   - `--timeout 60s` runs the stress test for 60 seconds.

2. **Monitor Resource Usage**

   While running the stress test, monitor the resource usage to see how close the pod gets to its limits. Tools like `kubectl top` or integrating with Prometheus/Grafana can help you visualize CPU and memory usage in real time.

   **Example**:

   ```bash
   kubectl top pod stress-test-pod
   ```

   This command will show you the CPU and memory usage of the pod. Compare these numbers with the requests and limits you set to see if adjustments are needed.

3. **Adjust Resources Based on Results**

   After the stress test, you might notice that your pod either consistently hits its limits or never uses close to what you’ve allocated. Use this information to adjust the requests and limits for better efficiency.

   **Example**:

   If you find that your pod only uses 250m CPU and 500Mi memory during peak load, you might adjust the resource settings:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: my-app-pod
   spec:
     containers:
     - name: my-app-container
       image: my-app-image
       resources:
         requests:
           memory: "500Mi"
           cpu: "250m"
         limits:
           memory: "1Gi"
           cpu: "500m"
   ```

   This adjustment helps ensure your pod is neither over-provisioned nor under-provisioned.

## Best Practices for Setting Resource Limits (with Examples) ✅

1. **Understand What Your App Needs**

   Before setting limits, it’s crucial to know how much CPU and memory your app actually needs. You can do this by:

   - **Running Tests**: Simulate real-world usage and see how much CPU and memory your app uses.
   - **Monitoring Tools**: Tools like Prometheus and Grafana can help track usage over time.

   **Example**: 

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: my-app-pod
   spec:
     containers:
     - name: my-app-container
       image: my-app-image
       resources:
         requests:
           memory: "128Mi"
           cpu: "250m"
         limits:
           memory: "256Mi"
           cpu: "500m"
   ```

   Here, we’re saying: "Hey Kubernetes, my app needs at least 128Mi of memory and 250m of CPU to run. But if it starts getting greedy, cap it at 256Mi of memory and 500m of CPU."

2. **Start with Some Buffer**

   When you're setting these limits, start conservatively. Give your app slightly more than it typically needs to ensure it doesn't run into trouble when things get busy.

3. **Use Autoscaling to Your Advantage 📈**

   Kubernetes can automatically adjust the number of running instances of your app based on demand. This is called Horizontal Pod Autoscaler (HPA). There’s also Vertical Pod Autoscaler (VPA), which adjusts the resource requests and limits as your app’s needs change.

   **Example of HPA**:

   ```yaml
   apiVersion: autoscaling/v2
   kind: HorizontalPodAutoscaler
   metadata:
     name: my-app-hpa
   spec:
     scaleTargetRef:
       apiVersion: apps/v1
       kind: Deployment
       name: my-app-deployment
     minReplicas: 1
     maxReplicas: 5
     metrics:
     - type: Resource
       resource:
         name: cpu
         target:
           type: Utilization
           averageUtilization: 70
   ```

   This example says, "Kubernetes, keep at least one instance of my app running, but feel free to add up to five if things get busy. Oh, and try to keep CPU usage around 70%."

4. **Aim for Guaranteed Quality of Service 🎯**

   Kubernetes has different levels of service depending on how you set your resource requests and limits. For critical apps, you want the "Guaranteed" level, which means setting the request and limit to the same value.

   **Example**:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: guaranteed-pod
   spec:
     containers:
     - name: guaranteed-container
       image: nginx
       resources:
         requests:
           memory: "500Mi"
           cpu: "1"
         limits:
           memory: "500Mi"
           cpu: "1"
   ```

   This setup makes sure your app always gets what it needs, no matter what.

5. **Keep an Eye on Things and Adjust 🔍**

   Things change! Your app might need more or less over time. Regularly check in and adjust your settings. Tools like Prometheus and Grafana can make this easier by showing you how your resources are being used.

6. **Don’t Overcommit Resources ⚠️**

   Kubernetes lets you overcommit resources like CPU, meaning you can promise more CPU than you actually have. But be careful! If things get busy, your app might get throttled, which could slow it down.

## Common Mistakes to Avoid ❌

1. **Setting Limits Too High**: Overestimating can lead to wasted resources and higher costs.

2. **Skipping Limits**: If you don’t set limits, one greedy app could use up everything, causing issues for others.

3. **Forgetting to Monitor**: Your app’s needs might change over time, so keep an eye on things and adjust as needed.

4. **Misconfiguring Autoscalers**: Make sure your autoscalers are set up right so they don’t go overboard and overwhelm your cluster.

## Conclusion 🎉

Setting resource limits in Kubernetes might seem a bit tricky at first, but with a little understanding and some careful planning, you can keep your apps running smoothly without any surprises. By following these tips and using the examples as a guide, you'll be well on your way to managing resources like a pro, keeping your apps happy, and your costs under control.

Remember, Kubernetes is a powerful tool, but like any tool, it works best when used wisely. So take the time to set things up right, and your apps—and your wallet—will thank you!

Happy clustering !
