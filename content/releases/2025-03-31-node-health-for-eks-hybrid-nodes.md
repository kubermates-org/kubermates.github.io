---
title: Node health for EKS Hybrid Nodes
date: '2025-03-31T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/node-health.html
post_kind: release
draft: false
tldr: Help improve this page To contribute to this user guide, choose the Edit this
  page on GitHub link that is located in the right pane of every page. Node health
  refers to the operational status and capability of a node to effectively run workloads.
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. Node\
  \ health refers to the operational status and capability of a node to effectively\
  \ run workloads. A healthy node maintains expected connectivity, has sufficient\
  \ resources, and can successfully run Pods without disruption. For information on\
  \ getting details about your nodes, see View the health status of your nodes and\
  \ Retrieve node logs for a managed node using kubectl and S3. To help with maintaining\
  \ healthy nodes, Amazon EKS offers the node monitoring agent and node auto repair.\
  \ The node monitoring agent and node auto repair are only available on Linux. These\
  \ features arenâ\x80\x99t available on Windows. The node monitoring agent automatically\
  \ reads node logs to detect certain health issues. It parses through node logs to\
  \ detect failures and surfaces various status information about worker nodes. A\
  \ dedicated NodeCondition is applied on the worker nodes for each category of issues\
  \ detected, such as storage and networking issues. Descriptions of detected health\
  \ issues are made available in the observability dashboard. For more information,\
  \ see Node health issues."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/node-health.html
