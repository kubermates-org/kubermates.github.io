---
title: 'Kubernetes v1.35: Introducing Workload Aware Scheduling'
date: '2025-12-29T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/29/kubernetes-v1-35-introducing-workload-aware-scheduling/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Introducing Workload Aware Scheduling Workload aware scheduling
  Workload API How gang scheduling works Opportunistic batching Restrictions The north
  star vision Getting started Learn more Scheduling large workloads is a much more
  complex and fragile operation than scheduling a single Pod, as it often requires
  considering all Pods together instead of scheduling each one independently. For
  example, when scheduling a machine learning batch job, you often need to place each
  worker strategically, such as on the same rack, to make the entire process as efficient
  as possible.'
summary: 'Kubernetes v1.35: Introducing Workload Aware Scheduling Workload aware scheduling
  Workload API How gang scheduling works Opportunistic batching Restrictions The north
  star vision Getting started Learn more Scheduling large workloads is a much more
  complex and fragile operation than scheduling a single Pod, as it often requires
  considering all Pods together instead of scheduling each one independently. For
  example, when scheduling a machine learning batch job, you often need to place each
  worker strategically, such as on the same rack, to make the entire process as efficient
  as possible. At the same time, the Pods that are part of such a workload are very
  often identical from the scheduling perspective, which fundamentally changes how
  this process should look. There are many custom schedulers adapted to perform workload
  scheduling efficiently, but considering how common and important workload scheduling
  is to Kubernetes users, especially in the AI era with the growing number of use
  cases, it is high time to make workloads a first-class citizen for kube-scheduler
  and support them natively. kube-scheduler The recent 1.35 release of Kubernetes
  delivered the first tranche of workload aware scheduling improvements. These are
  part of a wider effort that is aiming to improve scheduling and management of workloads.
  The effort will span over many SIGs and releases, and is supposed to gradually expand
  capabilities of the system toward reaching the north star goal, which is seamless
  workload scheduling and management in Kubernetes including, but not limited to,
  preemption and autoscaling. Kubernetes v1.35 introduces the Workload API that you
  can use to describe the desired shape as well as scheduling-oriented requirements
  of the workload. It comes with an initial implementation of gang scheduling that
  instructs the kube-scheduler to schedule gang Pods in the all-or-nothing fashion.
  Finally, we improved scheduling of identical Pods (that typically make a gang) to
  speed up the process thanks to the opportunistic batching feature. kube-scheduler
  The new Workload API resource is part of the scheduling. k8s.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/29/kubernetes-v1-35-introducing-workload-aware-scheduling/
