---
title: Switching to eBPF One Step at a Time with Calico DNS Inline Policy
date: '2025-06-25T16:05:49+00:00'
tags:
- tigera
source: Tigera
external_url: https://www.tigera.io/blog/switching-to-ebpf-one-step-at-a-time-with-calico-dns-inline-policy/
post_kind: link
draft: false
tldr: Calico Enterprise lets users write network policies using domain names instead
  of IP addresses. This is done by dynamically mapping domain names to IP addresses
  and matching the egress traffic against these IPs.
summary: 'Calico Enterprise lets users write network policies using domain names instead
  of IP addresses. This is done by dynamically mapping domain names to IP addresses
  and matching the egress traffic against these IPs. We have discussed this feature
  in detail when we introduced the Inline mode for the eBPF data plane in Calico Enterprise
  3. 20 release! It addresses the latency and performance issues of the various modes
  used by Calico in iptables/nftables data planes. It is a shame that Calico users
  who are not yet ready to switch completely to eBPF would miss out on this big DNS
  policy improvement. Don’t worry! We found a way to port it to iptables to enhance
  our users’ experience without forcing users to make a huge leap. In Calico Enterprise
  v3. 21, we have extended the Inline DNS policy mode to iptables. In this mode, DNS
  policies are updated in real time as DNS responses are parsed by eBPF within the
  data plane, thus improving the performance. In all the existing modes in the iptables
  data plane, the DNS response packets are sent to Felix – Calico’s userspace agent.
  It parses the packets and updates the data plane since advanced packet parsing is
  not feasible with standard iptables rules. However, iptables has an xt_bpf extension
  which lets us process and match the packets by an eBPF program the same way we do
  that in the eBPF data plane! An iptables rule that allows it may look something
  like this: The iptables rule calls the eBPF DNS parser program on the response packet
  and updates the data plane inline.'
---
Open the original post ↗ https://www.tigera.io/blog/switching-to-ebpf-one-step-at-a-time-with-calico-dns-inline-policy/
