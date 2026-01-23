---
title: 'From IPVS to NFTables: A Migration Guide for Kubernetes v1.35'
date: '2026-01-13T19:28:59+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/from-ipvs-to-nftables-a-migration-guide-for-kubernetes-v1-35/
post_kind: link
draft: false
tldr: 'Kubernetes Networking Is Changing Calico and the Path Forward Why a Migration?
  Migration Guide – Prerequisites Verify The Current Mode Migrate Kube-Proxy to NFTables
  Update the ConfigMap Restart Kube-Proxy Verify Kube-Proxy Migration Switch Calico
  to NFTables Step 1: Patch the Installation Step 2: Verify Calico Migration Switch
  to Calico eBPF (High Performance) Next Steps for a Future-Proof Cluster 💬 Join the
  Conversation! Further Reading & Resources Kubernetes v1.35 marks an important turning
  point for cluster networking. The IPVS backend for kube-proxy has been officially
  deprecated, and future Kubernetes releases will remove it entirely.'
summary: 'Kubernetes Networking Is Changing Calico and the Path Forward Why a Migration?
  Migration Guide – Prerequisites Verify The Current Mode Migrate Kube-Proxy to NFTables
  Update the ConfigMap Restart Kube-Proxy Verify Kube-Proxy Migration Switch Calico
  to NFTables Step 1: Patch the Installation Step 2: Verify Calico Migration Switch
  to Calico eBPF (High Performance) Next Steps for a Future-Proof Cluster 💬 Join the
  Conversation! Further Reading & Resources Kubernetes v1.35 marks an important turning
  point for cluster networking. The IPVS backend for kube-proxy has been officially
  deprecated, and future Kubernetes releases will remove it entirely. If your clusters
  still rely on IPVS, the clock is now very much ticking. Staying on IPVS is not just
  a matter of running older technology. As upstream support winds down, IPVS receives
  less testing, fewer fixes, and less attention overall. Over time, this increases
  the risk of subtle breakage, makes troubleshooting harder, and limits compatibility
  with newer Kubernetes networking features. Eventually, upgrading Kubernetes will
  force a migration anyway, often at the worst possible time. Migrating sooner gives
  you control over the timing, space to test properly, and a chance to avoid turning
  a routine upgrade into an emergency networking change. Project Calico’s unique design
  with a pluggable data plane architecture is what makes this transition possible
  without redesigning cluster networking from scratch. Calico supports a wide range
  of technologies, including eBPF, iptables , IPVS, Windows HNS, VPP, and nftables
  , allowing clusters to choose the most appropriate backend for their environment.
  This flexibility enables clusters to evolve alongside Kubernetes rather than being
  locked into a single implementation. iptables nftables When Tigera added IPVS support
  in 2019, it addressed real scalability limitations in iptables and became the right
  choice for many large clusters.'
---
Open the original post ↗ https://www.tigera.io/blog/from-ipvs-to-nftables-a-migration-guide-for-kubernetes-v1-35/
