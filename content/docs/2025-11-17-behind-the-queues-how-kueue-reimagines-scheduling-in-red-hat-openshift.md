---
title: 'Behind the queues: How Kueue reimagines scheduling in Red Hat OpenShift'
date: '2025-11-17T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/behind-queues-how-kueue-reimagines-scheduling-red-hat-openshift
post_kind: link
draft: false
tldr: 'Behind the queues: How Kueue reimagines scheduling in Red Hat OpenShift Topology-aware
  scheduling Kueue with dynamic resource allocation Why it matters Next steps Red
  Hat OpenShift Container Platform | Product Trial About the authors Pannaga Rao Bhoja
  Ramamanohara Sohan Kunkerkar More like this NGINX Gateway Fabric certified for Red
  Hat OpenShift DxOperator from DH2i is now certified for Red Hat OpenShift 4.19 Where
  Coders Code | Command Line Heroes What Kind of Coder Will You Become? | Command
  Line Heroes Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share In a modern cluster, the hardest problem isn’t running workloads—it''s sharing
  resources fairly. Red Hat OpenShift clusters are seeing a surge of AI-accelerated
  workloads, from GPU-intensive training jobs to large batches of inference requests.'
summary: 'Behind the queues: How Kueue reimagines scheduling in Red Hat OpenShift
  Topology-aware scheduling Kueue with dynamic resource allocation Why it matters
  Next steps Red Hat OpenShift Container Platform | Product Trial About the authors
  Pannaga Rao Bhoja Ramamanohara Sohan Kunkerkar More like this NGINX Gateway Fabric
  certified for Red Hat OpenShift DxOperator from DH2i is now certified for Red Hat
  OpenShift 4.19 Where Coders Code | Command Line Heroes What Kind of Coder Will You
  Become? | Command Line Heroes Keep exploring Browse by channel Automation Artificial
  intelligence Open hybrid cloud Security Edge computing Infrastructure Applications
  Virtualization Share In a modern cluster, the hardest problem isn’t running workloads—it''s
  sharing resources fairly. Red Hat OpenShift clusters are seeing a surge of AI-accelerated
  workloads, from GPU-intensive training jobs to large batches of inference requests.
  At the same time, other tenants still need consistent throughput for their everyday
  CI/CD pipelines and data processing tasks. The result is a constant battle for resources,
  where some jobs wait too long, others consume more than their fair share, and administrators
  are left fighting bottlenecks. This is exactly the challenge that Kueue, a Kubernetes-native
  job queueing and scheduling framework, was built to solve. It introduces structured
  queues, priorities, and quota enforcement to bring fairness and predictability back
  into scheduling. With Red Hat Build of Kueue, these upstream innovations are packaged,
  hardened, and delivered into Red Hat OpenShift as a supported, enterprise-ready
  solution to enable clusters to run efficiently while giving every workload a fair
  chance. Once workloads are queued fairly, the next challenge is where they actually
  land. For distributed jobs, placement can matter as much as allocation: pods that
  constantly exchange data perform very differently depending on whether they''re
  co-located or scattered across zones. This is where topology-aware scheduling (TAS)
  comes in. Rather than treating the cluster as a flat pool of machines, TAS considers
  the physical and logical layout of the infrastructure (racks, blocks, zones) and
  makes scheduling decisions that optimize communication and efficiency. Workloads
  that talk a lot can be placed closer together, multi-pod jobs can start in sync
  through gang scheduling, and fairness across tenants is preserved even as locality
  is optimized.'
---
Open the original post ↗ https://www.redhat.com/en/blog/behind-queues-how-kueue-reimagines-scheduling-red-hat-openshift
