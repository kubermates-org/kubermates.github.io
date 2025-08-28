---
title: 'Optimizing RAG Pipelines with Katib: Hyperparameter Tuning for Better Retrieval
  &amp; Generation'
date: '2025-02-21T00:00:00-06:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/katib/rag/
post_kind: link
draft: false
tldr: 'Introduction Let’s Get Started! STEP 1: Setup STEP 2: Implementing RAG pipeline
  Implementation Details: STEP 3: Run a Katib Experiment Define hyperparameter search
  space Conclusion Introduction Let’s Get Started! STEP 1: Setup STEP 2: Implementing
  RAG pipeline Implementation Details: STEP 3: Run a Katib Experiment STEP 1: Setup
  STEP 2: Implementing RAG pipeline Implementation Details: Implementation Details:
  STEP 3: Run a Katib Experiment Define hyperparameter search space Conclusion As
  artificial intelligence and machine learning models become more sophisticated, optimising
  their performance remains a critical challenge. Kubeflow provides a robust component,
  Katib , designed for hyperparameter optimization and neural architecture search.'
summary: 'Introduction Let’s Get Started! STEP 1: Setup STEP 2: Implementing RAG pipeline
  Implementation Details: STEP 3: Run a Katib Experiment Define hyperparameter search
  space Conclusion Introduction Let’s Get Started! STEP 1: Setup STEP 2: Implementing
  RAG pipeline Implementation Details: STEP 3: Run a Katib Experiment STEP 1: Setup
  STEP 2: Implementing RAG pipeline Implementation Details: Implementation Details:
  STEP 3: Run a Katib Experiment Define hyperparameter search space Conclusion As
  artificial intelligence and machine learning models become more sophisticated, optimising
  their performance remains a critical challenge. Kubeflow provides a robust component,
  Katib , designed for hyperparameter optimization and neural architecture search.
  As a part of the Kubeflow ecosystem, Katib enables scalable, automated tuning of
  underlying machine learning models, reducing the manual effort required for parameter
  selection while improving model performance across diverse ML workflows. With Retrieval-Augmented
  Generation ( RAG ) becoming an increasingly popular approach for improving search
  and retrieval quality, optimizing its parameters is essential to achieving high-quality
  results. RAG pipelines involve multiple hyperparameters that influence retrieval
  accuracy, hallucination reduction, and language generation quality. In this blog,
  we will explore how Katib can be leveraged to fine-tune a RAG pipeline, ensuring
  optimal performance by systematically adjusting key hyperparameters. Since compute
  resources are scarcer than a perfectly labeled dataset :), we’ll use a lightweight
  Kind cluster (Kubernetes in Docker) cluster to run this example locally. Rest assured,
  this setup can seamlessly scale to larger clusters by increasing the dataset size
  and the number of hyperparameters to tune. To get started, we’ll first install the
  Katib control plane in our cluster by following the steps outlined in the documentation.
  In this implementation, we use a retriever model , which encodes queries and documents
  into vector representations to find the most relevant matches, to fetch relevant
  documents based on a query and a generator model to produce coherent text responses.
  Retriever: Sentence Transformer & FAISS (Facebook AI Similarity Search) Index A
  SentenceTransformer model (paraphrase-MiniLM-L6-v2) encodes predefined documents
  into vector representations. FAISS is used to index these document embeddings and
  perform efficient similarity searches to retrieve the most relevant documents.'
---
Open the original post ↗ https://blog.kubeflow.org/katib/rag/
