---
title: Benchmarking KubeVirt performance with virtbench
date: '2026-06-08T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/08/benchmarking-kubevirt-performance-with-virtbench/
post_kind: link
draft: false
tldr: Benchmarking considerations for VM-based workloads How virtbench measures VM
  readiness Benchmark scenarios included in virtbench Visualizing performance bottlenecks
  Comparing different benchmarking approaches Running your first virtbench test Contributing
  and future roadmap Posted on June 8, 2026 by Bob Glithero, Senior Technical Product
  Marketing Manager, Portworx by Everpure CNCF projects highlighted in this post Organizations
  migrating VM estates from traditional hypervisors to KubeVirt often discover that
  many Kubernetes observability tools were originally designed around container workloads
  rather than VM-centric operational metrics. While KubeVirt schedules VMs as pods,
  the performance variables are fundamentally different—Kubernetes scheduler latency,
  CSI provisioner throughput, and SDN overlay overhead all interact in ways that standard
  kubectl metrics and pod-level monitoring do not surface.
summary: 'Benchmarking considerations for VM-based workloads How virtbench measures
  VM readiness Benchmark scenarios included in virtbench Visualizing performance bottlenecks
  Comparing different benchmarking approaches Running your first virtbench test Contributing
  and future roadmap Posted on June 8, 2026 by Bob Glithero, Senior Technical Product
  Marketing Manager, Portworx by Everpure CNCF projects highlighted in this post Organizations
  migrating VM estates from traditional hypervisors to KubeVirt often discover that
  many Kubernetes observability tools were originally designed around container workloads
  rather than VM-centric operational metrics. While KubeVirt schedules VMs as pods,
  the performance variables are fundamentally different—Kubernetes scheduler latency,
  CSI provisioner throughput, and SDN overlay overhead all interact in ways that standard
  kubectl metrics and pod-level monitoring do not surface. kubectl Platform engineering
  teams need quantifiable, reproducible answers to questions that container benchmarks
  ignore: Time-to-Ready: Wall-clock time from API call to confirmed guest OS network
  accessibility—not pod/Running. pod/Running Burst Capacity: Control plane and storage
  subsystem behavior under concurrent VM creation requests (boot storm). Live Migration
  Stun Time: Precise network-level interruption window during VMI live migration over
  the overlay network. To help measure these operational characteristics, we developed
  the KubeVirt Performance Benchmarking Toolkit (virtbench) , an open-source CLI framework
  for executing reproducible stress tests across KubeVirt-enabled clusters, including
  KubeVirt on OpenShift and other environments using CSI-compatible storage Standard
  Kubernetes observability tools can return a healthy status even when VM-class workloads
  are degraded. Three architectural mismatches explain why: Pod readiness ≠ VM readiness.
  The Kubernetes Ready condition is satisfied when the container process starts—often
  in milliseconds. A KubeVirt VMI is not operationally ready until the guest kernel
  boots, user-space services initialize, and the guest agent reports a heartbeat.
  Benchmarks that stop the clock at pod/Running misrepresent actual time-to-ready
  by minutes in typical deployments. virtbench uses an in-cluster ssh-test-pod to
  continuously probe the VMI’s guest network stack; the measurement only completes
  on confirmed SSH reachability. CSI provisioner load under multi-disk VMs.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/08/benchmarking-kubevirt-performance-with-virtbench/
