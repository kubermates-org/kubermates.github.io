---
title: 'Blog: Contextual Logging in Kubernetes 1.24'
date: '2022-05-25T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2022/05/25/contextual-logging/
post_kind: link
draft: false
tldr: 'Contextual Logging in Kubernetes 1. 24 Structured logging Contextual logging
  klog enhancements Contextual logging API ktesting logger klogr Reusable output test
  Output flushing Various other changes logcheck Next steps Authors: Patrick Ohly
  (Intel) The Structured Logging Working Group has added new capabilities to the logging
  infrastructure in Kubernetes 1.'
summary: 'Contextual Logging in Kubernetes 1. 24 Structured logging Contextual logging
  klog enhancements Contextual logging API ktesting logger klogr Reusable output test
  Output flushing Various other changes logcheck Next steps Authors: Patrick Ohly
  (Intel) The Structured Logging Working Group has added new capabilities to the logging
  infrastructure in Kubernetes 1. 24. This blog post explains how developers can take
  advantage of those to make log output more useful and how they can get involved
  with improving Kubernetes. The goal of structured logging is to replace C-style
  formatting and the resulting opaque log strings with log entries that have a well-defined
  syntax for storing message and parameters separately, for example as a JSON struct.
  When using the traditional klog text output format for structured log calls, strings
  were originally printed with \n escape sequences, except when embedded inside a
  struct. For structs, log entries could still span multiple lines, with no clean
  way to split the log stream into individual entries: \n I1112 14:06:35. 783529 328441
  structured_logging. go:51] "using InfoS" longData={Name:long Data:Multiple lines
  with quite a bit of text. internal:0} I1112 14:06:35. 783549 328441 structured_logging.
  go:52] "using InfoS with\nthe message across multiple lines" int=1 stringData="long:
  Multiple\nlines\nwith quite a bit\nof text.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2022/05/25/contextual-logging/
