---
title: General Availability for managed identity and workload identity on Microsoft
  Azure Red Hat OpenShift
date: '2026-02-02T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/general-availability-managed-identity-and-workload-identity-microsoft-azure-red-hat-openshift
post_kind: link
draft: false
tldr: General Availability for managed identity and workload identity on Microsoft
  Azure Red Hat OpenShift Why use managed identities? How to use managed identities
  Using identities for your applications What happens to managed identity clusters
  that were created during preview? Getting started Conclusion Red Hat OpenShift Container
  Platform | Product Trial About the author Oren Kashi More like this FedRAMP High
  Authorized Red Hat OpenShift Service on AWS GovCloud Red Hat OpenShift Service on
  AWS supports Capacity Reservations and Capacity Blocks for Machine Learning SREs
  on a plane | Technically Speaking Keep exploring Browse by channel Automation Artificial
  intelligence Open hybrid cloud Security Edge computing Infrastructure Applications
  Virtualization Share Support for managed identities and workload identities is now
  Generally Available (GA) for Microsoft Azure Red Hat OpenShift clusters. As a fully
  managed offering, Azure Red Hat OpenShift is a trusted, comprehensive and consistent
  application platform for building, deploying, and managing your applications at
  scale.
summary: General Availability for managed identity and workload identity on Microsoft
  Azure Red Hat OpenShift Why use managed identities? How to use managed identities
  Using identities for your applications What happens to managed identity clusters
  that were created during preview? Getting started Conclusion Red Hat OpenShift Container
  Platform | Product Trial About the author Oren Kashi More like this FedRAMP High
  Authorized Red Hat OpenShift Service on AWS GovCloud Red Hat OpenShift Service on
  AWS supports Capacity Reservations and Capacity Blocks for Machine Learning SREs
  on a plane | Technically Speaking Keep exploring Browse by channel Automation Artificial
  intelligence Open hybrid cloud Security Edge computing Infrastructure Applications
  Virtualization Share Support for managed identities and workload identities is now
  Generally Available (GA) for Microsoft Azure Red Hat OpenShift clusters. As a fully
  managed offering, Azure Red Hat OpenShift is a trusted, comprehensive and consistent
  application platform for building, deploying, and managing your applications at
  scale. It’s jointly operated and engineered by both Red Hat and Microsoft, providing
  an integrated support experience and allows organizations to focus on building and
  deploying applications, not managing the underlying infrastructure. This is a significant
  milestone that provides an enhanced security posture for how your Azure Red Hat
  OpenShift clusters access other Azure resources. This enables you to eliminate the
  complexity of managing service principal credentials and embrace a more streamlined
  and secure authentication process. As discussed in our previous blog , managed identities
  significantly enhance security by replacing long-term credentials, such as client
  secrets, with short-lived tokens. This approach minimizes the risk associated with
  compromise due to a token's brief lifespan and narrowly defined permissions. A further
  benefit is the reduction in operational overhead, as they eliminate the need for
  manual management and rotation of secrets, keys, and certificates. To use managed
  identities for an Azure Red Hat OpenShift cluster, you must create user-assigned
  managed identities for each Azure Red Hat OpenShift component and provide the proper
  role assignments over the required resources. Azure Red Hat OpenShift uses multiple
  user-assigned managed identities, each mapped to a particular operator or component.
  These identities are associated with a specific built-in role, with each role assignment
  scoped following the principles of least privilege. Once that is complete, you can
  use those in the creation of the cluster.
---
Open the original post ↗ https://www.redhat.com/en/blog/general-availability-managed-identity-and-workload-identity-microsoft-azure-red-hat-openshift
