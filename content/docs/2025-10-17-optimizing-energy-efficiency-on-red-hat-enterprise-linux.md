---
title: Optimizing energy efficiency on Red Hat Enterprise Linux
date: '2025-10-17T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/energy-efficient-computing-server-platforms-red-hat-enterprise-linux
post_kind: link
draft: false
tldr: Optimizing energy efficiency on Red Hat Enterprise Linux Testing methodology
  Measuring network throughput Measuring CPU utilization Computational efficiency
  Network-intensive process operating regimes Single process Multi-process Saturated
  Optimizing workloads for hardware locality NUMA-aware resource allocation for network-intensive
  processes Pinning interrupts and processes Hardware environment in the test Evaluating
  computer system power consumption External power meter System utility Platform management
  Normalizing performance against power consumption A note about power supplies Mitigation
  strategies Use lower-rated power supplies Enable hot standby mode Measure DC output
  directly Benefits of considering PSU efficiency Conclusion Red Hat Ansible Automation
  Platform | Product Trial About the authors Adam Okuliar Otto Šabart More like this
  Blog post Blog post Original podcast Original podcast Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share The energy efficiency of data centers and high-performance
  systems is becoming increasingly important. Energy costs can make up a substantial
  portion of the operating expenditure (OPEX) budget, potentially serving as a critical
  factor in the success or failure of a business.
summary: 'Optimizing energy efficiency on Red Hat Enterprise Linux Testing methodology
  Measuring network throughput Measuring CPU utilization Computational efficiency
  Network-intensive process operating regimes Single process Multi-process Saturated
  Optimizing workloads for hardware locality NUMA-aware resource allocation for network-intensive
  processes Pinning interrupts and processes Hardware environment in the test Evaluating
  computer system power consumption External power meter System utility Platform management
  Normalizing performance against power consumption A note about power supplies Mitigation
  strategies Use lower-rated power supplies Enable hot standby mode Measure DC output
  directly Benefits of considering PSU efficiency Conclusion Red Hat Ansible Automation
  Platform | Product Trial About the authors Adam Okuliar Otto Šabart More like this
  Blog post Blog post Original podcast Original podcast Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share The energy efficiency of data centers and high-performance
  systems is becoming increasingly important. Energy costs can make up a substantial
  portion of the operating expenditure (OPEX) budget, potentially serving as a critical
  factor in the success or failure of a business. This article breaks down the issue
  of energy efficiency in modern server platforms, presenting tools and an example
  methodology for measuring power consumption and performance. As a case study, we
  present measurement results from two server platforms with different CPU architectures.
  We will emphasize network performance (including throughput measurements), CPU utilization,
  and power consumption, with a particular emphasis on achieving the highest possible
  throughput per watt of energy consumed. Evaluating the relationship between a computer’s
  performance and its power requirements can be broken down into three key steps:
  Assess the computer’s performance Measure the computer’s power requirements Normalize
  performance relative to power consumption We measure system performance in terms
  of gigabits per second of achievable throughput per physical CPU core. It is important
  to note that with modern, high-speed (100 Gbps and above) Ethernet adapters, it''s
  virtually impossible for a single user-space process to utilize all available bandwidth.
  Moreover, network throughput is only part of the performance story. Handling network
  traffic ideally consumes minimal resources, leaving the majority of the system available
  for creating or processing the data transmitted over the network. Ideally, the CPU
  is saturated with as few cores as possible. To quantify these requirements, we monitor
  the following metrics: Maximum achievable throughput in gigabits per second. Total
  CPU utilization, measured in cores.'
---
Open the original post ↗ https://www.redhat.com/en/blog/energy-efficient-computing-server-platforms-red-hat-enterprise-linux
