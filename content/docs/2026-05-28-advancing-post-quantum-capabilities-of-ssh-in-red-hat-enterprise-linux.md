---
title: Advancing post-quantum capabilities of SSH in Red Hat Enterprise Linux
date: '2026-05-28T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/advancing-post-quantum-capabilities-ssh-red-hat-enterprise-linux
post_kind: link
draft: false
tldr: Advancing post-quantum capabilities of SSH in Red Hat Enterprise Linux What's
  new for SSH in RHEL 10.2 Post-quantum SSH key exchange in FIPS mode Post-quantum
  key exchange support in libssh What's possible for SSH in the future Pure ML-KEM
  key exchange and post-quantum SSH keys GSSAPI key exchange with post-quantum cryptography
  Conclusion Red Hat Enterprise Linux | Product trial About the author Pavol Žáčik
  More like this 7 features of Red Hat Identity Management you need to know for the
  modern enterprise 4 reasons to start using image mode for Red Hat Enterprise Linux
  right now Collaboration In Product Security | Compiler Keeping Track Of Vulnerabilities
  With CVEs | Compiler Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The post-quantum cryptography (PQC) transition is well underway in Red Hat
  Enterprise Linux (RHEL). In May 2025, RHEL 10 delivered post-quantum key exchange
  algorithms in three major cryptography libraries (OpenSSL, GnuTLS, and NSS), making
  post-quantum key exchange usable in TLS 1.3 connections.
summary: 'Advancing post-quantum capabilities of SSH in Red Hat Enterprise Linux What''s
  new for SSH in RHEL 10.2 Post-quantum SSH key exchange in FIPS mode Post-quantum
  key exchange support in libssh What''s possible for SSH in the future Pure ML-KEM
  key exchange and post-quantum SSH keys GSSAPI key exchange with post-quantum cryptography
  Conclusion Red Hat Enterprise Linux | Product trial About the author Pavol Žáčik
  More like this 7 features of Red Hat Identity Management you need to know for the
  modern enterprise 4 reasons to start using image mode for Red Hat Enterprise Linux
  right now Collaboration In Product Security | Compiler Keeping Track Of Vulnerabilities
  With CVEs | Compiler Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The post-quantum cryptography (PQC) transition is well underway in Red Hat
  Enterprise Linux (RHEL). In May 2025, RHEL 10 delivered post-quantum key exchange
  algorithms in three major cryptography libraries (OpenSSL, GnuTLS, and NSS), making
  post-quantum key exchange usable in TLS 1.3 connections. RHEL 10.1 followed, setting
  the new key exchange algorithms as default in TLS, and introducing post-quantum
  signatures for RPM packages. The secure shell (SSH) protocol was not left behind.
  RHEL 10 shipped with OpenSSH 9.9, supporting two hybrid post-quantum key exchange
  methods: sntrup761x25519-sha512 combines classical X25519 key exchange with the
  lattice-based streamlined NTRU prime algorithm (SNTRUP), and mlkem768x25519-sha256
  combines X25519 with the module-lattice-based key-encapsulation mechanism ( ML-KEM
  ) standardized by the US National Institute of Standards and Technology (NIST).
  Beginning with RHEL 10.1, the latter is preferred by OpenSSH when establishing connections
  unless configured otherwise. Further PQC features of SSH were integrated into RHEL
  10.2. The RFC draft for mlkem768x25519-sha256 is currently being finalized by the
  Internet Engineering Task Force (IETF) Secure Shell Maintenance (SSHM) working group,
  and the algorithm is getting increasingly adopted by various SSH implementations.
  However, the draft also specifies two other hybrid key exchange algorithms: mlkem768nistp256-sha256
  and mlkem1024nistp384-sha384. These combine ML-KEM variants with elliptic-curve
  Diffie-Hellman (ECDH) key exchange over NIST-recommended curves (P-256 and P-384)
  instead of Curve25519. Because ML-KEM and ECDH over P-256/P-384 are all FIPS-approved,
  we''re making mlkem768nistp256-sha256 and mlkem1024nistp384-sha384 available as
  the only two post-quantum FIPS-compatible SSH key exchange algorithms in Red Hat
  Enterprise Linux 10.2. Although upstream OpenSSH maintainers decided not to implement
  these two additional hybrids, Red Hat customers can start using post-quantum cryptography
  in SSH in FIPS mode thanks to downstream patches of OpenSSH provided by Red Hat
  developers.'
---
Open the original post ↗ https://www.redhat.com/en/blog/advancing-post-quantum-capabilities-ssh-red-hat-enterprise-linux
