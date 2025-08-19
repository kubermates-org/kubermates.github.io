---
title: "Chaos Engineering Let's Break Everything! 😈"
date: 2024-08-27T10:51:45+00:00
description: "Introduction   Hey there! 👋 If you're running your applications on Kubernetes, you might..."
tags: ["kubernetes", "cloud", "devops", "productivity"]
draft: false
slug: "chaos-engineering-lets-break-everything-io0"
devto_id: 1965771
devto_url: "https://dev.to/hkhelil/chaos-engineering-lets-break-everything-io0"
---
## Introduction

Hey there! 👋 If you're running your applications on Kubernetes, you might already know that things can go wrong in unexpected ways. That's where **chaos engineering** comes in! Chaos engineering is all about intentionally injecting failures into your system to see how it behaves under stress. The idea is to discover weaknesses and fix them before they can cause real problems.

Today, we're diving into **Chaos Mesh**, an awesome tool that makes chaos engineering in Kubernetes super easy and fun (well, as fun as breaking things can be!). We'll go step-by-step through setting up Chaos Mesh and show you how to run some cool chaos experiments to test your app's resilience.

## Setting Up Chaos Mesh

First things first, let’s get Chaos Mesh installed on your Kubernetes cluster. Don’t worry, it’s straightforward!

### 1. Installing Chaos Mesh with Helm

🚀 **Step 1: Add the Chaos Mesh Helm repository:**

```bash
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm repo update
```

🚀 **Step 2: Install Chaos Mesh:**

```bash
kubectl create ns chaos-testing
helm install chaos-mesh chaos-mesh/chaos-mesh -n chaos-testing
```

🚀 **Step 3: Verify the installation:**

```bash
kubectl get pods -n chaos-testing
```

You should see a bunch of pods up and running, like `chaos-controller-manager`, `chaos-daemon`, and `chaos-dashboard`. 🎉

### 2. Accessing the Chaos Mesh Dashboard

Chaos Mesh comes with a handy web dashboard where you can create and manage your chaos experiments.

🌐 **Step 4: Port-forward the dashboard service:**

```bash
kubectl port-forward -n chaos-testing svc/chaos-dashboard 2333:2333
```

🌐 **Step 5: Access the dashboard** by heading to `http://localhost:2333` in your browser. You’ll now be able to start breaking things… I mean, testing things! 😅

## Creating Chaos Experiments

Now that Chaos Mesh is up and running, let’s start experimenting! Below are some chaos scenarios you can try out, along with the main options you can configure in each experiment.

### 1. Simulating Network Latency

🚦 **What’s the deal?**  
Network latency can happen for all sorts of reasons, and it can really mess with your app’s performance. Let’s see how your app handles it.

**Example:**

```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-delay
  namespace: chaos-testing
spec:
  action: delay
  mode: one
  selector:
    namespaces:
      - default
    labelSelectors:
      "app": "my-app"
  delay:
    latency: "200ms"
  duration: "1m"
  scheduler:
    cron: "@every 3m"
```

**Main Options:**

- **`action`**: Type of network fault. Options include `delay`, `loss`, `duplicate`, `corrupt`, `partition`.
- **`mode`**: Specifies how the chaos is applied. Options include `one`, `all`, `fixed`, `fixed-percent`, `random-max-percent`.
- **`selector`**: Used to select target pods based on namespace, labels, or fields.
- **`delay.latency`**: Time to delay network packets.
- **`duration`**: How long the experiment should last.
- **`scheduler`**: Defines when the experiment should run (using cron syntax).

📚 [Learn more about NetworkChaos in the Chaos Mesh docs](https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/)

### 2. Killing a Pod (Pod Chaos)

💥 **What’s the deal?**  
Sometimes, pods just die. It could be due to resource exhaustion, bugs, or something else. Let’s simulate a pod crash and see what happens!

**Example:**

```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: pod-failure
  namespace: chaos-testing
spec:
  action: pod-kill
  mode: one
  selector:
    namespaces:
      - default
    labelSelectors:
      "app": "my-app"
  duration: "10s"
  scheduler:
    cron: "@every 1m"
```

**Main Options:**

- **`action`**: Type of pod fault. Common options are `pod-kill`, `container-kill`, `pod-failure`.
- **`mode`**: Specifies how the chaos is applied. Options include `one`, `all`, `fixed`, `fixed-percent`, `random-max-percent`.
- **`selector`**: Used to select target pods based on namespace, labels, or fields.
- **`duration`**: How long the experiment should last.
- **`scheduler`**: Defines when the experiment should run (using cron syntax).

📚 [Learn more about PodChaos in the Chaos Mesh docs](https://chaos-mesh.org/docs/simulate-pod-chaos-on-kubernetes/)

### 3. CPU Stress Test

🔥 **What’s the deal?**  
High CPU usage can slow things down or even cause crashes. Let’s crank up the CPU usage and see how your app handles the heat.

**Example:**

```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: StressChaos
metadata:
  name: cpu-stress
  namespace: chaos-testing
spec:
  mode: one
  selector:
    namespaces:
      - default
    labelSelectors:
      "app": "my-app"
  stressors:
    cpu:
      workers: 4
  duration: "30s"
  scheduler:
    cron: "@every 5m"
```

**Main Options:**

- **`stressors.cpu.workers`**: Number of CPU workers to stress the target pods.
- **`mode`**: Specifies how the chaos is applied. Options include `one`, `all`, `fixed`, `fixed-percent`, `random-max-percent`.
- **`selector`**: Used to select target pods based on namespace, labels, or fields.
- **`duration`**: How long the experiment should last.
- **`scheduler`**: Defines when the experiment should run (using cron syntax).

📚 [Learn more about StressChaos in the Chaos Mesh docs](https://chaos-mesh.org/docs/simulate-heavy-stress-on-kubernetes/)

### 4. Simulating Disk Pressure

💾 **What’s the deal?**  
Running out of disk space or dealing with slow disk I/O can cause major issues. Let’s simulate disk pressure and observe the impact.

**Example:**

```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: StressChaos
metadata:
  name: disk-stress
  namespace: chaos-testing
spec:
  mode: one
  selector:
    namespaces:
      - default
    labelSelectors:
      "app": "my-app"
  stressors:
    io:
      workers: 2
  duration: "40s"
  scheduler:
    cron: "@every 7m"
```

**Main Options:**

- **`stressors.io.workers`**: Number of I/O workers to stress the target pods.
- **`mode`**: Specifies how the chaos is applied. Options include `one`, `all`, `fixed`, `fixed-percent`, `random-max-percent`.
- **`selector`**: Used to select target pods based on namespace, labels, or fields.
- **`duration`**: How long the experiment should last.
- **`scheduler`**: Defines when the experiment should run (using cron syntax).

📚 [Learn more about StressChaos in the Chaos Mesh docs](https://chaos-mesh.org/docs/simulate-heavy-stress-on-kubernetes/)

### 5. Network Partition

🌐 **What’s the deal?**  
Network partitions, where parts of your system can’t talk to each other, can cause all kinds of chaos. Let’s split your network and see what breaks!

**Example:**

```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-partition
  namespace: chaos-testing
spec:
  action: partition
  mode: all
  selector:
    namespaces:
      - default
    labelSelectors:
      "app": "frontend"
  direction: both
  target:
    selector:
      namespaces:
        - default
      labelSelectors:
        "app": "backend"
  duration: "60s"
  scheduler:
    cron: "@every 10m"
```

**Main Options:**

- **`action`**: Type of network fault. Here it’s `partition`, which simulates a network partition.
- **`mode`**: Specifies how the chaos is applied. Options include `one`, `all`, `fixed`, `fixed-percent`, `random-max-percent`.
- **`selector`**: Used to select target pods based on namespace, labels, or fields.
- **`direction`**: Defines the direction of the partition (`from`, `to`, `both`).
- **`target.selector`**: Specifies the target pods that will be isolated from the selected pods.
- **`duration`**: How long the experiment should last.
- **`scheduler`**: Defines when the experiment should run (

using cron syntax).

📚 [Learn more about NetworkChaos in the Chaos Mesh docs](https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/)

## Monitoring the Impact of Chaos

While your chaos experiments are running, it’s super important to keep an eye on your app’s performance. Here’s how to do it:

- **Use Monitoring Tools:** Make sure you’ve got tools like Prometheus and Grafana set up to track things like response times, error rates, and resource usage. 📊
- **Check Your Logs:** Keep an eye on your logs to spot any errors or warnings that pop up during the chaos experiments. 🕵️
- **Analyze Metrics:** Look at the data you’re collecting to understand how your app is handling the chaos. Are there timeouts? Increased latency? Use this info to improve your system’s resilience. 🔍

## Best Practices for Chaos Engineering with Chaos Mesh

🌟 **Start Small:** Don’t go all-in right away. Start with simple experiments and work your way up to more complex scenarios.

🌟 **Test in Staging:** Before you unleash chaos in production, run your experiments in a staging environment to avoid any nasty surprises.

🌟 **Automate Tests:** Integrate chaos experiments into your CI/CD pipeline. This way, you’ll automatically test your app’s resilience with every new deployment.

🌟 **Monitor Everything:** Make sure you have comprehensive monitoring in place so you can quickly spot and respond to any issues caused by the chaos experiments.

🌟 **Iterate and Improve:** Use what you learn from the experiments to make your app stronger. Keep refining your chaos tests as your system evolves.

## Conclusion

And there you have it! 🎉 Chaos Mesh is an incredible tool that makes chaos engineering in Kubernetes not only possible but also enjoyable. By running these experiments, you’ll uncover weaknesses in your system that you might never have found otherwise.

Remember, the goal of chaos engineering isn’t to break things just for fun (though it can be fun 😜), but to learn how to build more resilient and reliable systems. So start small, experiment often, and keep improving your app’s resilience. Happy chaos engineering! 🚀

For more detailed documentation on each type of chaos experiment and more advanced configurations, you can check out the official [Chaos Mesh Documentation](https://chaos-mesh.org/docs/).
