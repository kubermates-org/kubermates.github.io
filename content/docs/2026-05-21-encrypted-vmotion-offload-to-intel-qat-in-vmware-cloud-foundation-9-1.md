---
title: Encrypted vMotion Offload to Intel QAT in VMware Cloud Foundation 9.1
date: '2026-05-21T16:20:37+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/05/21/encrypted-vmotion-offload-to-intel-qat-in-vmware-cloud-foundation-9-1/
post_kind: link
draft: false
tldr: 'First, let’s talk about encrypted vMotion Why Intel QAT changes the equation
  So, what does this actually get you? Does my hardware support this? The bigger picture
  Next steps Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Encrypted vMotion Offload to Intel QAT in VMware Cloud Foundation 9.1 Increase Deployment
  Flexibility with VCF Edge Automation 1.0.3 More Memory, Less Effort: Configuring
  Memory Tiering in VCF 9.1 Compute resources are expensive. One of the most common
  missed opportunities in enterprise infrastructure is not fully leveraging the hardware
  that is already in the rack.'
summary: 'First, let’s talk about encrypted vMotion Why Intel QAT changes the equation
  So, what does this actually get you? Does my hardware support this? The bigger picture
  Next steps Discover more from VMware Cloud Foundation (VCF) Blog Related Articles
  Encrypted vMotion Offload to Intel QAT in VMware Cloud Foundation 9.1 Increase Deployment
  Flexibility with VCF Edge Automation 1.0.3 More Memory, Less Effort: Configuring
  Memory Tiering in VCF 9.1 Compute resources are expensive. One of the most common
  missed opportunities in enterprise infrastructure is not fully leveraging the hardware
  that is already in the rack. Getting the most out of your investment requires careful
  mapping of what your hardware is actually capable of and what your software platform
  can take advantage of, and that alignment doesn’t always happen automatically. VMware
  Cloud Foundation 9.1 makes one of those alignments easier than you might think.
  If you’re running modern Intel Xeon processors, you likely already have Intel® QAT
  (QuickAssist Technology) built right into the chip. VCF 9.1 now knows how to take
  advantage of this technology in our favor. Specifically, it offloads encrypted vMotion
  operations to QAT, freeing up CPU cores that previously had no choice but to handle
  that work themselves. vMotion encryption has been around since vSphere 6.5, and
  the default behavior for VMs is what we call “opportunistic. ” Think of it this
  way: whenever your VMs move between ESX hosts running 6.5 or later, vSphere automatically
  tries to encrypt that migration traffic. No extra configuration needed. Hopefully
  you are no longer running vSphere 6.5 in your environment, as you are missing out
  a lot of great features. Based on telemetry, over 99% of vMotion operations today
  are encrypted.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/05/21/encrypted-vmotion-offload-to-intel-qat-in-vmware-cloud-foundation-9-1/
