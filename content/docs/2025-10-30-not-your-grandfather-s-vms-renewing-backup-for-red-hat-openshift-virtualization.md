---
title: 'Not your grandfather''s VMs: Renewing backup for Red Hat OpenShift Virtualization'
date: '2025-10-30T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/netapp-backup-and-recovery-red-hat-openshift-virtualization
post_kind: link
draft: false
tldr: 'Not your grandfather''s VMs: Renewing backup for Red Hat OpenShift Virtualization
  Why old backup models break A solution for a modern platform Protect your investment,
  achieve resilience Further discovery 15 reasons to adopt Red Hat OpenShift Virtualization
  About the author Shane Heroux More like this Blog post Blog post Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Maybe you’re planning
  your migration right now, or you’ve done it (congratulations!) Joining industry
  leaders in the strategic move to Red Hat OpenShift Virtualization gives you the
  best of both worlds: The operational familiarity of a virtual machine (VM) combined
  with the agility and scalability of a Kubernetes-native platform. You''re running
  critical workloads in a modern, efficient way.'
summary: 'Not your grandfather''s VMs: Renewing backup for Red Hat OpenShift Virtualization
  Why old backup models break A solution for a modern platform Protect your investment,
  achieve resilience Further discovery 15 reasons to adopt Red Hat OpenShift Virtualization
  About the author Shane Heroux More like this Blog post Blog post Keep exploring
  Browse by channel Automation Artificial intelligence Open hybrid cloud Security
  Edge computing Infrastructure Applications Virtualization Share Maybe you’re planning
  your migration right now, or you’ve done it (congratulations!) Joining industry
  leaders in the strategic move to Red Hat OpenShift Virtualization gives you the
  best of both worlds: The operational familiarity of a virtual machine (VM) combined
  with the agility and scalability of a Kubernetes-native platform. You''re running
  critical workloads in a modern, efficient way. But have you stopped to ask the crucial
  question: "How are we protecting them?" If your answer involves traditional, hypervisor-level
  backup tools, you might have a significant gap in your data protection strategy.
  The simple truth is that a VM running on OpenShift is fundamentally different from
  one on a legacy hypervisor, and it demands a modern approach to backup and recovery.
  In a traditional virtualization stack, a VM is a relatively self-contained unit.
  Backing it up usually meant taking an agent-based or hypervisor-level snapshot of
  a VMDK or VHDX file on a datastore. Simple enough. But in OpenShift Virtualization,
  a VM is much more than a virtual disk file. It''s a composite application defined
  by a collection of interdependent Kubernetes resources. This includes the VirtualMachineInstance
  (VMI) itself, its DataVolumes and PersistentVolumeClaims (PVCs), along with associated
  ConfigMaps , Secrets , and network services that allow it to function. VirtualMachineInstance
  DataVolumes PersistentVolumeClaims ConfigMaps Secrets Backing up only the persistent
  volume is like saving your car''s engine but throwing away the chassis, wheels,
  and control system. You have a critical component, but you can''t actually rebuild
  the car.'
---
Open the original post ↗ https://www.redhat.com/en/blog/netapp-backup-and-recovery-red-hat-openshift-virtualization
