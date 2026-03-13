---
title: 'VMware Cloud Foundation: Workaround for Quorum-Disk Failure Scenario in 2-Node
  WSFC 2025 Configuration'
date: '2026-03-09T20:45:18+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/03/09/vcf-workaround-for-quorum-disk-failure-scenario-in-2-node-wsfc-2025-configuration/
post_kind: link
draft: false
tldr: 'Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Cluster
  API, Immutability, and the Future of Kubernetes Infrastructure Where Logic and Creativity
  Meet: Libby Shen on Building Sustainable Solutions with VMware Cloud Foundation
  VMware Data Services Manager – DBaaS Solution for Private Cloud Synopsis Broadcom
  has published a 10-minute demo video that shows you how to work around a commonly
  reported failure scenario in 2-node Windows Server 2025 Failover Clusters (WSFC)
  when adding/configuring a quorum disk in VMware Cloud Foundation (VCF). Important:
  This video demonstrates a workaround for one symptom.'
summary: 'Discover more from VMware Cloud Foundation (VCF) Blog Related Articles Cluster
  API, Immutability, and the Future of Kubernetes Infrastructure Where Logic and Creativity
  Meet: Libby Shen on Building Sustainable Solutions with VMware Cloud Foundation
  VMware Data Services Manager – DBaaS Solution for Private Cloud Synopsis Broadcom
  has published a 10-minute demo video that shows you how to work around a commonly
  reported failure scenario in 2-node Windows Server 2025 Failover Clusters (WSFC)
  when adding/configuring a quorum disk in VMware Cloud Foundation (VCF). Important:
  This video demonstrates a workaround for one symptom. It does not resolve the underlying
  WSFC 2025 defect that can present as broader quorum/core-resource transition and
  failover reliability issues. Applies to • Windows Server 2025 Failover Clustering
  (2-node) • Shared disk / quorum disk configurations • VMware Cloud Foundation deployments
  (symptoms also reported outside vSphere) Customer-reported behavior (field symptom)
  Customers have reported WSFC 2025 failure scenarios where expected quorum/core-resource
  behavior breaks down in a 2-node cluster. Broadcom has documented a related failure
  mode (where shutting down an active VM holding cluster resources when the cluster
  has no roles can lead to a cluster-down condition) and notes Microsoft is actively
  investigating. Separately, similar 2-node quorum/ownership failure behavior is also
  described by customers in non-VCF environments (including 2-node configurations
  on Microsoft Hyper-V), confirming that the reported issues are not specifically
  hypervisor-related. What we’re releasing • A 10-minute demo video : This video shows
  a repeatable workaround to successfully complete quorum disk addition/configuration
  without triggering the Cluster failure condition. • Scope: workaround for this specific
  symptom only – does not claim to “fix WSFC 2025. ” Microsoft mitigation (shipped
  update and enablement flag) Microsoft has shipped Windows Server 2025 cumulative
  updates that customers commonly associate with the mitigation path, including KB5063878
  (August 12, 2025; OS Build 26100.4946). However, reports on Microsoft-hosted threads
  indicate the effective behavior may require an explicit FeatureManagement override
  registry value (2005146767) to be set (followed by a restart). VERIFY THE UPDATE
  IS PRESENT (POWERSHELL) GET-HOTFIX -ID KB5063878 ENABLE THE MITIGATION (CMD OR POWERSHELL,
  ELEVATED) REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CURRENTCONTROLSET\POLICIES\MICROSOFT\FEATUREMANAGEMENT\OVERRIDES
  /V 2005146767 /T REG_DWORD /D 1 /F DISABLE THE MITIGATION REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CURRENTCONTROLSET\POLICIES\MICROSOFT\FEATUREMANAGEMENT\OVERRIDES
  /V 2005146767 /T REG_DWORD /D 0 /F RETURN TO DEFAULT BEHAVIOR (REMOVE OVERRIDE)
  REG DELETE HKEY_LOCAL_MACHINE\SYSTEM\CURRENTCONTROLSET\POLICIES\MICROSOFT\FEATUREMANAGEMENT\OVERRIDES
  /V 2005146767 /F RESTART (REQUIRED) RESTART-COMPUTER Notes : • If you are actively
  experiencing cluster instability during quorum disk configuration, you are encouraged
  to start with the workaround shown in this video, then evaluate Microsoft’s shipped
  mitigation and override flag in a controlled maintenance window. • Community reports
  also describe broader “quorum/core resources don’t transition as expected” scenarios
  during node maintenance (including patching) in 2-node WSFC 2025.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/03/09/vcf-workaround-for-quorum-disk-failure-scenario-in-2-node-wsfc-2025-configuration/
