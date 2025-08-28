---
title: Announcing enhancements to per-bucket access keys and public preview of Spaces
  access logs
date: '2025-04-08T17:40:20.228000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/spaces-api-access-logs
post_kind: link
draft: false
tldr: "By Anantha Ramachandran and Keshav Attrey At DigitalOcean, we continuously\
  \ enhance our cloud storage solutions to empower developers and growing businesses.\
  \ Today, weâ\x80\x99re excited to announce the general availability of DO API support\
  \ for per-bucket access keys, mixed permissions support for per-bucket access keys,\
  \ and the public preview of Spaces access logs, delivering greater automation, visibility,\
  \ and security to DigitalOcean Spaces object storage."
summary: "By Anantha Ramachandran and Keshav Attrey At DigitalOcean, we continuously\
  \ enhance our cloud storage solutions to empower developers and growing businesses.\
  \ Today, weâ\x80\x99re excited to announce the general availability of DO API support\
  \ for per-bucket access keys, mixed permissions support for per-bucket access keys,\
  \ and the public preview of Spaces access logs, delivering greater automation, visibility,\
  \ and security to DigitalOcean Spaces object storage. Building on the success of\
  \ per-bucket access keys, weâ\x80\x99re introducing two major upgrades that are\
  \ now generally available to all customers to streamline storage access management:\
  \ DO API support for managing access keys â\x80\x93 Manage Spaces access keys programmatically\
  \ using the DigitalOcean API, enabling automation through the DigitalOcean Terraform\
  \ Provider, doctl CLI, DigitalOcean Go API Client (godo), and DigitalOceanâ\x80\x99\
  s Python library (PyDo). More granular access control â\x80\x93 A single access\
  \ key can now be configured with permissions that vary by bucket. This lets you\
  \ grant read-only permissions for some buckets and read-write permissions for other\
  \ buckets to a single person or application. These enhancements simplify storage\
  \ management for customers handling large-scale deployments, automated backups,\
  \ and security-driven workflows. Explore the documentation to use DO API and manage\
  \ mixed-permissions access keys. You can start using these new features right now.\
  \ Spaces access logs are now available in public preview to provide detailed records\
  \ of read and write requests to your Spaces buckets, helping you to better understand\
  \ usage and enhance security. Access logging â\x80\x93 Generate detailed records\
  \ of reads, writes, and deletions of objects in your Spaces buckets, whether using\
  \ Spaces origin endpoints or Spaces CDN endpoints. Detailed metadata â\x80\x93 Capture\
  \ object paths, client IPs, and more. S3-compatible â\x80\x93 Logs are compatible\
  \ with Amazon S3 server access log format, and logging is enabled using the S3-compatible\
  \ PutBucketLogging API."
---
Open the original post ↗ https://www.digitalocean.com/blog/spaces-api-access-logs
