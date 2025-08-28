---
title: Bottlerocket FIPS AMIs
date: '2025-03-27T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/bottlerocket-fips-amis.html
post_kind: release
draft: false
tldr: Make your worker nodes FIPS ready with Bottlerocket FIPS AMIs Considerations
  Create a managed node group with a Bottlerocket FIPS AMI Disable the FIPS endpoint
  for non-supported AWS Regions Help improve this page To contribute to this user
  guide, choose the Edit this page on GitHub link that is located in the right pane
  of every page. The Federal Information Processing Standard (FIPS) Publication 140-3
  is a United States and Canadian government standard that specifies the security
  requirements for cryptographic modules that protect sensitive information.
summary: Make your worker nodes FIPS ready with Bottlerocket FIPS AMIs Considerations
  Create a managed node group with a Bottlerocket FIPS AMI Disable the FIPS endpoint
  for non-supported AWS Regions Help improve this page To contribute to this user
  guide, choose the Edit this page on GitHub link that is located in the right pane
  of every page. The Federal Information Processing Standard (FIPS) Publication 140-3
  is a United States and Canadian government standard that specifies the security
  requirements for cryptographic modules that protect sensitive information. Bottlerocket
  makes it easier to adhere to FIPS by offering AMIs with a FIPS kernel. These AMIs
  are preconfigured to use FIPS 140-3 validated cryptographic modules. This includes
  the Amazon Linux 2023 Kernel Crypto API Cryptographic Module and the AWS-LC Cryptographic
  Module. Using Bottlerocket FIPS AMIs makes your worker nodes "FIPS ready" but not
  automatically "FIPS-compliant". For more information, see Federal Information Processing
  Standard (FIPS) 140-3. If your cluster uses isolated subnets, the Amazon ECR FIPS
  endpoint may not be accessible. This can cause the node bootstrap to fail. Make
  sure that your network configuration allows access to the necessary FIPS endpoints.
  For more information, see Access a resource through a resource VPC endpoint in the
  AWS PrivateLink Guide. If your cluster uses isolated subnets, the Amazon ECR FIPS
  endpoint may not be accessible.
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/bottlerocket-fips-amis.html
