---
title: 'Blog: Using Go workspaces in Kubernetes'
date: '2024-03-19T08:30:00-08:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2024/03/19/go-workspaces-in-kubernetes/
post_kind: link
draft: false
tldr: Using Go workspaces in Kubernetes GOPATH and Go modules The problems Enter workspaces
  The work Results Thanks The Go programming language has played a huge role in the
  success of Kubernetes. As Kubernetes has grown, matured, and pushed the bounds of
  what “regular” projects do, the Go project team has also grown and evolved the language
  and tools.
summary: Using Go workspaces in Kubernetes GOPATH and Go modules The problems Enter
  workspaces The work Results Thanks The Go programming language has played a huge
  role in the success of Kubernetes. As Kubernetes has grown, matured, and pushed
  the bounds of what “regular” projects do, the Go project team has also grown and
  evolved the language and tools. In recent releases, Go introduced a feature called
  “workspaces” which was aimed at making projects like Kubernetes easier to manage.
  We’ve just completed a major effort to adopt workspaces in Kubernetes, and the results
  are great. Our codebase is simpler and less error-prone, and we’re no longer off
  on our own technology island. Kubernetes is one of the most visible open source
  projects written in Go. The earliest versions of Kubernetes, dating back to 2014,
  were built with Go 1.3. Today, 10 years later, Go is up to version 1.22 — and let’s
  just say that a whole lot has changed. In 2014, Go development was entirely based
  on GOPATH. As a Go project, Kubernetes lived by the rules of GOPATH. In the buildup
  to Kubernetes 1.4 (mid 2016), we introduced a directory tree called staging. This
  allowed us to pretend to be multiple projects, but still exist within one git repository
  (which had advantages for development velocity).
---
Open the original post ↗ https://www.kubernetes.dev/blog/2024/03/19/go-workspaces-in-kubernetes/
