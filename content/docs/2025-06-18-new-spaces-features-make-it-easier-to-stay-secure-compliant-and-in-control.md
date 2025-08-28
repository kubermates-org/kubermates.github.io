---
title: New Spaces features make it easier to stay secure, compliant, and in control
date: '2025-06-18T19:05:05.088000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/spaces-storage-accesslogs-connectionwizard
post_kind: link
draft: false
tldr: "By Anantha Ramachandran and Keshav Attrey As teams grow and their cloud storage\
  \ needs scale, seemingly small issues can snowball into bigger problems. Weâ\x80\
  \x99ve seen common pain points emerge, like struggling to track who accessed files\
  \ through CDN endpoints, or wrestling with tricky configurations when using third-party\
  \ tools like the AWS CLI or s3cmd, plus missed audit trails, prolonged troubleshooting,\
  \ or accidental misconfigurations that can lead to data loss."
summary: "By Anantha Ramachandran and Keshav Attrey As teams grow and their cloud\
  \ storage needs scale, seemingly small issues can snowball into bigger problems.\
  \ Weâ\x80\x99ve seen common pain points emerge, like struggling to track who accessed\
  \ files through CDN endpoints, or wrestling with tricky configurations when using\
  \ third-party tools like the AWS CLI or s3cmd, plus missed audit trails, prolonged\
  \ troubleshooting, or accidental misconfigurations that can lead to data loss. Thatâ\x80\
  \x99s why weâ\x80\x99ve made two important updates to help simplify and strengthen\
  \ the way you manage object storage with DigitalOcean Spaces , our S3-compatible\
  \ object storage solution, built for simplicity, scalability, and affordability.\
  \ Whether youâ\x80\x99re serving up images on a website, storing large media files,\
  \ managing data backups, or powering developer workflows, Spaces helps you move\
  \ fast without managing infrastructure. These new featuresâ\x80\x94the general availability\
  \ of Spaces access logs and the introduction of the connection wizardâ\x80\x94are\
  \ designed to enhance your visibility, minimize risk, and empower you to work with\
  \ greater confidence. With access logs, you can get detailed, time-stamped records\
  \ of all file read and write requests, including traffic that flows through both\
  \ Spaces origin and CDN endpoints. Previously, there was no easy way to monitor\
  \ who was accessing your files over the CDN. That made it difficult to troubleshoot,\
  \ detect suspicious behavior, or meet compliance and audit requirements. Whatâ\x80\
  \x99s new Logs now capture both direct and CDN traffic, so you have a complete view\
  \ of object activity. Spaces Origin access logs are compatible with Amazon S3 Server\
  \ Access Logs format, while Spaces CDN access logs are compatible with Amazon CloudFront\
  \ log formats, making it easy to integrate with tools you already use. Logs are\
  \ stored in your existing Spaces buckets, so they fit directly within your existing\
  \ services and workflows. Benefits of using Spaces access logs If you serve public\
  \ files such as images, videos, downloadable content especially at scale or over\
  \ a CDN, Access Logs can help you: Monitor object storage usage trends Detect unusual\
  \ patterns or spikes Audit access to meet compliance needs Real-world use cases\
  \ include AdTech and media platforms with high public traffic that need to track\
  \ downloads and API activity across their CDN endpoints for better performance insights\
  \ and usage monitoring."
---
Open the original post ↗ https://www.digitalocean.com/blog/spaces-storage-accesslogs-connectionwizard
