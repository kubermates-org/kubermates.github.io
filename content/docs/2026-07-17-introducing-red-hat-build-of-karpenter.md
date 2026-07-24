---
title: Introducing Red Hat build of Karpenter
date: '2026-07-17T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/introducing-red-hat-build-karpenter
post_kind: link
draft: false
tldr: 'Introducing Red Hat build of Karpenter What is Karpenter? What is the Red Hat
  build of Karpenter? Controllers hosted in the control plane Enable on existing clusters
  Independent upgrades Coexistence with Cluster Autoscaler Capacity Reservations and
  Capacity Blocks for ML Kubelet configuration and node tuning Security compliance
  Cost savings Best Practices for smarter autoscaling Conclusion Red Hat OpenShift
  Container Platform | Product Trial About the authors Subin Modeel Bala Chandrasekaran
  More like this Debunking IT automation myths: A strategic blueprint for healthcare
  payers The evolution of infrastructure automation in the age of AI: 4 key takeaways
  from Red Hat Summit 2026 Untangling Networks | Compiler Operating System Management
  | Compiler Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Achieving infrastructure efficiency and controlling compute costs is a continuous
  effort. While traditional machine pools are effective for steady workloads, scaling
  diverse applications often requires balancing cloud utilization with the effort
  spent manually right-sizing instances, all while providing continuous node availability
  when compute demands spike.'
summary: 'Introducing Red Hat build of Karpenter What is Karpenter? What is the Red
  Hat build of Karpenter? Controllers hosted in the control plane Enable on existing
  clusters Independent upgrades Coexistence with Cluster Autoscaler Capacity Reservations
  and Capacity Blocks for ML Kubelet configuration and node tuning Security compliance
  Cost savings Best Practices for smarter autoscaling Conclusion Red Hat OpenShift
  Container Platform | Product Trial About the authors Subin Modeel Bala Chandrasekaran
  More like this Debunking IT automation myths: A strategic blueprint for healthcare
  payers The evolution of infrastructure automation in the age of AI: 4 key takeaways
  from Red Hat Summit 2026 Untangling Networks | Compiler Operating System Management
  | Compiler Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share Achieving infrastructure efficiency and controlling compute costs is a continuous
  effort. While traditional machine pools are effective for steady workloads, scaling
  diverse applications often requires balancing cloud utilization with the effort
  spent manually right-sizing instances, all while providing continuous node availability
  when compute demands spike. To help achieve this balance, we are introducing the
  Red Hat build of Karpenter, based on the upstream Karpenter project. With the release
  of Red Hat OpenShift 4.22 , Red Hat build of Karpenter can be enabled on Red Hat
  OpenShift Service on AWS with hosted control planes. Karpenter is a high-performance,
  Kubernetes-native node autoscaler. Instead of scaling fixed pools of identical machines,
  it looks at the collective resource requirements of your pending pods and provisions
  the right compute resources just-in-time, then continuously consolidates the cluster
  to reduce your infrastructure costs. The result is compute that is right-sized automatically,
  around the clock, with no manual intervention. Red Hat build of Karpenter brings
  workload-aware, just-in-time node provisioning to Red Hat OpenShift Service on AWS
  with hosted control planes. Instead of managing static machine pools with pre-defined
  instance types, Karpenter evaluates the exact CPU, memory, and scheduling constraints
  of pending pods and provisions the optimal EC2 instance automatically, and then
  consolidates underutilized nodes when they are no longer needed. The Karpenter controllers
  run as part of the hosted control plane, not on your worker nodes. There are no
  extra pods to manage, no added compute overhead, and no resource contention between
  Karpenter and your applications. Karpenter can be turned on for existing clusters
  once they are upgraded to OpenShift 4.22.'
---
Open the original post ↗ https://www.redhat.com/en/blog/introducing-red-hat-build-karpenter
