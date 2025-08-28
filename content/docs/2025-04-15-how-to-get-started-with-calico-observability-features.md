---
title: How to get started with Calico Observability features
date: '2025-04-15T15:37:28+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/how-to-get-started-with-calico-observability-features/
post_kind: link
draft: false
tldr: The Need for a Zero Trust Model Simplifying Network Flow Visibility with Calico
  Whisker Using Calico Whisker to Secure the ANP Demo APP What if you missed something?
  Conclusion Kubernetes, by default, adopts a permissive networking model where all
  pods can freely communicate unless explicitly restricted using network policies.
  While this simplifies application deployment, it introduces significant security
  risks.
summary: 'The Need for a Zero Trust Model Simplifying Network Flow Visibility with
  Calico Whisker Using Calico Whisker to Secure the ANP Demo APP What if you missed
  something? Conclusion Kubernetes, by default, adopts a permissive networking model
  where all pods can freely communicate unless explicitly restricted using network
  policies. While this simplifies application deployment, it introduces significant
  security risks. Unrestricted network traffic allows workloads to interact with unauthorized
  destinations, increasing the potential for cyberattacks such as Remote Code Execution
  (RCE), DNS spoofing, and privilege escalation. To better understand these problems,
  let’s examine a sample Kubernetes application: ANP Demo App. This application comprises
  a deployment that spawns pods and a service that exposes them to external users
  in a similar situation like any real word workload which you will encounter in your
  environment. If you open the application service before implementing any policies,
  the application reports the following messages: Container can reach the Internet
  – Without network policies, an attacker can use our container as an entry point
  by exploiting it with a vulnerability. This could allow them to exfiltrate data
  or establish remote control over the workload by leveraging its Internet access.
  Container can reach CoreDNS Pods – Kubernetes relies heavily on DNS, with records
  served using CoreDNS Pods. While communication between your Pods and CoreDNS is
  essential and not inherently a vulnerability, pairing it with unrestricted access
  to external DNS servers creates a significant security risk such as cluster wide
  DNS poisoning from a vulnerable pod or a pod with access to NET_RAW capabilities.
  Container can reach external DNS servers – Without restricting network policies,
  attackers can leverage techniques such as DNS poisoning, where they manipulate DNS
  responses to redirect traffic to malicious destinations. Container can reach the
  Kubernetes API Server – Often overlooked but without network policies all workloads
  can access the host via local networking addresses, or host sockets. While some
  applications require these communications, unrestricted access can serve as an escalation
  entry point for attackers to exploit internal services which are not managed by
  Kubernetes (e.'
---
Open the original post ↗ https://www.tigera.io/blog/how-to-get-started-with-calico-observability-features/
