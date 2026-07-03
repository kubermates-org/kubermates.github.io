---
title: Dragonfly v2.5.0 is released
date: '2026-06-30T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/06/30/dragonfly-v2-5-0-is-released/
post_kind: link
draft: false
tldr: New features and enhancements Direct repository downloads from Hugging Face
  and ModelScope Blocklist for download control Comprehensive rate limiting dfctl
  command line tool Container registry proxy configuration simplification Client download
  and transfer optimization HTTP handling and redirect security improvements Additional
  enhancements Significant bug fixes Nydus New features and enhancements Significant
  bug fixes Others Links Dragonfly Github Posted on June 30, 2026 by Gaius Qi, Dragonfly
  Maintainer CNCF projects highlighted in this post Dragonfly v2.5.0 is released!
  Thanks to all of the contributors who made this Dragonfly release happen. Dragonfly
  Client now supports directly downloading model repositories from Hugging Face and
  ModelScope.
summary: New features and enhancements Direct repository downloads from Hugging Face
  and ModelScope Blocklist for download control Comprehensive rate limiting dfctl
  command line tool Container registry proxy configuration simplification Client download
  and transfer optimization HTTP handling and redirect security improvements Additional
  enhancements Significant bug fixes Nydus New features and enhancements Significant
  bug fixes Others Links Dragonfly Github Posted on June 30, 2026 by Gaius Qi, Dragonfly
  Maintainer CNCF projects highlighted in this post Dragonfly v2.5.0 is released!
  Thanks to all of the contributors who made this Dragonfly release happen. Dragonfly
  Client now supports directly downloading model repositories from Hugging Face and
  ModelScope. Users can run commands such as dfget hf://deepseek-ai/DeepSeek-OCR and
  dfget modelscope://models/deepseek-ai/DeepSeek-OCR to fetch repositories. Git LFS
  data is downloaded through Dragonfly P2P acceleration, while other repository metadata
  is fetched through the Git protocol. dfget hf://deepseek-ai/DeepSeek-OCR dfget modelscope://models/deepseek-ai/DeepSeek-OCR
  For more information, please refer to Hugging Face repository download and ModelScope
  repository download. Dragonfly Injector for Kubernetes Webhook Injection Dragonfly
  provides dragonfly-injector , a Kubernetes Mutating Admission Webhook for automatic
  P2P capability injection. It can inject Dragonfly client binaries and configurations,
  dfdaemon socket mounts, and CLI tools into application Pods through annotation-based
  policies, enabling Pods to use Dragonfly for file downloads without rebuilding container
  images. Helm Charts now also support deploying Dragonfly with webhook injection
  enabled. For more details, please refer to Using Dragonfly with webhook injection.
  Dragonfly supports configuring a blocklist in the Manager console to disable specific
  downloads. This can be used as an emergency measure to mitigate the impact of sudden
  abnormal requests on the service. When a blocked download is intercepted, gRPC downloads
  return a PermissionDenied error code, and HTTP proxy downloads return a FORBIDDEN
  status.
---
Open the original post ↗ https://www.cncf.io/blog/2026/06/30/dragonfly-v2-5-0-is-released/
