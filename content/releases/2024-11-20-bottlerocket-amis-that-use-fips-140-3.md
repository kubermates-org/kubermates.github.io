---
title: Bottlerocket AMIs that use FIPS 140-3
date: '2024-11-20T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/retrieve-ami-id-bottlerocket.html
post_kind: release
draft: false
tldr: Retrieve recommended Bottlerocket AMI IDs Help improve this page To contribute
  to this user guide, choose the Edit this page on GitHub link that is located in
  the right pane of every page. When deploying nodes, you can specify an ID for a
  pre-built Amazon EKS optimized Amazon Machine Image (AMI).
summary: 'Retrieve recommended Bottlerocket AMI IDs Help improve this page To contribute
  to this user guide, choose the Edit this page on GitHub link that is located in
  the right pane of every page. When deploying nodes, you can specify an ID for a
  pre-built Amazon EKS optimized Amazon Machine Image (AMI). To retrieve an AMI ID
  that fits your desired configuration, query the AWS Systems Manager Parameter Store
  API. Using this API eliminates the need to manually look up Amazon EKS optimized
  AMI IDs. For more information, see GetParameter. The IAM principal that you use
  must have the ssm:GetParameter IAM permission to retrieve the Amazon EKS optimized
  AMI metadata. ssm:GetParameter You can retrieve the image ID of the latest recommended
  Amazon EKS optimized Bottlerocket AMI with the following AWS CLI command, which
  uses the sub-parameter image_id. Make the following modifications to the command
  as needed and then run the modified command: image_id Replace kubernetes-version
  with a supported platform-version. Replace kubernetes-version with a supported platform-version.
  kubernetes-version Replace -flavor with one of the following options. Remove -flavor
  for variants without a GPU. Use -nvidia for GPU-enabled variants.'
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/retrieve-ami-id-bottlerocket.html
