---
title: VPC CNI troubleshooting content update
date: '2025-06-30T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/network-policies-troubleshooting.html
post_kind: release
draft: false
tldr: "Troubleshooting Kubernetes network policies For Amazon EKS New policyendpoints\
  \ CRD and permissions Network policy logs Amazon EKS add-on Self-managed add-on\
  \ Send network policy logs to Amazon CloudWatch Logs Included eBPF SDK Known issues\
  \ and solutions Network policy logs generated despite enable-policy-event-logs set\
  \ to false Network policy map cleanup issues Network policies arenâ\x80\x99t applied\
  \ Pods donâ\x80\x99t return to default deny state after policy deletion in strict\
  \ mode Security Groups for Pods startup latency FailedScheduling due to insufficient\
  \ vpc. amazonaws."
summary: "Troubleshooting Kubernetes network policies For Amazon EKS New policyendpoints\
  \ CRD and permissions Network policy logs Amazon EKS add-on Self-managed add-on\
  \ Send network policy logs to Amazon CloudWatch Logs Included eBPF SDK Known issues\
  \ and solutions Network policy logs generated despite enable-policy-event-logs set\
  \ to false Network policy map cleanup issues Network policies arenâ\x80\x99t applied\
  \ Pods donâ\x80\x99t return to default deny state after policy deletion in strict\
  \ mode Security Groups for Pods startup latency FailedScheduling due to insufficient\
  \ vpc. amazonaws. com/pod-eni IPAM connectivity issues and segmentation faults Failed\
  \ to find device by name error CVE vulnerabilities in Multus CNI image Flow Info\
  \ DENY verdicts in logs Pod-to-pod communication issues after migrating from Calico\
  \ Network policy agent doesnâ\x80\x99t support standalone pods Help improve this\
  \ page To contribute to this user guide, choose the Edit this page on GitHub link\
  \ that is located in the right pane of every page. This is the troubleshooting guide\
  \ for network policy feature of the Amazon VPC CNI. This guide covers: Install information,\
  \ CRD and RBAC permissions New policyendpoints CRD and permissions Install information,\
  \ CRD and RBAC permissions New policyendpoints CRD and permissions Logs to examine\
  \ when diagnosing network policy problems Network policy logs Logs to examine when\
  \ diagnosing network policy problems Network policy logs Running the eBPF SDK collection\
  \ of tools to troubleshoot Running the eBPF SDK collection of tools to troubleshoot\
  \ Known issues and solutions Known issues and solutions Known issues and solutions\
  \ Known issues and solutions Note that network policies are only applied to pods\
  \ that are made by Kubernetes Deployments. For more limitations of the network policies\
  \ in the VPC CNI, see Considerations. You can troubleshoot and investigate network\
  \ connections that use network policies by reading the Network policy logs and by\
  \ running tools from the eBPF SDK. policyendpoints CRD: policyendpoints. networking.\
  \ k8s. aws CRD: policyendpoints. networking."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/network-policies-troubleshooting.html
