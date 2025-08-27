---
title: 'LLM Hyperparameter Optimization API: My Google Summer of Code Journey with
  Kubeflow'
date: '2024-09-19T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/gsoc-2024-project-4/
post_kind: link
draft: false
tldr: Sep 19, 2024 • Hezhi(Helen) Xie • 4 min read gsoc This summer, I had the opportunity
  to participate in the Google Summer of Code (GSoC) program, where I contributed
  to Kubeflow, an open-source machine learning toolkit. My project focused on developing
  a high-level API for optimizing hyperparameters in Large Language Models (LLMs)
  within Katib, Kubeflow’s automated hyperparameter tuning system.
summary: 'Sep 19, 2024 • Hezhi(Helen) Xie • 4 min read gsoc This summer, I had the
  opportunity to participate in the Google Summer of Code (GSoC) program, where I
  contributed to Kubeflow, an open-source machine learning toolkit. My project focused
  on developing a high-level API for optimizing hyperparameters in Large Language
  Models (LLMs) within Katib, Kubeflow’s automated hyperparameter tuning system. I’d
  like to share insights from this experience with others interested in Kubeflow,
  GSoC, or optimizing LLMs. The rapid advancements and rising popularity of LLMs,
  such as GPT and BERT, have created a growing demand for efficient LLMOps in Kubernetes.
  To address this, we have developed a train API within the Training Python SDK, simplifying
  the process of fine-tuning LLMs using distributed PyTorchJob workers. However, hyperparameter
  optimization remains a crucial yet labor-intensive task for enhancing model performance.
  Hyperparameter optimization is essential but time-consuming, especially for LLMs
  with billions of parameters. This API simplifies the process by handling Kubernetes
  infrastructure, allowing data scientists to focus on model performance rather than
  system configuration. With this API, users can import pretrained models and datasets
  from Hugging Face and Amazon S3, define parameters including the hyperparameter
  search space, optimization objective, and resource configuration. The API then automates
  the creation of Experiment, which contains multiple Trials with different hyperparameter
  settings using PyTorch distributed training. It then collects and analyzes the metrics
  from each Trial to identify the optimal hyperparameter configuration. For detailed
  instruction on using the API, please refer to this guide My work on the project
  can be broadly divided into four stages: In addition, I addressed several critical
  bugs in previous Katib and Training Operator releases and contributed new features,
  such as writing end-to-end tests for the train API.'
---
Open the original post ↗ https://blog.kubeflow.org/gsoc-2024-project-4/
