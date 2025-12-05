---
title: Kubernetes Configuration Good Practices
date: '2025-11-25T00:00:00+00:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/11/25/configuration-good-practices/
post_kind: link
draft: false
tldr: 'Kubernetes Configuration Good Practices General configuration practices Use
  the latest stable API version Store configuration in version control Write configs
  in YAML not JSON Keep configuration simple and minimal Group related objects together
  Add helpful annotations Managing Workloads: Pods, Deployments, and Jobs Use Deployments
  for apps that should always be running Use Jobs for tasks that should finish Service
  Configuration and Networking Create Services before workloads that use them Use
  DNS for Service discovery Avoid hostPort and hostNetwork unless absolutely necessary
  Use headless Services for internal discovery Working with labels effectively Use
  semantics labels Use common Kubernetes labels Manipulate labels for debugging Handy
  kubectl tips Apply entire directories Use label selectors to get or delete resources
  Quickly create Deployments and Services Conclusion Configuration is one of those
  things in Kubernetes that seems small until it''s not. Configuration is at the heart
  of every Kubernetes workload.'
summary: 'Kubernetes Configuration Good Practices General configuration practices
  Use the latest stable API version Store configuration in version control Write configs
  in YAML not JSON Keep configuration simple and minimal Group related objects together
  Add helpful annotations Managing Workloads: Pods, Deployments, and Jobs Use Deployments
  for apps that should always be running Use Jobs for tasks that should finish Service
  Configuration and Networking Create Services before workloads that use them Use
  DNS for Service discovery Avoid hostPort and hostNetwork unless absolutely necessary
  Use headless Services for internal discovery Working with labels effectively Use
  semantics labels Use common Kubernetes labels Manipulate labels for debugging Handy
  kubectl tips Apply entire directories Use label selectors to get or delete resources
  Quickly create Deployments and Services Conclusion Configuration is one of those
  things in Kubernetes that seems small until it''s not. Configuration is at the heart
  of every Kubernetes workload. A missing quote, a wrong API version or a misplaced
  YAML indent can ruin your entire deploy. This blog brings together tried-and-tested
  configuration best practices. The small habits that make your Kubernetes setup clean,
  consistent and easier to manage. Whether you are just starting out or already deploying
  apps daily, these are the little things that keep your cluster stable and your future
  self sane. This blog is inspired by the original Configuration Best Practices page,
  which has evolved through contributions from many members of the Kubernetes community.
  Kubernetes evolves fast. Older APIs eventually get deprecated and stop working.
  So, whenever you are defining resources, make sure you are using the latest stable
  API version. You can always check with kubectl api-resources kubectl api-resources
  This simple step saves you from future compatibility issues. Never apply manifest
  files directly from your desktop.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/11/25/configuration-good-practices/
