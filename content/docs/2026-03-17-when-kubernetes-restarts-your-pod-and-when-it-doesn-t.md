---
title: When Kubernetes restarts your pod — And when it doesn’t
date: '2026-03-17T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/03/17/when-kubernetes-restarts-your-pod-and-when-it-doesnt/
post_kind: link
draft: false
tldr: 'The terminology problem The core insight: What kubelet actually watches Decision
  matrix Scenario 1: ConfigMap — Why the same change has two behaviors Lab Evidence
  (01-configmap/ in companion repo) Correct inotify pattern — watch the directory,
  not the file Scenario 2: Image updates — Recreation vs container restart vs CrashLoop
  Successful image update — pod is recreated ImagePullBackOff — old pod stays protected
  CrashLoopBackOff — same pod, restart count climbs Scenario 3: In-place resource
  resize (K8s 1.35 GA) Lab Evidence (05-resource-resize/ — requires K8s 1.35+) How
  to apply Scenario 4: Istio routing — Zero restarts via xDS Lab Evidence (04-istio-routing/
  in companion repo) Scenario 5: Stakater reloader — Automating the manual step Lab
  Evidence (07-stakater-reloader/ in companion repo) When hot-reload goes wrong Semantically
  invalid config accepted silently Envoy rejects xDS push silently Observability:
  Three commands every operator should know Conclusion Posted on March 17, 2026 by
  Shamsher Khan, Project Maintainer CNCF projects highlighted in this post A production
  internals guide verified against Kubernetes 1.35 GA Companion repository: github.
  com/opscart/k8s-pod-restart-mechanics Engineers say “the pod restarted” when they
  mean four different things.'
summary: 'The terminology problem The core insight: What kubelet actually watches
  Decision matrix Scenario 1: ConfigMap — Why the same change has two behaviors Lab
  Evidence (01-configmap/ in companion repo) Correct inotify pattern — watch the directory,
  not the file Scenario 2: Image updates — Recreation vs container restart vs CrashLoop
  Successful image update — pod is recreated ImagePullBackOff — old pod stays protected
  CrashLoopBackOff — same pod, restart count climbs Scenario 3: In-place resource
  resize (K8s 1.35 GA) Lab Evidence (05-resource-resize/ — requires K8s 1.35+) How
  to apply Scenario 4: Istio routing — Zero restarts via xDS Lab Evidence (04-istio-routing/
  in companion repo) Scenario 5: Stakater reloader — Automating the manual step Lab
  Evidence (07-stakater-reloader/ in companion repo) When hot-reload goes wrong Semantically
  invalid config accepted silently Envoy rejects xDS push silently Observability:
  Three commands every operator should know Conclusion Posted on March 17, 2026 by
  Shamsher Khan, Project Maintainer CNCF projects highlighted in this post A production
  internals guide verified against Kubernetes 1.35 GA Companion repository: github.
  com/opscart/k8s-pod-restart-mechanics Engineers say “the pod restarted” when they
  mean four different things. Getting this wrong leads to flawed runbooks and bad
  on-call decisions. The practical test: Did the pod UID change? If yes — that is
  recreation, not a container restart. Restart count resets to zero. If no — same
  pod object, container process restarted inside it. kubelet watches the pod spec
  — not ConfigMaps, not Secrets, not Istio CRDs. If the pod spec didn’t change, kubelet
  never fires. This single fact explains the majority of “why didn’t my config update?”
  investigations in production. Mutating admission webhooks can change the pod spec
  at creation time, but never after admission — they cannot trigger container restarts
  post-creation. The flowchart below translates the same matrix into a decision path
  you can walk at 2am during an incident. Diagram 1: Complete decision flowchart —
  does this change require a pod restart? [Diagram 1: ConfigMap env var vs volume
  mount — env var pod frozen, volume pod auto-synced via kubelet symlink swap] Env
  var mode (envFrom / valueFrom) : The kernel copies env vars into /proc/<pid>/environ
  at execve().'
---
Open the original post ↗ https://www.cncf.io/blog/2026/03/17/when-kubernetes-restarts-your-pod-and-when-it-doesnt/
