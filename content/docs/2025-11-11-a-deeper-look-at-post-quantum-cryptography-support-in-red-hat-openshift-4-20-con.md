---
title: A deeper look at post-quantum cryptography support in Red Hat OpenShift 4.20
  control plane
date: '2025-11-11T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/deeper-look-post-quantum-cryptography-support-red-hat-openshift-420-control-plane
post_kind: link
draft: false
tldr: 'A deeper look at post-quantum cryptography support in Red Hat OpenShift 4.20
  control plane The quantum threat PQC in Kubernetes and OpenShift Applying PQC to
  the OpenShift control plane The Red Hat perspective The Go version mismatch What
  about etcd? The road ahead Red Hat OpenShift Container Platform | Product Trial
  About the author JP Jung More like this Blog post Blog post Original podcast Original
  podcast Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The age of quantum computing is on the horizon, and with its immense processing
  power comes a significant threat to the cryptographic foundations of our digital
  world. In this article, we''ll explore the emerging support for post-quantum cryptography
  (PQC) in Red Hat OpenShift 4.20 , focusing on how it enhances the core components
  of the Kubernetes control plane: the apiserver, kubelet, scheduler, and controller-manager.'
summary: 'A deeper look at post-quantum cryptography support in Red Hat OpenShift
  4.20 control plane The quantum threat PQC in Kubernetes and OpenShift Applying PQC
  to the OpenShift control plane The Red Hat perspective The Go version mismatch What
  about etcd? The road ahead Red Hat OpenShift Container Platform | Product Trial
  About the author JP Jung More like this Blog post Blog post Original podcast Original
  podcast Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The age of quantum computing is on the horizon, and with its immense processing
  power comes a significant threat to the cryptographic foundations of our digital
  world. In this article, we''ll explore the emerging support for post-quantum cryptography
  (PQC) in Red Hat OpenShift 4.20 , focusing on how it enhances the core components
  of the Kubernetes control plane: the apiserver, kubelet, scheduler, and controller-manager.
  Missing is etcd, using an older version of Go. Today''s widely used public-key cryptosystems,
  such as RSA and elliptic curve cryptography (ECC), form the foundation of security-enhanced
  online communication. These systems are vulnerable to attacks from large-scale quantum
  computers, however, which can solve the mathematical problems underlying these algorithms
  with alarming speed. This has given rise to attacks in which adversaries record
  encrypted traffic today to decrypt it in the future once they have access to a powerful
  quantum computer. The same challenge applies to data at rest if an adversary manages
  to make a copy now to decrypt later. To counter this threat, the field of PQC has
  emerged, developing new cryptographic algorithms that are resistant to attacks from
  both classical and quantum computers. Red Hat OpenShift is a Cloud Native Computing
  Foundation (CNCF) certified distribution of Kubernetes, and Kubernetes is written
  in the Go programming language. Thus, the journey to PQC support in OpenShift begins
  with Go. The Go 1.24 release marked a significant milestone by introducing support
  for the X25519MLKEM768 hybrid key exchange mechanism. X25519MLKEM768 is a hybrid
  key exchange that combines classical X25519 (elliptic curve Diffie-Hellman) with
  ML-KEM-768 (the post-quantum algorithm).'
---
Open the original post ↗ https://www.redhat.com/en/blog/deeper-look-post-quantum-cryptography-support-red-hat-openshift-420-control-plane
