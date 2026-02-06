---
title: Build deep learning model training apps using CNCF Fluid with Amazon EKS
date: '2026-02-03T20:37:56+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/build-deep-learning-model-training-apps-using-cncf-fluid-with-amazon-eks/
post_kind: link
draft: false
tldr: Build deep learning model training apps using CNCF Fluid with Amazon EKS Deep
  learning data loading challenges and solutions Data loading bottleneck Challenges
  of managing parallel file systems The advantages of the file system built by Amazon
  EKS and CNCF Fluid Solution overview Achieve training data caching using and elastic
  high throughput file system using Amazon EKS and CNCF Fluid Achieve deep learning
  model training resource and workflow orchestration using Amazon EKS, KubeRay, and
  Ray Train Architecture design explanation Technical implementation Prerequisites
  Provision infrastructure on Amazon EKS Set up Fluid with JuiceFSRuntime on Amazon
  EKS Training data preparation and caching Amazon ECR image creation Create Ray Cluster
  Ray Job submission Ray Job monitoring Observability (optional) Cleaning up Conclusion
  About the authors Machine learning (ML) intensive companies face significant challenges
  in efficiently managing training data. This post introduces a solution to build
  an ephemeral, cloud-native elastic high-throughput file system.
summary: 'Build deep learning model training apps using CNCF Fluid with Amazon EKS
  Deep learning data loading challenges and solutions Data loading bottleneck Challenges
  of managing parallel file systems The advantages of the file system built by Amazon
  EKS and CNCF Fluid Solution overview Achieve training data caching using and elastic
  high throughput file system using Amazon EKS and CNCF Fluid Achieve deep learning
  model training resource and workflow orchestration using Amazon EKS, KubeRay, and
  Ray Train Architecture design explanation Technical implementation Prerequisites
  Provision infrastructure on Amazon EKS Set up Fluid with JuiceFSRuntime on Amazon
  EKS Training data preparation and caching Amazon ECR image creation Create Ray Cluster
  Ray Job submission Ray Job monitoring Observability (optional) Cleaning up Conclusion
  About the authors Machine learning (ML) intensive companies face significant challenges
  in efficiently managing training data. This post introduces a solution to build
  an ephemeral, cloud-native elastic high-throughput file system. By the end of this
  post, you will learn how to implement the elastic high-throughput file system using
  Amazon Elastic Kubernetes Service (Amazon EKS ) and CNCF Fluid , set up efficient
  data caching mechanisms, and orchestrate training workflows using KubeRay. This
  post targets DevOps engineers, MLOps specialists, and infrastructure architects
  who are responsible for building and optimizing ML training infrastructure in cloud
  environments, particularly those working with Amazon EKS and looking to enhance
  their deep learning training pipelines. You will need one hour to read through this
  post and two hours for the demo implementation. The cost for the resources is approximately
  $4 USD per hour. The following sections outline the deep learning data loading challenges
  and solutions. Data loading poses a major performance bottleneck in deep learning
  training systems, especially in large-scale operations. This challenge stems from
  two key issues: the need to repeatedly access many small files, and the constant
  back-and-forth communication between storage and computing systems. Distributed
  systems, complex datasets, random data access patterns, and extensive data augmentation
  amplify these problems during training. The significance of this bottleneck varies
  across different models and datasets but consistently remains a critical concern,
  particularly given the high costs of GPU computing resources. This makes it essential
  to optimize data loading for better hardware efficiency and faster training times.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/build-deep-learning-model-training-apps-using-cncf-fluid-with-amazon-eks/
