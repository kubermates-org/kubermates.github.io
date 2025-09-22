---
title: Top Kubernetes (K8s) Troubleshooting Techniques – Part 2
date: '2025-09-19T16:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/09/19/top-kubernetes-k8s-troubleshooting-techniques-part-2/
post_kind: link
draft: false
tldr: 'Kubernetes Troubleshooting Storage: Resolving PVC Pending Errors 7. Using Event
  and Audit Logs: Deep System Analysis 8.'
summary: 'Kubernetes Troubleshooting Storage: Resolving PVC Pending Errors 7. Using
  Event and Audit Logs: Deep System Analysis 8. Using Kubernetes Dashboard and Visual
  Tools 9. Implementing Health Checks and Probes 10. Advanced Debugging Techniques
  Practical Example: Network Issue Investigation Conclusion Posted on September 19,
  2025 by Keval Bhogayata, Principal Engineer at Middleware In Part 1 of our series,
  we explored essential Kubernetes troubleshooting techniques that help DevOps engineers
  diagnose and resolve common cluster and application issues effectively. However,
  Kubernetes environments are complex, and there’s always more to uncover. In this
  Part 2, we’ll dive deeper into additional troubleshooting strategies, covering advanced
  techniques and real-world scenarios that can save you time and prevent downtime.
  Whether you’re dealing with persistent pod failures, network issues, or cluster
  misconfigurations, these tips will equip you with the knowledge to tackle Kubernetes
  challenges with confidence. The PersistentVolumeClaim (PVC) Pending status is a
  common storage issue in Kubernetes, preventing applications from accessing persistent
  data. This typically results from misconfigured storage classes, missing volume
  provisioners, or insufficient available storage in the cluster. Start by listing
  all Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) across all namespaces.
  This command provides an overview of their status, access modes, capacity, and whether
  they are bound: kubectl get pv,pvc --all-namespaces kubectl get pv,pvc --all-namespaces
  To further investigate an unbound PVC stuck in the Pending state, use the following
  command: kubectl describe pvc kubectl describe pvc Check the Events section at the
  bottom of the output.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/09/19/top-kubernetes-k8s-troubleshooting-techniques-part-2/
