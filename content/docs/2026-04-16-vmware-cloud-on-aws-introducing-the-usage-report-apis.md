---
title: 'VMware Cloud on AWS: Introducing the Usage Report APIs'
date: '2026-04-16T17:34:26+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2026/04/16/vmware-cloud-aws-usage-report-apis/
post_kind: link
draft: false
tldr: What’s Available 1. Host Usage Report API 2.
summary: 'What’s Available 1. Host Usage Report API 2. SPLA Usage Report API 3. Miscellaneous
  Usage Report API (Non-Host Networking Charges) Key Capabilities Use Cases HTML Usage
  Report Generator Getting Started What’s Next Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles VMware Cloud on AWS: Introducing the Usage Report APIs
  Converging VMware vSphere to VMware Cloud Foundation 9.0: The Top 10 Questions Answered
  The Unification Dividend: Consolidating Database Operations on VMware Cloud Foundation
  Tracking VMware Cloud on AWS consumption across hosts, SPLA, and non-host charges
  today requires manual data pulls and waiting for invoice every quarter. Customers
  building FinOps practices and mature cloud financial operations have consistently
  asked for programmatic access to this data, in a format their existing tools can
  consume. Today, we’re delivering on that with three new Usage Report APIs for Host
  Usage, Microsoft SPLA Usage, and Miscellaneous Usage (non-host charges) covering
  networking charges like EIP, TGW, data transfer, and Direct Connect. These Usage
  Report APIs provide daily-granularity usage data through clean, filterable endpoints
  that integrate directly into your existing cost management, BI, and reporting workflows.
  Whether you’re tracking costs, analyzing consumption patterns, or building custom
  dashboards, these APIs give you the flexibility to retrieve and organize usage data
  on your terms. All three APIs are available now to all VMware Cloud on AWS customers.
  GET /activityanalytic/{org_id}/hosts/{freq}/usage-report GET /activityanalytic/{org_id}/hosts/{freq}/usage-report
  Retrieve daily host consumption data for any date range, broken down by instance
  type and region group. Each record includes the SKU, region, instance type, subscription
  count, actual host usage count, and overage. This gives you the data needed for
  forecasting invoices, understanding usage spikes, financial planning, chargeback,
  and subscription right-sizing.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2026/04/16/vmware-cloud-aws-usage-report-apis/
