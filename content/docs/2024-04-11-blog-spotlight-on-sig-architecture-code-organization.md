---
title: 'Blog: Spotlight on SIG Architecture: Code Organization'
date: '2024-04-11T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2024/04/11/sig-architecture-code-spotlight-2024/
post_kind: link
draft: false
tldr: 'This is the third interview of a SIG Architecture Spotlight series that will
  cover the different subprojects. We will cover SIG Architecture: Code Organization.'
summary: 'This is the third interview of a SIG Architecture Spotlight series that
  will cover the different subprojects. We will cover SIG Architecture: Code Organization.
  In this SIG Architecture spotlight I talked with Madhav Jivrajani (VMware), a member
  of the Code Organization subproject. Frederico (FSM) : Hello Madhav, thank you for
  your availability. Could you start by telling us a bit about yourself, your role
  and how you got involved in Kubernetes? Madhav Jivrajani (MJ) : Hello! My name is
  Madhav Jivrajani, I serve as a technical lead for SIG Contributor Experience and
  a GitHub Admin for the Kubernetes project. Apart from that I also contribute to
  SIG API Machinery and SIG Etcd, but more recently, I’ve been helping out with the
  work that is needed to help Kubernetes stay on supported versions of Go , and it
  is through this that I am involved with the Code Organization subproject of SIG
  Architecture. FSM : A project the size of Kubernetes must have unique challenges
  in terms of code organization – is this a fair assumption? If so, what would you
  pick as some of the main challenges that are specific to Kubernetes? MJ : That’s
  a fair assumption! The first interesting challenge comes from the sheer size of
  the Kubernetes codebase. We have ≅2. 2 million lines of Go code (which is steadily
  decreasing thanks to dims and other folks in this sub-project!), and a little over
  240 dependencies that we rely on either directly or indirectly, which is why having
  a sub-project dedicated to helping out with dependency management is crucial: we
  need to know what dependencies we’re pulling in, what versions these dependencies
  are at, and tooling to help make sure we are managing these dependencies across
  different parts of the codebase in a consistent manner. Another interesting challenge
  with Kubernetes is that we publish a lot of Go modules as part of the Kubernetes
  release cycles, one example of this is client-go. However, we as a project would
  also like the benefits of having everything in one repository to get the advantages
  of using a monorepo, like atomic commits… so, because of this, code organization
  works with other SIGs (like SIG Release) to automate the process of publishing code
  from the monorepo to downstream individual repositories which are much easier to
  consume, and this way you won’t have to import the entire Kubernetes codebase! FSM
  : For someone just starting contributing to Kubernetes code-wise, what are the main
  things they should consider in terms of code organization? How would you sum up
  the key concepts? MJ : I think one of the key things to keep in mind at least as
  you’re starting off is the concept of staging directories. In the kubernetes/kubernetes
  repository, you will come across a directory called staging/.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2024/04/11/sig-architecture-code-spotlight-2024/
