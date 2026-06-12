---
title: 'Kubernetes v1.36: Admission Policies That Can''t Be Deleted'
date: '2026-05-04T10:35:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/
post_kind: link
draft: false
tldr: 'Kubernetes v1.36: Admission Policies That Can''t Be Deleted The gap we''re
  closing How it works Protecting what couldn''t be protected before A few things
  to know Try it out How to get involved If you''ve ever tried to enforce a security
  policy across a fleet of Kubernetes clusters, you''ve probably run into a frustrating
  chicken-and-egg problem. Your admission policies are API objects, which means they
  don''t exist until someone creates them, and they can be deleted by anyone with
  the right permissions.'
summary: 'Kubernetes v1.36: Admission Policies That Can''t Be Deleted The gap we''re
  closing How it works Protecting what couldn''t be protected before A few things
  to know Try it out How to get involved If you''ve ever tried to enforce a security
  policy across a fleet of Kubernetes clusters, you''ve probably run into a frustrating
  chicken-and-egg problem. Your admission policies are API objects, which means they
  don''t exist until someone creates them, and they can be deleted by anyone with
  the right permissions. There''s always a window during cluster bootstrap where your
  policies aren''t active yet, and there''s no way to prevent a privileged user from
  removing them. Kubernetes v1.36 introduces an alpha feature that addresses this:
  manifest-based admission control. It lets you define admission webhooks and CEL
  -based policies as files on disk, loaded by the API server at startup, before it
  serves any requests. Most Kubernetes policy enforcement today works through the
  API. You create a ValidatingAdmissionPolicy or a webhook configuration as an API
  object, and the admission controller picks it up. This works well in steady state,
  but it has some fundamental limitations. During cluster bootstrap, there''s a gap
  between when the API server starts serving requests and when your policies are created
  and active. If you''re restoring from a backup or recovering from an etcd failure,
  that gap can be significant. There''s also a self-protection problem. Admission
  webhooks and policies can''t intercept operations on their own configuration resources.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/
