---
title: 'Disaster Recovery: Achieving Instantaneous Hot-Hot with OpenShift'
date: '2025-08-20T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/disaster-recovery-with-openshift-hot-hot
post_kind: link
draft: false
tldr: Share The biggest challenge for disaster recovery in traditional environments
  is that every environment looks and feels different. If you're moving from a colo
  that someone manages to VMware, the cloud, or a different VMware data center, they
  all look and feel different.
summary: Share The biggest challenge for disaster recovery in traditional environments
  is that every environment looks and feels different. If you're moving from a colo
  that someone manages to VMware, the cloud, or a different VMware data center, they
  all look and feel different. Even if you're using the same virtualization provider,
  storage is probably handled differently. There has to be a lot of planning and strategy
  around how to copy data from one area to another since that’s not something natively
  built into your virtualization provider. You also have to figure out networking,
  DNS, routing, etc. With Red Hat OpenShift , all of these components are software-defined.
  You get software-defined DNS, networking, and storage layers all because it’s based
  on Kubernetes. Out-of-the-box OpenShift won’t “automagically” failover without additional
  levels of configuration, much like VMware or other traditional infrastructure environments.
  But the tools required are mostly there for you, either pre-packaged and open-source
  or robustly tested and a standard in the space. You can set up OpenShift in any
  environment because the least common denominator for everything, no matter where
  you are (bare metal or virtual), is the operating system This is where OpenShift
  lives. That’s why it is the perfect tool for building a truly agile infrastructure
  that can move freely between environments, providing instantaneous disaster recovery
  for businesses. There are different benefits of infrastructure agility.
---
Open the original post ↗ https://www.redhat.com/en/blog/disaster-recovery-with-openshift-hot-hot
