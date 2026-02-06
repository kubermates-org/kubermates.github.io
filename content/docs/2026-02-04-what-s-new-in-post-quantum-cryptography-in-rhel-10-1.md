---
title: What’s new in post-quantum cryptography in RHEL 10.1
date: '2026-02-04T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/whats-new-post-quantum-cryptography-rhel-101
post_kind: link
draft: false
tldr: 'What’s new in post-quantum cryptography in RHEL 10.1 Post-quantum cryptography
  in TLS PQC by DEFAULT policy Package updates with post-quantum signatures Conclusion
  Red Hat Product Security About the author Clemens Lang More like this Introducing
  OpenShift Service Mesh 3.2 with Istio’s ambient mode From if to how: A year of post-quantum
  reality Data Security And AI | Compiler Data Security 101 | Compiler Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share In May 2025, Red
  Hat Enterprise Linux 10 (RHEL) shipped with the first steps toward post-quantum
  cryptography (PQC) to protect against attacks by quantum computers, which will make
  attacks on existing classic cryptographic algorithms such as RSA and elliptic curves
  feasible. Cryptographically relevant quantum computers (CRQC) are still not known
  to exist, but that does not mean the risk is zero.'
summary: 'What’s new in post-quantum cryptography in RHEL 10.1 Post-quantum cryptography
  in TLS PQC by DEFAULT policy Package updates with post-quantum signatures Conclusion
  Red Hat Product Security About the author Clemens Lang More like this Introducing
  OpenShift Service Mesh 3.2 with Istio’s ambient mode From if to how: A year of post-quantum
  reality Data Security And AI | Compiler Data Security 101 | Compiler Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share In May 2025, Red
  Hat Enterprise Linux 10 (RHEL) shipped with the first steps toward post-quantum
  cryptography (PQC) to protect against attacks by quantum computers, which will make
  attacks on existing classic cryptographic algorithms such as RSA and elliptic curves
  feasible. Cryptographically relevant quantum computers (CRQC) are still not known
  to exist, but that does not mean the risk is zero. For example, "harvest now, decrypt
  later" attacks do not need a quantum computer now, one only needs to become available
  before the stored encrypted data loses its value, and depending on the transferred
  data, decades might pass before that happens. To prepare for a quantum future, RHEL
  10.1 improves defenses against such “harvest now, decrypt later” attacks and introduces
  post-quantum signatures for its packages. The next section covers changes to PQC
  in Transport Layer Security (TLS), followed by a section explaining a change in
  the default cryptography policies of RHEL. Did you know RHEL is the first major
  Linux distribution to sign its packages with hybrid post-quantum keys? The third
  section covers the details of these changes, before finishing with recommended next
  steps for users and third-party software vendors. TLS can use post-quantum cryptography
  in two places: Key exchange, where it protects against "harvest now, decrypt later"
  attacks, and signatures, preventing machine-in-the-middle attacks that use quantum
  computers. With the release of RHEL 10.1, applications that use OpenSSL, GnuTLS,
  NSS, or the Go programming language have support for post-quantum key exchange enabled
  by default. The OpenSSL, GnuTLS, and NSS cryptography libraries additionally support
  signatures and TLS certificates with Module-Lattice-Based Digital Signature Algorithm
  (ML-DSA), a NIST-standardized PQC algorithm. Note that no public Certificate Authorities
  (CAs) currently offer post-quantum cryptography, but private CAs or self-signed
  certificates can be created with ML-DSA today. In RHEL 10.0 , this functionality
  was released as technology preview due to the quickly evolving nature of standards
  and implementations. This is now changing: post-quantum cryptography with Module-Lattice-Based
  Key Encapsulation Mechanism (ML-KEM) and ML-DSA in TLS is generally available and
  fully supported in Go, OpenSSL, GnuTLS and NSS.'
---
Open the original post ↗ https://www.redhat.com/en/blog/whats-new-post-quantum-cryptography-rhel-101
