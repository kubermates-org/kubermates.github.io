---
title: 'Before You Migrate: Five Surprising Ingress-NGINX Behaviors You Need to Know'
date: '2026-02-27T07:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2026/02/27/ingress-nginx-before-you-migrate/
post_kind: link
draft: false
tldr: 'Before You Migrate: Five Surprising Ingress-NGINX Behaviors You Need to Know
  1. Regex matches are prefix-based and case insensitive 2.'
summary: 'Before You Migrate: Five Surprising Ingress-NGINX Behaviors You Need to
  Know 1. Regex matches are prefix-based and case insensitive 2. The nginx. ingress.
  kubernetes. io/use-regex applies to all paths of a host across all (Ingress-NGINX)
  Ingresses 3. Rewrite target implies regex 4. Requests missing a trailing slash are
  redirected to the same path with a trailing slash 5. Ingress-NGINX normalizes URLs
  Conclusion As announced November 2025, Kubernetes will retire Ingress-NGINX in March
  2026. Despite its widespread usage, Ingress-NGINX is full of surprising defaults
  and side effects that are probably present in your cluster today. This blog highlights
  these behaviors so that you can migrate away safely and make a conscious decision
  about which behaviors to keep. This post also compares Ingress-NGINX with Gateway
  API and shows you how to preserve Ingress-NGINX behavior in Gateway API.'
---
Open the original post ↗ https://kubernetes.io/blog/2026/02/27/ingress-nginx-before-you-migrate/
