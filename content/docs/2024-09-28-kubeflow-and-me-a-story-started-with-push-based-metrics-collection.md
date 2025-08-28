---
title: 'Kubeflow and Me: A Story Started with Push-based Metrics Collection'
date: '2024-09-28T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/gsoc-2024-project-6/
post_kind: link
draft: false
tldr: Problem Solution My Contributions during the GSoC Lessons Learned In the End
  Links This summer, I gained a precious opportunity to participate in the Google
  Summer of Code(GSoC), in which I would contribute to Katib and fulfill a project
  named “Push-based Metrics Collection in Katib” within 12 weeks. Firstly, I got to
  know about GSoC and Kubeflow with the recommendation from the former active maintainer
  Ce Gao(gaocegege)’s personal blog.
summary: 'Problem Solution My Contributions during the GSoC Lessons Learned In the
  End Links This summer, I gained a precious opportunity to participate in the Google
  Summer of Code(GSoC), in which I would contribute to Katib and fulfill a project
  named “Push-based Metrics Collection in Katib” within 12 weeks. Firstly, I got to
  know about GSoC and Kubeflow with the recommendation from the former active maintainer
  Ce Gao(gaocegege)’s personal blog. And I was deeply impressed by the idea of cloud
  native AI toolkits, I decided to dive into this area and learn some skills to enhance
  my career and future. In the blog, I’ll provide my personal insight into Katib,
  for those who are interested in cloud native, AI, and hyperparameters tuning. The
  project aims to provide a Python SDK API interface for users to push metrics to
  Katib DB directly. The current implementation of Metrics Collector is pull-based,
  raising design problems such as determining the frequency at which we scrape the
  metrics, performance issues like the overhead caused by too many sidecar containers,
  and restrictions on developing environments that must support sidecar containers
  and admission webhooks. And also, for data scientists, they need to pay attention
  to the format of metrics printed in the training scripts, which is error prone and
  may be hard to recognize. We decided to implement a new API for Katib Python SDK
  to offer users a push-based way to store metrics directly into the Kaitb DB and
  resolve those issues raised by pull-based metrics collection. In the new design,
  users just need to set metrics_collector_config={"kind": "Push"} in the tune() function
  and call the report_metrics() API in their objective function to push metrics to
  Katib DB directly. There are no sidecar containers and restricted metric log formats
  any more. After that, Trial Controller will continuously collect metrics from Katib
  DB and update the status of Trial, which is the same as pull-based metrics collection.
  metrics_collector_config={"kind": "Push"} tune() report_metrics() If you are interested
  in it, please refer to this doc and example for more details.'
---
Open the original post ↗ https://blog.kubeflow.org/gsoc-2024-project-6/
