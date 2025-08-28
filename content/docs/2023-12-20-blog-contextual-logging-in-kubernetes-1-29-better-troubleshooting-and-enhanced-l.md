---
title: 'Blog: Contextual logging in Kubernetes 1.29: Better troubleshooting and enhanced
  logging'
date: '2023-12-20T09:30:00-08:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2023/12/20/contextual-logging/
post_kind: link
draft: false
tldr: 'Contextual logging in Kubernetes 1.29: Better troubleshooting and enhanced
  logging What is contextual logging? How to use it Performance impact Impact on downstream
  users Further reading Get involved On behalf of the Structured Logging Working Group
  and SIG Instrumentation , we are pleased to announce that the contextual logging
  feature introduced in Kubernetes v1.24 has now been successfully migrated to two
  components (kube-scheduler and kube-controller-manager) as well as some directories.
  This feature aims to provide more useful logs for better troubleshooting of Kubernetes
  and to empower developers to enhance Kubernetes.'
summary: 'Contextual logging in Kubernetes 1.29: Better troubleshooting and enhanced
  logging What is contextual logging? How to use it Performance impact Impact on downstream
  users Further reading Get involved On behalf of the Structured Logging Working Group
  and SIG Instrumentation , we are pleased to announce that the contextual logging
  feature introduced in Kubernetes v1.24 has now been successfully migrated to two
  components (kube-scheduler and kube-controller-manager) as well as some directories.
  This feature aims to provide more useful logs for better troubleshooting of Kubernetes
  and to empower developers to enhance Kubernetes. Contextual logging is based on
  the go-logr API. The key idea is that libraries are passed a logger instance by
  their caller and use that for logging instead of accessing a global logger. The
  binary decides the logging implementation, not the libraries. The go-logr API is
  designed around structured logging and supports attaching additional information
  to a logger. This enables additional use cases: The caller can attach additional
  information to a logger: WithName adds a “logger” key with the names concatenated
  by a dot as value WithValues adds key/value pairs When passing this extended logger
  into a function, and the function uses it instead of the global logger, the additional
  information is then included in all log entries, without having to modify the code
  that generates the log entries. This is useful in highly parallel applications where
  it can become hard to identify all log entries for a certain operation, because
  the output from different operations gets interleaved. The caller can attach additional
  information to a logger: WithName adds a “logger” key with the names concatenated
  by a dot as value WithValues adds key/value pairs When passing this extended logger
  into a function, and the function uses it instead of the global logger, the additional
  information is then included in all log entries, without having to modify the code
  that generates the log entries. This is useful in highly parallel applications where
  it can become hard to identify all log entries for a certain operation, because
  the output from different operations gets interleaved. When running unit tests,
  log output can be associated with the current test. Then, when a test fails, only
  the log output of the failed test gets shown by go test.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2023/12/20/contextual-logging/
