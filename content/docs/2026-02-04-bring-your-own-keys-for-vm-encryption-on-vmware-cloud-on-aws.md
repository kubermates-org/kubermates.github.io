---
title: Bring Your Own Keys for VM Encryption on VMware Cloud on AWS
date: '2026-02-04T04:29:57+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/02/03/byok-vm-encryption-vmware-cloud-aws/
post_kind: link
draft: false
tldr: 'What is BYOK for VM encryption? How Does It Work? Getting Started in Four Steps
  Key Features and Capabilities Encryption operations Migration and disaster recovery
  Important Considerations Frequently Asked Questions Learn More Discover more from
  VMware Cloud Foundation (VCF) Blog Related Articles Modernizing EDA Infrastructure:
  Lessons from Samsung’s VCF Deployment How to Converge a VMware vSphere Environment
  to VMware Cloud Foundation 9.0 VCF Breakroom Chats Episode 83 – Designing Developer-Loved
  Platforms: What is an IDP? Updated: 02/05/2026 We are excited to announce that VMware
  Cloud on AWS now supports Bring Your Own Keys (BYOK) for VM encryption as part of
  the new version 1.26 release ! This capability enables you to integrate your own
  KMIP-compliant Key Management System (KMS) directly with VMware Cloud on AWS, giving
  you complete ownership and control of the encryption keys that protect your workloads.
  This feature is available now for all SDDCs running version 1.26 and above.'
summary: 'What is BYOK for VM encryption? How Does It Work? Getting Started in Four
  Steps Key Features and Capabilities Encryption operations Migration and disaster
  recovery Important Considerations Frequently Asked Questions Learn More Discover
  more from VMware Cloud Foundation (VCF) Blog Related Articles Modernizing EDA Infrastructure:
  Lessons from Samsung’s VCF Deployment How to Converge a VMware vSphere Environment
  to VMware Cloud Foundation 9.0 VCF Breakroom Chats Episode 83 – Designing Developer-Loved
  Platforms: What is an IDP? Updated: 02/05/2026 We are excited to announce that VMware
  Cloud on AWS now supports Bring Your Own Keys (BYOK) for VM encryption as part of
  the new version 1.26 release ! This capability enables you to integrate your own
  KMIP-compliant Key Management System (KMS) directly with VMware Cloud on AWS, giving
  you complete ownership and control of the encryption keys that protect your workloads.
  This feature is available now for all SDDCs running version 1.26 and above. BYOK
  for VM encryption allows you to use your own external, KMIP-compliant Key Management
  System to manage encryption keys for your virtual machines running on VMware Cloud
  on AWS. This means you hold and manage the keys that protect your workloads. This
  approach provides clear separation of concerns: your customer-managed keys protect
  your workload data, while the VMware Cloud on AWS control plane remains secured
  separately by AWS KMS, managed by Broadcom. Some key benefits include Data Sovereignty:
  Retain total control over your encryption keys to meet regional and regulatory compliance
  requirements. Compliance-Ready: Designed to align with European data sovereignty
  standards, including the Italian National Cybersecurity Agency Level 2 certification.
  Workload Security: Encrypt VMs using a customer-managed key provider that integrates
  seamlessly with VMware Cloud on AWS. Key Lifecycle Control: Manage key rotation,
  lifecycle events, and recovery—all on your terms. BYOK for VM encryption connects
  your external KMIP-compliant KMS with VMware Cloud on AWS through vSphere VM Encryption
  (VMcrypt). Your vCenter Server communicates with your external KMS over the KMIP
  protocol to request encryption keys when needed. These keys are used to encrypt
  virtual machine disks using VMcrypt.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/02/03/byok-vm-encryption-vmware-cloud-aws/
