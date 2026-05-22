---
title: 'What kubectl debug doesn’t tell you: The silent evidence gap'
date: '2026-05-18T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/05/18/what-kubectl-debug-doesnt-tell-you-the-silent-evidence-gap/
post_kind: link
draft: false
tldr: The session that left no record Reproduce it in three commands What gets lost
  in practice The incident response impact What can be done today Is this worth a
  KEP? Posted on May 18, 2026 by Shamsher Khan, CNCF Community Member CNCF projects
  highlighted in this post A kubectl debug session can contain the only direct observation
  of a failing system state. However, once the session ends, Kubernetes does not retain
  the termination context of that session in its API.
summary: 'The session that left no record Reproduce it in three commands What gets
  lost in practice The incident response impact What can be done today Is this worth
  a KEP? Posted on May 18, 2026 by Shamsher Khan, CNCF Community Member CNCF projects
  highlighted in this post A kubectl debug session can contain the only direct observation
  of a failing system state. However, once the session ends, Kubernetes does not retain
  the termination context of that session in its API. This is not a kubectl bug —
  it follows directly from the Kubernetes API design for ephemeral containers. Once
  the pod state changes, the Kubernetes API no longer exposes the termination context
  of that debug session. The exit code that encoded your finding, the duration of
  the session, which container you targeted — is not retained by the Kubernetes API
  after subsequent pod updates. Here is what that looks like, and what it means for
  your incident response workflow. You do not need a special cluster to see this.
  Any Kubernetes 1.25+ cluster works. Three commands confirm the gap. Step 1 — Deploy
  a stable target pod: kubectl run debug-target --image=nginx:alpine -n default kubectl
  wait --for=condition=Ready pod/debug-target -n default kubectl run debug-target
  --image=nginx:alpine -n default kubectl wait --for=condition=Ready pod/debug-target
  -n default Step 2 — Attach a debug session, run for 10 seconds, exit with a distinctive
  code: kubectl debug debug-target -n default \ --image=busybox:1.36 \ --target=nginx
  \ -it -- sh -c "echo ''finding: connection pool exhausted''; sleep 10; exit 42"
  kubectl debug debug-target -n default \ --image=busybox:1.36 \ --target=nginx \
  -it -- sh -c "echo ''finding: connection pool exhausted''; sleep 10; exit 42" Note:
  –target is a kubectl CLI feature that routes the debug container into the target
  container’s process namespace. The target container name is not stored as an API
  field on the pod object. kubectl Step 3 — Immediately after exit, inspect the ephemeral
  container status: kubectl get pod debug-target -n default \ -o jsonpath=''{.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/05/18/what-kubectl-debug-doesnt-tell-you-the-silent-evidence-gap/
