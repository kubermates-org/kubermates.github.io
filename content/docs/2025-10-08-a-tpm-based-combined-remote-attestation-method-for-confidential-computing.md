---
title: A TPM-based combined remote attestation method for confidential computing
date: '2025-10-08T14:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/08/a-tpm-based-combined-remote-attestation-method-for-confidential-computing/
post_kind: link
draft: false
tldr: 'Problem statement Scenario Representative existing approaches Our solution:
  Hybrid attestation with TPM and TEE integration Workflow overview Implementation
  with Hygon CSV Advantages of the combined approach Posted on October 8, 2025 by
  Andy, Confidential Computing Engineer,JD. COM Confidential computing technologies
  such as Intel TDX and AMD SNP rely on hardware-controlled Roots of Trust (RoT),
  inherently binding remote attestation to specific CPU vendors.'
summary: 'Problem statement Scenario Representative existing approaches Our solution:
  Hybrid attestation with TPM and TEE integration Workflow overview Implementation
  with Hygon CSV Advantages of the combined approach Posted on October 8, 2025 by
  Andy, Confidential Computing Engineer,JD. COM Confidential computing technologies
  such as Intel TDX and AMD SNP rely on hardware-controlled Roots of Trust (RoT),
  inherently binding remote attestation to specific CPU vendors. While these solutions
  offer strong security guarantees, they also introduce challenges for enterprises
  seeking compliance, transparency, and independence in managing their Trusted Execution
  Environments (TEEs). This raises key questions: How can organizations leverage TEE
  security features (e. g. , memory encryption, attestation) without being fully dependent
  on vendor-controlled RoT? Is it possible to partially decouple the RoT while maintaining
  robust security guarantees? Consider a large enterprise deploying Intel TDX or AMD
  SNP servers, but with a requirement that the Root of Trust (RoT) be shared with
  a third-party authority—such as an internal certificate authority (CA) or an industry-wide
  trust anchor—to enable independent verification and operational flexibility. The
  goal is to retain the security benefits of TEEs while mitigating vendor lock-in.
  Strengths: Fully vendor-agnostic and open-source. Utilizes TPM for attestation,
  minimizing reliance on CPU vendors. Fully vendor-agnostic and open-source. Utilizes
  TPM for attestation, minimizing reliance on CPU vendors. Considerations: Adopts
  an SGX-like, process-based isolation model, which, as of the time of this blog,
  may present compatibility challenges for integration with TDX/SNP ecosystems.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/08/a-tpm-based-combined-remote-attestation-method-for-confidential-computing/
