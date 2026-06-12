---
title: Expiration of Secure Boot signing certificates in 2026
date: '2026-06-10T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/expiration-secure-boot-signing-certificates-2026
post_kind: link
draft: false
tldr: 'Expiration of Secure Boot signing certificates in 2026 What is Secure Boot?
  How does Secure Boot work? How is Microsoft involved in this? What is happening
  in June 2026? What is Red Hat doing in response to the situation? What about RHEL
  7.9? What will happen when a new version of shim is needed? Should I update my firmware
  db? How do I update my firmware db? Are there any risks associated with updating
  the firmware db? Helpful commands related to Secure Boot More information about
  Secure Boot Red Hat Enterprise Linux | Product trial About the authors Marta Lewandowska
  Peter Jones More like this Planning your path forward from Amazon Linux 2: Why consistency
  is the ultimate upgrade 4 reasons to start using image mode for Red Hat Enterprise
  Linux right now Operating System Management | Compiler OS Wars_part 1 | Command
  Line Heroes Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The keys that Microsoft uses to sign for Secure Boot are expiring at the end
  of June 2026. Here is what you need to know: Secure Boot-enabled systems will continue
  to boot after June 2026 whether they are immediately updated or not.'
summary: 'Expiration of Secure Boot signing certificates in 2026 What is Secure Boot?
  How does Secure Boot work? How is Microsoft involved in this? What is happening
  in June 2026? What is Red Hat doing in response to the situation? What about RHEL
  7.9? What will happen when a new version of shim is needed? Should I update my firmware
  db? How do I update my firmware db? Are there any risks associated with updating
  the firmware db? Helpful commands related to Secure Boot More information about
  Secure Boot Red Hat Enterprise Linux | Product trial About the authors Marta Lewandowska
  Peter Jones More like this Planning your path forward from Amazon Linux 2: Why consistency
  is the ultimate upgrade 4 reasons to start using image mode for Red Hat Enterprise
  Linux right now Operating System Management | Compiler OS Wars_part 1 | Command
  Line Heroes Keep exploring Browse by channel Automation Artificial intelligence
  Open hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share The keys that Microsoft uses to sign for Secure Boot are expiring at the end
  of June 2026. Here is what you need to know: Secure Boot-enabled systems will continue
  to boot after June 2026 whether they are immediately updated or not. Red Hat has
  released new shims, signed by multiple certificates, for all supported RHEL 9 and
  RHEL 10 streams; RHEL 8 will receive the new shim in June 2026. To prepare your
  systems for the future, it’s best to update your firmware database, if an update
  is available, and update your shim. UEFI Secure Boot is a security feature that
  permits only signed, trusted components to boot on your system. This means the bootloader(s)
  that start the machine and load the kernel—the kernel itself—which is the heart
  of the operating system (OS), and the kernel modules are signed. Allowing only trusted
  components to load prevents malicious bootkits or rootkits from getting installed.
  UEFI Secure Boot is only available on x86_64 machines running UEFI firmware and
  aarch64 machines. Importantly, the information in this article is relevant only
  to x86_64. Red Hat-enabled Secure Boot on aarch64 quite recently, and the aarch64
  shim is signed with the 2023 key only. Key pairs are generated using cryptographic
  algorithms. One half of the key pair is the private key, which is kept secret and
  used to sign applications.'
---
Open the original post ↗ https://www.redhat.com/en/blog/expiration-secure-boot-signing-certificates-2026
