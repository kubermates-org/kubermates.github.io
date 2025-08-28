---
title: 'Blog: Post-Quantum Cryptography in Kubernetes'
date: '2025-07-18T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2025/07/18/pqc-in-k8s/
post_kind: link
draft: false
tldr: 'Post-Quantum Cryptography in Kubernetes What is Post-Quantum Cryptography Key
  exchange vs. digital signatures: different needs, different timelines State of PQC
  key exchange mechanisms (KEMs) today Post-quantum KEMs in Kubernetes: an unexpected
  arrival The Go version mismatch pitfall Limitations: packet size State of Post-Quantum
  Signatures Conclusion The world of cryptography is on the cusp of a major shift
  with the advent of quantum computing.'
summary: 'Post-Quantum Cryptography in Kubernetes What is Post-Quantum Cryptography
  Key exchange vs. digital signatures: different needs, different timelines State
  of PQC key exchange mechanisms (KEMs) today Post-quantum KEMs in Kubernetes: an
  unexpected arrival The Go version mismatch pitfall Limitations: packet size State
  of Post-Quantum Signatures Conclusion The world of cryptography is on the cusp of
  a major shift with the advent of quantum computing. While powerful quantum computers
  are still largely theoretical for many applications, their potential to break current
  cryptographic standards is a serious concern, especially for long-lived systems.
  This is where Post-Quantum Cryptography (PQC) comes in. In this article, I''ll dive
  into what PQC means for TLS and, more specifically, for the Kubernetes ecosystem.
  I’ll explain what the (suprising) state of PQC in Kubernetes is and what the implications
  are for current and future clusters. Post-Quantum Cryptography refers to cryptographic
  algorithms that are thought to be secure against attacks by both classical and quantum
  computers. The primary concern is that quantum computers, using algorithms like
  Shor''s Algorithm , could efficiently break widely used public-key cryptosystems
  such as RSA and Elliptic Curve Cryptography (ECC), which underpin much of today''s
  secure communication, including TLS. The industry is actively working on standardizing
  and adopting PQC algorithms. One of the first to be standardized by NIST is the
  Module-Lattice Key Encapsulation Mechanism ( ML-KEM ), formerly known as Kyber,
  and now standardized as FIPS-203 (PDF download). ML-KEM It is difficult to predict
  when quantum computers will be able to break classical algorithms. However, it is
  clear that we need to start migrating to PQC algorithms now, as the next section
  shows.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2025/07/18/pqc-in-k8s/
