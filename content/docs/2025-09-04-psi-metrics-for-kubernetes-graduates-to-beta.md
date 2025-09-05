---
title: PSI Metrics for Kubernetes Graduates to Beta
date: '2025-09-04T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/09/04/kubernetes-v1-34-introducing-psi-metrics-beta/
post_kind: link
draft: false
tldr: PSI Metrics for Kubernetes Graduates to Beta What is Pressure Stall Information
  (PSI)? PSI metrics in Kubernetes How to enable PSI metrics What's next? As Kubernetes
  clusters grow in size and complexity, understanding the health and performance of
  individual nodes becomes increasingly critical. We are excited to announce that
  as of Kubernetes v1.34, Pressure Stall Information (PSI) Metrics has graduated to
  Beta.
summary: 'PSI Metrics for Kubernetes Graduates to Beta What is Pressure Stall Information
  (PSI)? PSI metrics in Kubernetes How to enable PSI metrics What''s next? As Kubernetes
  clusters grow in size and complexity, understanding the health and performance of
  individual nodes becomes increasingly critical. We are excited to announce that
  as of Kubernetes v1.34, Pressure Stall Information (PSI) Metrics has graduated to
  Beta. Pressure Stall Information (PSI) is a feature of the Linux kernel (version
  4.20 and later) that provides a canonical way to quantify pressure on infrastructure
  resources, in terms of whether demand for a resource exceeds current supply. It
  moves beyond simple resource utilization metrics and instead measures the amount
  of time that tasks are stalled due to resource contention. This is a powerful way
  to identify and diagnose resource bottlenecks that can impact application performance.
  PSI exposes metrics for CPU, memory, and I/O, categorized as either some or full
  pressure: some full some full These metrics are aggregated over 10-second, 1-minute,
  and 5-minute rolling windows, providing a comprehensive view of resource pressure
  over time. With the KubeletPSI feature gate enabled, the kubelet can now collect
  PSI metrics from the Linux kernel and expose them through two channels: the Summary
  API and the /metrics/cadvisor Prometheus endpoint. This allows you to monitor and
  alert on resource pressure at the node, pod, and container level. KubeletPSI /metrics/cadvisor
  The following new metrics are available in Prometheus exposition format via /metrics/cadvisor
  : /metrics/cadvisor container_pressure_cpu_stalled_seconds_total container_pressure_cpu_stalled_seconds_total
  container_pressure_cpu_waiting_seconds_total container_pressure_cpu_waiting_seconds_total
  container_pressure_memory_stalled_seconds_total container_pressure_memory_stalled_seconds_total
  container_pressure_memory_waiting_seconds_total container_pressure_memory_waiting_seconds_total
  container_pressure_io_stalled_seconds_total container_pressure_io_stalled_seconds_total
  container_pressure_io_waiting_seconds_total container_pressure_io_waiting_seconds_total
  These metrics, along with the data from the Summary API, provide a granular view
  of resource pressure, enabling you to pinpoint the source of performance issues
  and take corrective action. For example, you can use these metrics to: Identify
  memory leaks: A steadily increasing some pressure for memory can indicate a memory
  leak in an application. some Optimize resource requests and limits: By understanding
  the resource pressure of your workloads, you can more accurately tune their resource
  requests and limits. Autoscale workloads: You can use PSI metrics to trigger autoscaling
  events, ensuring that your workloads have the resources they need to perform optimally.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/09/04/kubernetes-v1-34-introducing-psi-metrics-beta/
