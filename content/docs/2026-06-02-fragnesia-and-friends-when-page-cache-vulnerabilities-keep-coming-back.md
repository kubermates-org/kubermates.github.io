---
title: 'Fragnesia and friends: When page cache vulnerabilities keep coming back'
date: '2026-06-02T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/fragnesia-and-friends-when-page-cache-vulnerabilities-keep-coming-back
post_kind: link
draft: false
tldr: 'Fragnesia and friends: When page cache vulnerabilities keep coming back Different
  CVEs, same pattern The exploit evolves. The signals don''t Learn more Red Hat Product
  Security About the author Sean Rickerd More like this Why flexibility is non-negotiable
  in the Middle East’s AI transformation journey Beyond automation: Why the surge
  in AI-driven security vulnerabilities demands human technical advocacy Technically
  Speaking | Inside open source AI strategy Collaboration In Product Security | Compiler
  Keep exploring Browse by channel Automation Artificial intelligence Open hybrid
  cloud Security Edge computing Infrastructure Applications Virtualization Share A
  couple of weeks ago, I wrote about Copy-Fail (CVE-2026-31431) and how Red Hat OpenShift’s
  defense-in-depth approach prevented container escape despite a vulnerable kernel.'
summary: 'Fragnesia and friends: When page cache vulnerabilities keep coming back
  Different CVEs, same pattern The exploit evolves. The signals don''t Learn more
  Red Hat Product Security About the author Sean Rickerd More like this Why flexibility
  is non-negotiable in the Middle East’s AI transformation journey Beyond automation:
  Why the surge in AI-driven security vulnerabilities demands human technical advocacy
  Technically Speaking | Inside open source AI strategy Collaboration In Product Security
  | Compiler Keep exploring Browse by channel Automation Artificial intelligence Open
  hybrid cloud Security Edge computing Infrastructure Applications Virtualization
  Share A couple of weeks ago, I wrote about Copy-Fail (CVE-2026-31431) and how Red
  Hat OpenShift’s defense-in-depth approach prevented container escape despite a vulnerable
  kernel. I spent time actively trying to break out of an OpenShift container, achieved
  root inside the pod almost immediately, and still couldn’t escape to the host. The
  kernel vulnerability was real. The exploit path was real. The defenses still held.
  While I was wrapping up this article, another related variant, DirtyDecrypt (CVE-2026-31635),
  started circulating publicly alongside exploit discussion and proof-of-concept coverage.
  At that point, we were looking at 4 major Linux privilege escalation vulnerabilities
  in roughly 14 days, all abusing variations of the same broader pattern. That’s the
  part that matters most to me. At a certain point, you stop looking at these as isolated
  CVEs and start recognizing a systemic issue. Different subsystems. Different exploit
  paths.'
---
Open the original post ↗ https://www.redhat.com/en/blog/fragnesia-and-friends-when-page-cache-vulnerabilities-keep-coming-back
