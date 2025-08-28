---
title: 'Blog: Blixt - A load-balancer written in Rust, using eBPF, born from Gateway
  API'
date: '2024-01-08T00:00:00+00:00'
tags:
- kubernetes
- community
source: Kubernetes.dev Blog
external_url: https://www.kubernetes.dev/blog/2024/01/08/blixt-load-balancer-rust-ebpf-gateway-api/
post_kind: link
draft: false
tldr: Blixt - A load-balancer written in Rust, using eBPF, born from Gateway API History
  Goals Getting involved In SIG Network we now have a layer 4 (“L4”) load balancer
  named Blixt. This project started as a fun experiment using emerging technologies
  and is intended to become a utility for CI and testing to help facilitate the continued
  development of Gateway API.
summary: 'Blixt - A load-balancer written in Rust, using eBPF, born from Gateway API
  History Goals Getting involved In SIG Network we now have a layer 4 (“L4”) load
  balancer named Blixt. This project started as a fun experiment using emerging technologies
  and is intended to become a utility for CI and testing to help facilitate the continued
  development of Gateway API. Are you interested in developing networking tools in
  Rust and eBPF ? Or perhaps you’re specifically interested in Gateway API? We’ll
  tell you a bit about the project and how it might benefit you. Blixt originated
  at Kong as an experiment to test load-balancing ingress traffic for Kubernetes clusters
  using eBPF for the dataplane. Around the time of Kubecon Detroit (2022) we (the
  Gateway API maintainers) realized it had significant potential to help us move our
  TCPRoute and UDPRoute support forward, which had been sort of “stuck in alpha” at
  the time due to a lack of conformance tests being developed for them. At the same
  time, various others in the SIG Network community developed an interest in the project
  due to the rapid growth of eBPFs use on Kubernetes. Given the potential for benefit
  to the Kubernetes ecosystem and the growing interest, Kong decided it would be helpful
  to donate the project to Kubernetes SIGs to benefit upstream Kubernetes. Over several
  months we rewrote the project in Rust (from C), due to a strong contingency of Rust
  knowledge (and interest) between us developing the project and an active interest
  in the burgeoning Aya project (a Rust framework for developing eBPF programs). We
  did eventually move the control plane (specifically) to Golang however, so that
  we could take advantage of the Kubebuilder and controller-runtime ecosystems. Additionally,
  we augmented our custom program loader (in eBPF, you generally write loaders that
  load your BPF byte code into the kernel) with bpfman : a project adjacent to us
  in the Rust + eBPF ecosystem, which helps solve several security and ergonomic problems
  with managing BPF programs on Linux systems. After the recently completed license
  review process , which provided a blanket exception for the use of dual licensed
  eBPF in CNCF code, the project became officially part of Kubernetes and interest
  has been growing. We have several goals for the project which revolve around the
  continued development of Gateway API, with a specific focus on helping mature Layer
  4 support (e.'
---
Open the original post ↗ https://www.kubernetes.dev/blog/2024/01/08/blixt-load-balancer-rust-ebpf-gateway-api/
