---
title: Modernizing Kubeflow Pipelines UI
date: '2026-03-31T00:00:00-05:00'
tags:
- kubeflow
- kubernetes
source: Kubeflow Blog
external_url: https://blog.kubeflow.org/modernizing-kubeflow-pipelines-ui/
post_kind: link
draft: false
tldr: 'What’s changing for users A faster, more responsive interface Smoother pipeline
  graph navigation Improved charts and metrics display Better accessibility No breaking
  changes Why we made this change How we got here React 16 → 17: Rebuilding the foundation
  React 17 → 18: The biggest leap React 18 → 19: The final stretch The full stack
  transformation By the numbers Want to contribute? What’s changing for users A faster,
  more responsive interface Smoother pipeline graph navigation Improved charts and
  metrics display Better accessibility No breaking changes A faster, more responsive
  interface Smoother pipeline graph navigation Improved charts and metrics display
  Better accessibility No breaking changes Why we made this change How we got here
  React 16 → 17: Rebuilding the foundation React 17 → 18: The biggest leap React 18
  → 19: The final stretch React 16 → 17: Rebuilding the foundation React 17 → 18:
  The biggest leap React 18 → 19: The final stretch The full stack transformation
  By the numbers Want to contribute? The Kubeflow Pipelines web interface has been
  upgraded from React 16 to React 19 — a modernization effort that touches every layer
  of the frontend stack. Whether you use the UI to manage pipelines day-to-day or
  contribute to the codebase, here is what this means for you.'
summary: 'What’s changing for users A faster, more responsive interface Smoother pipeline
  graph navigation Improved charts and metrics display Better accessibility No breaking
  changes Why we made this change How we got here React 16 → 17: Rebuilding the foundation
  React 17 → 18: The biggest leap React 18 → 19: The final stretch The full stack
  transformation By the numbers Want to contribute? What’s changing for users A faster,
  more responsive interface Smoother pipeline graph navigation Improved charts and
  metrics display Better accessibility No breaking changes A faster, more responsive
  interface Smoother pipeline graph navigation Improved charts and metrics display
  Better accessibility No breaking changes Why we made this change How we got here
  React 16 → 17: Rebuilding the foundation React 17 → 18: The biggest leap React 18
  → 19: The final stretch React 16 → 17: Rebuilding the foundation React 17 → 18:
  The biggest leap React 18 → 19: The final stretch The full stack transformation
  By the numbers Want to contribute? The Kubeflow Pipelines web interface has been
  upgraded from React 16 to React 19 — a modernization effort that touches every layer
  of the frontend stack. Whether you use the UI to manage pipelines day-to-day or
  contribute to the codebase, here is what this means for you. You do not need to
  do anything differently. Your bookmarks, workflows, and browser all work exactly
  as before. But under the hood, the UI is now built on a modern foundation that delivers
  tangible improvements: React 18 introduced automatic batching, which reduces unnecessary
  re-renders across the UI. In practice, this means pages like Run Details, Experiment
  Details, and the pipeline creation flow respond faster to your interactions. Forms
  validate without flicker, and multi-step workflows feel snappier. The production
  bundle size stayed exactly the same — 0% increase — so page load times are unchanged.
  The pipeline DAG visualization (the graph you see when inspecting a pipeline’s structure)
  has been migrated from the deprecated react-flow-renderer to @xyflow/react. This
  brings improved pan, zoom, and drag performance, especially on larger or more complex
  pipeline graphs. If you’ve ever experienced sluggishness when navigating a deeply
  nested pipeline, this upgrade directly addresses that. Run metrics and comparison
  charts now use Recharts instead of the deprecated react-vis library.'
---
Open the original post ↗ https://blog.kubeflow.org/modernizing-kubeflow-pipelines-ui/
