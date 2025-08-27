---
title: 🚀 Announcing the Kubeflow Spark Operator Benchmarking Results
date: '2025-03-15T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/operators/benchmarking/performance/2025/03/15/kubeflow-spark-operator-benchmarks.html
post_kind: link
draft: false
tldr: Mar 15, 2025 • Vara Bonthu , Manabu McCloskey , Ratnopam Chakrabarti , Alan
  Halcyon • 5 min read operators benchmarking performance Kubernetes has become the
  go-to platform for running large-scale Apache Spark workloads. But as workloads
  scale, how do you ensure your Spark jobs run efficiently without hitting bottlenecks?
  Managing thousands of concurrent Spark jobs can introduce severe performance challenges
  —from CPU saturation in the Spark Operator to Kubernetes API slowdowns and job scheduling
  inefficiencies.
summary: 'Mar 15, 2025 • Vara Bonthu , Manabu McCloskey , Ratnopam Chakrabarti , Alan
  Halcyon • 5 min read operators benchmarking performance Kubernetes has become the
  go-to platform for running large-scale Apache Spark workloads. But as workloads
  scale, how do you ensure your Spark jobs run efficiently without hitting bottlenecks?
  Managing thousands of concurrent Spark jobs can introduce severe performance challenges
  —from CPU saturation in the Spark Operator to Kubernetes API slowdowns and job scheduling
  inefficiencies. To address these challenges, we are excited to introduce the Kubeflow
  Spark Operator Benchmarking Results and Toolkit —a comprehensive framework to analyze
  performance, pinpoint bottlenecks, and optimize your Spark on Kubernetes deployments.
  This benchmarking effort provides three key outcomes to help you take full control
  of your Spark on Kubernetes deployment: ✅ Benchmarking Results – A detailed evaluation
  of performance insights and tuning recommendations for large-scale Spark workloads.
  🛠 Benchmarking Test Toolkit – A fully reproducible test suite to help users evaluate
  their own Spark Operator performance and validate improvements. 📊 Open-Sourced Grafana
  Dashboard – A battle-tested visualization tool designed specifically to track large-scale
  Spark Operator deployments, providing real-time monitoring of job processing efficiency,
  API latencies, and system health. Running thousands of Spark jobs on Kubernetes
  at scale uncovers several performance roadblocks that can cripple efficiency if
  left unresolved: 💡 So, how do you fix these issues and optimize your Spark Operator
  deployment? That’s where our benchmarking results and toolkit come in. Based on
  our benchmarking findings, we provide clear, actionable recommendations for improving
  Spark Operator performance at scale. If you’re running thousands of concurrent Spark
  jobs , here’s what you need to do: 💡 Why? A single Spark Operator instance struggles
  to keep up with high job submission rates. ✅ Solution : When a single Spark Operator
  instance struggles with high job submission rates, leading to CPU saturation and
  slower job launches, deploying multiple instances can help. Distribute the workload
  by assigning different namespaces to each instance. For example, one instance can
  manage ` 20 namespaces while another handles a separate set of 20 namespaces.'
---
Open the original post ↗ https://blog.kubeflow.org/operators/benchmarking/performance/2025/03/15/kubeflow-spark-operator-benchmarks.html
