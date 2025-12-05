---
title: Reducing Harbor Deployment Complexity on Kubernetes
date: '2025-11-25T10:01:39+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/11/25/reducing-harbor-deployment-complexity-on-kubernetes/
post_kind: link
draft: false
tldr: 'Deploying Harbor on Kubernetes using Helm Prerequisites Step 1: Download Harbor
  Deployment Manifests Step 2: Configure values. yaml Step 3: Deploy Harbor Step 4:
  Verify Harbor Installation Leveraging VKS Standard Packages for Harbor setup Prerequisites:
  Step 1: Associate a VKS Standard Package Repository Step 2: Deploy Prerequisites
  (For Production-Ready Harbor) Step 3: Deploy Harbor Step 4: Verify Harbor Installation
  Deploying Harbor as a Supervisor Service in VCF 9 Prerequisites Step 1: Download
  and Update the Harbor Supervisor Service YAML Step 2: Deploy the Harbor Supervisor
  Service Step 3: Monitor the Harbor Supervisor Service Deployment Conclusion Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles Harbor: Your Enterprise-Ready
  Container Registry for a Modern Private Cloud VCF Breakroom Chats Episode 75 - Breaking
  the GitOps Barrier: Continuous Delivery for Modern Apps with VCF 9 What’s Next for
  Cloud Native: Highlights from KubeCon North America 2025 Harbor is an indispensable
  open-source container image registry, offering robust features like policy-driven
  security, role-based access control (RBAC), vulnerability scanning, image signing,
  image replication and distribution.'
summary: 'Deploying Harbor on Kubernetes using Helm Prerequisites Step 1: Download
  Harbor Deployment Manifests Step 2: Configure values. yaml Step 3: Deploy Harbor
  Step 4: Verify Harbor Installation Leveraging VKS Standard Packages for Harbor setup
  Prerequisites: Step 1: Associate a VKS Standard Package Repository Step 2: Deploy
  Prerequisites (For Production-Ready Harbor) Step 3: Deploy Harbor Step 4: Verify
  Harbor Installation Deploying Harbor as a Supervisor Service in VCF 9 Prerequisites
  Step 1: Download and Update the Harbor Supervisor Service YAML Step 2: Deploy the
  Harbor Supervisor Service Step 3: Monitor the Harbor Supervisor Service Deployment
  Conclusion Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Harbor: Your Enterprise-Ready Container Registry for a Modern Private Cloud VCF
  Breakroom Chats Episode 75 - Breaking the GitOps Barrier: Continuous Delivery for
  Modern Apps with VCF 9 What’s Next for Cloud Native: Highlights from KubeCon North
  America 2025 Harbor is an indispensable open-source container image registry, offering
  robust features like policy-driven security, role-based access control (RBAC), vulnerability
  scanning, image signing, image replication and distribution. Deploying Harbor is
  a common and critical step for organizations looking to streamline their containerization
  workflows. As we discussed in our previous blog post , Harbor offers significant
  value through its comprehensive features and can be deployed on a virtual machine
  (VM). This blog post will pick up where we left off, guiding you through the process
  of deploying Harbor on an upstream conformant Kubernetes platform using VMware vSphere
  Kubernetes Service (VKS) as an example first via Helm, then via VKS standard packages,
  and finally showcasing the simplified deployment as a supervisor service in VMware
  Cloud Foundation (VCF) 9. This progression highlights how complexity is progressively
  reduced at each level. If you are interested to learn more about Harbor and how
  to deploy it on a VM, check out our previous blog. Before diving into the specifics
  of VKS, let’s briefly outline the general steps for deploying the bare-minimum components
  of Harbor on any standard Kubernetes cluster (non production-ready). This foundational
  understanding will help you grasp the components involved. A running Kubernetes
  cluster (We will use VMware vSphere Kubernetes Service (VKS) for this, however the
  process remains the same for any upstream conformant Kubernetes platform). Additionally,
  configure kubectl to interact with your cluster. kubectl Helm (recommended) for
  simplified deployment.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/11/25/reducing-harbor-deployment-complexity-on-kubernetes/
