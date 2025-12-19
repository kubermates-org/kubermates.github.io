---
title: Resilient model training on Red Hat OpenShift AI with Kubeflow Trainer
date: '2025-12-18T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/resilient-model-training-red-hat-openshift-ai-kubeflow-trainer
post_kind: link
draft: false
tldr: 'Resilient model training on Red Hat OpenShift AI with Kubeflow Trainer Problem:
  Training failures are expensive Real-world cost impact Challenges in shared cluster
  environments Periodic checkpointing and its limitations How periodic checkpointing
  works Critical limitations of periodic checkpointing The need for a better solution
  The solution: Just-in-time (JIT) checkpointing How JIT checkpointing works How JIT
  checkpointing overcomes periodic checkpointing limitations Windows of vulnerability
  Training interruption Unpredictable preemption Storage overhead Cost savings Use
  cases and common scenarios Kueue preemption protection Planned maintenance windows
  Resource rebalancing GPU-as-a-service Combining JIT with periodic checkpointing
  Red Hat OpenShift AI integration with Kubeflow Trainer v2 Coming soon: Full JIT
  checkpointing support Red Hat OpenShift AI (Self-Managed) | Product Trial About
  the author Esa Fazal More like this Looking ahead to 2026: Red Hat’s view across
  the hybrid cloud Red Hat to acquire Chatterbox Labs: Frequently Asked Questions
  Technically Speaking | Platform engineering for AI agents Technically Speaking |
  Driving healthcare discoveries with AI Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Imagine that after 60 hours of training, a large
  language model (LLM) on an 8x NVIDIA H100 GPU cluster costing $55 an hour, your
  job fails at 90% completion. You must restart from your last checkpoint, which was
  saved 3 hours ago, wasting $165 in compute costs, and delaying model deployment.'
summary: 'Resilient model training on Red Hat OpenShift AI with Kubeflow Trainer Problem:
  Training failures are expensive Real-world cost impact Challenges in shared cluster
  environments Periodic checkpointing and its limitations How periodic checkpointing
  works Critical limitations of periodic checkpointing The need for a better solution
  The solution: Just-in-time (JIT) checkpointing How JIT checkpointing works How JIT
  checkpointing overcomes periodic checkpointing limitations Windows of vulnerability
  Training interruption Unpredictable preemption Storage overhead Cost savings Use
  cases and common scenarios Kueue preemption protection Planned maintenance windows
  Resource rebalancing GPU-as-a-service Combining JIT with periodic checkpointing
  Red Hat OpenShift AI integration with Kubeflow Trainer v2 Coming soon: Full JIT
  checkpointing support Red Hat OpenShift AI (Self-Managed) | Product Trial About
  the author Esa Fazal More like this Looking ahead to 2026: Red Hat’s view across
  the hybrid cloud Red Hat to acquire Chatterbox Labs: Frequently Asked Questions
  Technically Speaking | Platform engineering for AI agents Technically Speaking |
  Driving healthcare discoveries with AI Keep exploring Browse by channel Automation
  Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Imagine that after 60 hours of training, a large
  language model (LLM) on an 8x NVIDIA H100 GPU cluster costing $55 an hour, your
  job fails at 90% completion. You must restart from your last checkpoint, which was
  saved 3 hours ago, wasting $165 in compute costs, and delaying model deployment.
  This kind of scenario isn''t hypothetical, it''s a daily reality for organizations
  running distributed AI training workloads in production environments. LLM training
  represents one of the most compute-intensive workloads in modern AI infrastructure.
  With GPU clusters costing thousands of dollars and training jobs running for days
  or weeks, any interruption can result in catastrophic financial losses and project
  delays. This article explores the challenges of distributed model training, examines
  the limitations of existing periodic checkpointing approaches, and introduces just-in-time
  (JIT) checkpointing, a new capability coming to Red Hat OpenShift AI 3.2 that protects
  your training investments while enabling new operational patterns like GPU-as-a-service
  and sustainable AI training practices. The financial and operational impact of training
  failures extends far beyond individual job restarts. Industry-facing studies show
  that a substantial fraction of GPU compute is wasted. For example, one study found
  many training jobs operating at less than 50% GPU utilization. Others show that
  interruptions and slowdowns due to failures or stragglers can delay job completion
  by roughly 2 times or more than planned. Taken together, findings across large-scale
  machine learning (ML) clusters suggest that 30% or more of GPU spending may be lost
  to idle time, interruptions, and inefficiencies. Consider a financial services organization
  training a fraud detection model on an 8 GPU cluster: Training duration : 72 hours
  planned GPU cost : $55/hour for 8 GPU cluster (AWS p5.'
---
Open the original post ↗ https://www.redhat.com/en/blog/resilient-model-training-red-hat-openshift-ai-kubeflow-trainer
