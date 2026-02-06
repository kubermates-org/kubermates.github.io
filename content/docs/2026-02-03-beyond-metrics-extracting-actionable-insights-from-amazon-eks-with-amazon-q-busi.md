---
title: 'Beyond metrics: Extracting actionable insights from Amazon EKS with Amazon
  Q Business'
date: '2026-02-03T21:08:57+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/beyond-metrics-extracting-actionable-insights-from-amazon-eks-with-amazon-q-business/
post_kind: link
draft: false
tldr: However, it can be very complex to monitor and understand the behavior of enterprise
  applications, and derive valuable insights from the extensive data produced by an
  application stack on Amazon EKS. Fortunately, the integration of Amazon EKS with
  Amazon Q Business provides a robust solution for uncovering actionable insights
  from your applications.
summary: 'However, it can be very complex to monitor and understand the behavior of
  enterprise applications, and derive valuable insights from the extensive data produced
  by an application stack on Amazon EKS. Fortunately, the integration of Amazon EKS
  with Amazon Q Business provides a robust solution for uncovering actionable insights
  from your applications. Amazon Q Business is a generative AI–powered assistant that
  can answer questions, provide summaries, generate content, and securely complete
  tasks based on data and information in your enterprise systems. Customers can use
  this fully managed service to query and analyze data from multiple sources, such
  as the control plane, data plane, request rates, and application logs. Furthermore,
  it offers organizations thorough insight into their applications and Kubernetes
  environments. In this post, we demonstrate a solution that uses Amazon Data Firehose
  to aggregate logs from the Amazon EKS control plane and data plane, and send them
  to Amazon Simple Storage Service (Amazon S3). Finally, we use Amazon Q Business
  and its Amazon S3 connector to synchronize the logs, index the log data in Amazon
  S3, and enable a chat experience powered by the generative AI capabilities of Amazon
  Q Business. The following architecture diagram shows the workflow that occurs when
  deploying the Terraform code that we use in this solution. The following steps detail
  how the EKS cluster is deployed with the retail sample application. Figure 1: Solution
  architecture diagram The user deploys the complete infrastructure stack including
  Amazon Virtual Private Cloud (Amazon VPC) , AWS Identity Access Management (IAM)
  roles, EKS cluster, and Amazon Q Business using a single Terraform execution. Application
  traffic flows through the Application Load Balancer (ALB) to the deployed sample
  retail application running on the EKS cluster. Amazon EKS Control Plane logs stored
  in Amazon CloudWatch get streamed to Amazon S3 through Amazon Data Firehose.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/beyond-metrics-extracting-actionable-insights-from-amazon-eks-with-amazon-q-business/
