---
title: What’s new with data science pipelines in Red Hat OpenShift AI
date: '2025-09-02T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/whats-new-data-science-pipelines-red-hat-openshift-ai
post_kind: link
draft: false
tldr: 'What’s new with data science pipelines in Red Hat OpenShift AI So, what exactly
  are data science pipelines in OpenShift AI? Creating a pipeline (and then what?)
  Cool new things in data science pipelines (from Kubeflow Pipelines 2.4. x) Flexible
  resource limits with placeholders Better control over parallel loops Reliable SubDAG
  Output resolution How these updates help you in OpenShift AI An important heads-up:
  The data science pipelines 2.0 change Wrapping up Learn more Get started with AI
  Inference About the author Alex Handy More like this Blog post Blog post Blog post
  Keep exploring Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share If
  you’ve ever struggled with manual, inconsistent, or expensive machine learning (ML)
  workflows (or if you''d love to have a formalized workflow at all), you’re not alone!
  Many teams hit roadblocks when trying to automate, scale, or manage their ML pipelines—especially
  as projects grow, scope creeps, and requirements inevitably change.'
summary: 'What’s new with data science pipelines in Red Hat OpenShift AI So, what
  exactly are data science pipelines in OpenShift AI? Creating a pipeline (and then
  what?) Cool new things in data science pipelines (from Kubeflow Pipelines 2.4. x)
  Flexible resource limits with placeholders Better control over parallel loops Reliable
  SubDAG Output resolution How these updates help you in OpenShift AI An important
  heads-up: The data science pipelines 2.0 change Wrapping up Learn more Get started
  with AI Inference About the author Alex Handy More like this Blog post Blog post
  Blog post Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share If you’ve ever struggled with manual, inconsistent, or expensive machine learning
  (ML) workflows (or if you''d love to have a formalized workflow at all), you’re
  not alone! Many teams hit roadblocks when trying to automate, scale, or manage their
  ML pipelines—especially as projects grow, scope creeps, and requirements inevitably
  change. Red Hat OpenShift AI now brings a set of updates to data science pipelines,
  making it easier than ever to control and optimize your ML processes. These improvements
  aren’t just about new features, they’re also about helping you optimize resource
  consumption and minimize the 2am on-call page-outs by building workflows you can
  trust in production. Think of a data science pipeline in OpenShift AI as the navigation
  system for your entire ML workflow. You can visually build this pipeline, which
  is powered by a structure called a directed acyclic graph (DAG). A DAG acts as the
  blueprint for your process, from data prep to deployment, by mapping out each task
  in a clear, one-way workflow. This structure is what makes sure that every step
  runs in the correct order and your pipeline doesn''t get stuck in an infinite loop.
  This blueprint or map is technically a graph where each component (a node) runs
  inside of a container on Red Hat OpenShift. These nodes are connected by edges (think
  of this as the arrows on a flow chart), which define their dependencies, so a task
  only runs after its prerequisites are met and the appropriate outputs go to the
  right places (the inputs of the next steps). The graph is "directed" because the
  workflow only moves forward and "acyclic" because it can''t circle back on itself.
  This workflow gives you precise control over your ML operations, making more efficient
  use of cluster resources.'
---
Open the original post ↗ https://www.redhat.com/en/blog/whats-new-data-science-pipelines-red-hat-openshift-ai
