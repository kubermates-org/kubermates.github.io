---
title: 'From Incident Counting to SLIs: How DigitalOcean Rethought Availability'
date: '2026-04-23T09:15:00.007000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/sli-based-availability-framework
post_kind: link
draft: false
tldr: 'From Incident Counting to SLIs: How DigitalOcean Rethought Availability The
  Old Methodology Splitting Our Measurement: Control Plane vs Data Plane Control Plane
  Data Plane Magnitude matters From Raw Metrics to Recording Rules Product Journeys
  Multi Window Multi Burn Rate Alerts Error Budgets as Engineering Policy Tracking
  Policy From Core to Inference Cloud About the author Start building today Related
  Articles Beyond the Abyss Project Poseidon’s Quest for Zero-Downtime Reliability
  The LLM Inference Trilemma: Throughput, Latency, Cost Mastering the 600B+ Frontier:
  Optimizing Large Model Deployments on the Inference Cloud By Miguel Carrera Published:
  April 23, 2026 11 min read Our journey to truly understand our customer experience
  began with a hard look at our internal availability numbers at the start of 2025.
  We saw something uncomfortable: the numbers didn’t match our customers’ reality.'
summary: 'From Incident Counting to SLIs: How DigitalOcean Rethought Availability
  The Old Methodology Splitting Our Measurement: Control Plane vs Data Plane Control
  Plane Data Plane Magnitude matters From Raw Metrics to Recording Rules Product Journeys
  Multi Window Multi Burn Rate Alerts Error Budgets as Engineering Policy Tracking
  Policy From Core to Inference Cloud About the author Start building today Related
  Articles Beyond the Abyss Project Poseidon’s Quest for Zero-Downtime Reliability
  The LLM Inference Trilemma: Throughput, Latency, Cost Mastering the 600B+ Frontier:
  Optimizing Large Model Deployments on the Inference Cloud By Miguel Carrera Published:
  April 23, 2026 11 min read Our journey to truly understand our customer experience
  began with a hard look at our internal availability numbers at the start of 2025.
  We saw something uncomfortable: the numbers didn’t match our customers’ reality.
  Our monthly availability oscillated between 99.5% and 99.9%. Those peaks and valleys
  depended more on whether we declared a high-severity incident that month than on
  how the platform was actually performing. Customers were still experiencing issues
  and opening escalations, but the metric didn’t reflect customer availability. The
  previous internal measurement served us well in our early days, but its limitations
  became evident as DigitalOcean expanded. Our incident-based approach treated any
  declared incident as a total outage and anything below the severity threshold as
  invisible. This created a structural trap: we couldn’t expand coverage to include
  lower-severity issues without artificially destroying our availability number, because
  the formula would count every minute of a partial degradation as a full platform
  outage. The chart above shows monthly platform availability using both methodologies
  over the same time period. The incident-based (old) swings between roughly 99.5%
  and 99.9% month to month. The SLI-based metric (new) holds consistently at 99.95%
  or above. The old metric was measuring noise, while the new metric measures actual
  availability signals.'
---
Open the original post ↗ https://www.digitalocean.com/blog/sli-based-availability-framework
