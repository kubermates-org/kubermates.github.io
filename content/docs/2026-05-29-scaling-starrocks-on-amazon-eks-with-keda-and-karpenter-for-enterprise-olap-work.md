---
title: Scaling StarRocks on Amazon EKS with KEDA and Karpenter for enterprise OLAP
  workloads
date: '2026-05-29T18:57:30+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/scaling-starrocks-on-amazon-eks-with-keda-and-karpenter-for-enterprise-olap-workloads/
post_kind: link
draft: false
tldr: 'Scaling StarRocks on Amazon EKS with KEDA and Karpenter for enterprise OLAP
  workloads The analytical challenge Benchmark results: StarRocks compared to ClickHouse
  Why we chose StarRocks Architecture on Amazon EKS Lessons learned and operational
  insights Conclusion Acknowledgements About the authors Financial analytics at enterprise
  scale is unforgiving. Queries must return in seconds, not minutes.'
summary: 'Scaling StarRocks on Amazon EKS with KEDA and Karpenter for enterprise OLAP
  workloads The analytical challenge Benchmark results: StarRocks compared to ClickHouse
  Why we chose StarRocks Architecture on Amazon EKS Lessons learned and operational
  insights Conclusion Acknowledgements About the authors Financial analytics at enterprise
  scale is unforgiving. Queries must return in seconds, not minutes. Thousands of
  finance professionals need concurrent access during monthly close cycles. And when
  data volumes grow from hundreds of gigabytes to terabytes, spanning billions of
  records, the infrastructure underneath must scale without forcing engineers to choose
  between performance and cost. This is the challenge the Amazon WW Stores FinTech
  team faced. We build and operate analytical products covering financial reporting,
  planning and allocation, self-serve analytics, and AI-powered financial insights,
  serving thousands of finance users every business day. As workloads scaled, the
  gap between what our systems could deliver and what our finance teams needed grew
  impossible to ignore. The demands were clear: Sub-second to single-digit-second
  query responses across terabytes of financial data Hundreds of concurrent users
  supported during peak business cycles Horizontal scaling without disruptive data
  rebalancing Our existing systems could satisfy one or two of these dimensions in
  isolation, but not all three simultaneously at the data volumes we were projecting.
  This wasn’t a migration problem, it was a greenfield opportunity to build the right
  analytical foundation from scratch. This post shares what we found, the architecture
  we built on Amazon Elastic Kubernetes Service (Amazon EKS) , and how we use KEDA
  and Karpenter to elastically scale StarRocks for bursty enterprise financial workloads.
  We partnered with the Data on EKS team on the reference blueprints that back this
  infrastructure. Financial analytics differs fundamentally from general operational
  analytics.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/scaling-starrocks-on-amazon-eks-with-keda-and-karpenter-for-enterprise-olap-workloads/
