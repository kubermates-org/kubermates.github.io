---
title: Auditing user activity in pods and nodes with the Security-Profiles-Operator
date: '2025-10-07T15:29:47+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/07/auditing-user-activity-in-pods-and-nodes-with-the-security-profiles-operator/
post_kind: link
draft: false
tldr: How the audit logging feature in SPO works How to enable it Considerations while
  using privileged containers Performance considerations Conclusion Posted on October
  7, 2025 by Neeraj Krishna Gopalakrishna & Red Hat OpenShift Node Team CNCF projects
  highlighted in this post Kubernetes’ native audit logs are essential for tracking
  control plane activities, but they fail to capture what happens inside a container
  or on the host node itself during kubectl debugging sessions. This creates a security
  and compliance gap, as malicious or unauthorized actions within a pod or on the
  node go unrecorded.
summary: 'How the audit logging feature in SPO works How to enable it Considerations
  while using privileged containers Performance considerations Conclusion Posted on
  October 7, 2025 by Neeraj Krishna Gopalakrishna & Red Hat OpenShift Node Team CNCF
  projects highlighted in this post Kubernetes’ native audit logs are essential for
  tracking control plane activities, but they fail to capture what happens inside
  a container or on the host node itself during kubectl debugging sessions. This creates
  a security and compliance gap, as malicious or unauthorized actions within a pod
  or on the node go unrecorded. Without this visibility, it’s impossible to fully
  understand user actions, conduct an incident investigation, or meet regulatory compliance
  requirements. The newly added audit logging feature in Security-Profiles-Operator
  (SPO) addresses this by enabling detailed, server-side logging of user activity
  at the node level. Let’s imagine a scenario: A team of engineers is responsible
  for maintaining an application that processes financial transactions. The application
  is deployed on Kubernetes, with various containers (in pods) running different workloads.
  When a customer reports a bug, an engineer is granted access to the pod via kubectl
  exec to debug the issue (also kubectl debug node). However, during the session,
  they accidentally delete/modify a crucial configuration file. The application fails,
  leading to financial losses and business disruption. During a post-incident audit,
  the security team can see from the Kubernetes control plane logs that the engineer
  initiated a kubectl exec session. But the logs don’t reveal what commands were run
  inside the container. It’s an operational black box.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/07/auditing-user-activity-in-pods-and-nodes-with-the-security-profiles-operator/
