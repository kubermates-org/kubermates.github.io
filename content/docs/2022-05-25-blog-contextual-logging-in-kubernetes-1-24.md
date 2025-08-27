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
tldr: 'Authors: Patrick Ohly (Intel) The Structured Logging Working Group has added
  new capabilities to the logging infrastructure in Kubernetes 1. 24.'
summary: 'Authors: Patrick Ohly (Intel) The Structured Logging Working Group has added
  new capabilities to the logging infrastructure in Kubernetes 1. 24. This blog post
  explains how developers can take advantage of those to make log output more useful
  and how they can get involved with improving Kubernetes. The goal of structured
  logging is to replace C-style formatting and the resulting opaque log strings with
  log entries that have a well-defined syntax for storing message and parameters separately,
  for example as a JSON struct. When using the traditional klog text output format
  for structured log calls, strings were originally printed with \n escape sequences,
  except when embedded inside a struct. For structs, log entries could still span
  multiple lines, with no clean way to split the log stream into individual entries:
  Now, the < and > markers along with indentation are used to ensure that splitting
  at a klog header at the start of a line is reliable and the resulting output is
  human-readable: Note that the log message itself is printed with quoting. It is
  meant to be a fixed string that identifies a log entry, so newlines should be avoided
  there. Before Kubernetes 1. 24, some log calls in kube-scheduler still used klog.
  Info for multi-line strings to avoid the unreadable output. Now all log calls have
  been updated to support structured logging. Contextual logging is based on the go-logr
  API.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2022/05/25/contextual-logging/
