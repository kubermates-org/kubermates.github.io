---
title: 'Tomcat in the Crosshairs: New Research Reveals Ongoing Attacks'
date: '2025-04-02T12:00:49+00:00'
tags:
- security
source: Aqua Security
external_url: https://blog.aquasec.com/new-campaign-against-apache-tomcat
post_kind: link
draft: false
tldr: 'Tomcat in the Crosshairs: New Research Reveals Ongoing Attacks Tomcat Campaign
  25′: Attack Flow Detecting This Malware and Protecting your Environments Mitigation
  of Tomcat environments Indications of Compromise (IOCs) News headlines reported
  that it took just 30 hours for attackers to exploit a newly discovered vulnerability
  in Apache Tomcat servers. But what does this mean for workloads relying on Tomcat?
  Aqua Nautilus researchers discovered a new attack campaign targeting Apache Tomcat.'
summary: 'Tomcat in the Crosshairs: New Research Reveals Ongoing Attacks Tomcat Campaign
  25′: Attack Flow Detecting This Malware and Protecting your Environments Mitigation
  of Tomcat environments Indications of Compromise (IOCs) News headlines reported
  that it took just 30 hours for attackers to exploit a newly discovered vulnerability
  in Apache Tomcat servers. But what does this mean for workloads relying on Tomcat?
  Aqua Nautilus researchers discovered a new attack campaign targeting Apache Tomcat.
  In this blog, we shed light on newly discovered malware that targets Tomcat servers
  to hijack resources. After gaining initial access, the attackers uploads encrypted
  and encoded payloads that establish backdoors and persistence mechanisms. They then
  deploy two binaries disguised as kernel processes to exploit the server. The attack
  infrastructure appears to be relatively new, and code snippets suggest possible
  links to a Chinese-speaking threat actor. In this blog, we break down how the attack
  works—and how to stop it. The campaign targets Apache Tomcat servers and deploys
  encrypted payloads designed to run on both Windows and Linux systems. Once executed,
  the attack disguises itself, steals SSH credentials to spread laterally, and ultimately
  hijacks resources for cryptocurrency mining. It all starts with a brute-force attempt
  from a remote server using a Python script, which tests commonly used usernames
  and weak passwords on the Tomcat management console (e. g. , username “Tomcat” and
  password “123456”).'
---
Open the original post ↗ https://blog.aquasec.com/new-campaign-against-apache-tomcat
