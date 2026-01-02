---
title: 'Part 2: Observing and scaling MLOps infrastructure on Amazon EKS'
date: '2025-12-29T15:16:24+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/part-2-observing-and-scaling-mlops-infrastructure-on-amazon-eks/
post_kind: link
draft: false
tldr: 'Part 2: Observing and scaling MLOps infrastructure on Amazon EKS The unique
  challenges of MLOps monitoring Understanding your ML hardware landscape NVIDIA GPUs
  with CUDA Key features for ML workloads Latest advancements (NVIDIA GPUs and AWS
  Custom silicon chips) Building your monitoring strategy framework Essential metrics
  by hardware type AWS Neuron specific metrics Implementing Prometheus for metrics
  collection Understanding Prometheus Prometheus exposition formats The kube-prometheus-stack
  Implementing scaling based on custom metrics Monitoring and scaling an application
  Visualizing ML operations with Grafana Monitoring with third party solutions Evaluation
  criteria Conclusion About the authors In part 1 of this series, Introduction to
  observing machine learning workloads on Amazon EKS , we established several key
  foundational concepts. We explored the fundamental differences between monitoring
  machine learning (ML) and traditional workloads, emphasizing how ML systems require
  more specialized metrics and granular monitoring.'
summary: 'Part 2: Observing and scaling MLOps infrastructure on Amazon EKS The unique
  challenges of MLOps monitoring Understanding your ML hardware landscape NVIDIA GPUs
  with CUDA Key features for ML workloads Latest advancements (NVIDIA GPUs and AWS
  Custom silicon chips) Building your monitoring strategy framework Essential metrics
  by hardware type AWS Neuron specific metrics Implementing Prometheus for metrics
  collection Understanding Prometheus Prometheus exposition formats The kube-prometheus-stack
  Implementing scaling based on custom metrics Monitoring and scaling an application
  Visualizing ML operations with Grafana Monitoring with third party solutions Evaluation
  criteria Conclusion About the authors In part 1 of this series, Introduction to
  observing machine learning workloads on Amazon EKS , we established several key
  foundational concepts. We explored the fundamental differences between monitoring
  machine learning (ML) and traditional workloads, emphasizing how ML systems require
  more specialized metrics and granular monitoring. We detailed the essential metrics
  needed across ML infrastructure, model performance, and workload deployment on Amazon
  Elastic Kubernetes Service (Amazon EKS), including critical indicators such as model
  accuracy, inference latency, and resource usage. Furthermore, we examined how different
  roles, from data scientists to DevOps engineers, have unique monitoring requirements
  that shape the overall observability strategy. In this post, we focus on observing
  and scaling ML operations (MLOps) infrastructure on Kubernetes. MLOps platforms
  running on Amazon EKS provide powerful built-in capabilities for logging, monitoring,
  and alerting that are essential for maintaining healthy ML systems at scale. When
  deploying tools such as Airflow , JupyterHub , Ray , Kubeflow , or MLflow on Amazon
  EKS, you need a comprehensive observability strategy that uses both Amazon Web Services
  (AWS) services and cloud tooling. Amazon EKS integrates seamlessly with Amazon CloudWatch
  for logging and monitoring capabilities, but many organizations choose to implement
  other open source observability stacks into their ML workloads. The most common
  pattern involves using Prometheus for metrics collection, Grafana for visualization,
  and Kubernetes-native resources for automated scaling. You can use this setup to
  monitor everything from infrastructure metrics (CPU, memory, and GPU usage) to ML-specific
  metrics (model inference latency, training job progress, and batch processing throughput).
  ML workloads present distinct monitoring challenges when compared to traditional
  applications. ML systems involve complex pipelines with multiple stages, such as
  data preprocessing, model training, validation, and inference, each with different
  resource requirements and failure modes.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/part-2-observing-and-scaling-mlops-infrastructure-on-amazon-eks/
