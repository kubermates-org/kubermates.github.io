---
title: 'Upgrading VMware Cloud Foundation 5.2 to 9.0: The Top 10 Questions Answered'
date: '2025-12-18T15:34:01+00:00'
tags:
- vmware
- cloud-foundation
- kubernetes
source: VMware Cloud Foundation Blog
external_url: https://blogs.vmware.com/cloud-foundation/2025/12/18/upgrading-vmware-cloud-foundation-5-2-to-9-0-the-top-10-questions-answered/
post_kind: link
draft: false
tldr: 'Question 1: How does VMware SDDC Manager handle upgrades? Are there major changes
  with upgrades in version 9.0? Question 2: Are there considerations for VMware vSAN
  Original Storage Architecture (OSA) clusters during the upgrade? Question 3: How
  is the VMware NSX upgrade performed? Question 4: If I have VMware Aria Suite deployed
  in VCF aware mode in version 5.2, do I need to decouple Aria Suite from the deployment
  before upgrading? Question 5: Is it possible to upgrade from VCF 5.2 without LCM
  and Aria Suite configured? Question 6: How many hosts are allowed in a consolidated
  design in VCF 9.0? Question 7: How can I transition from VMware Identity Manager
  (vIDM) to VCF Identity Broker (VIDB) in VCF 9? Question 8: For VCF Operations do
  we need to download the binaries and where should they be placed? Question 9: Is
  there a regression / rollback pathway if I have an error in my upgrade? Question
  10: Is there any path for VMware Cloud Director (VCD) to VCF Automation Migrations?
  On-Demand Replay Need Help? Discover more from VMware Cloud Foundation (VCF) Blog
  Related Articles Upgrading VMware Cloud Foundation 5.2 to 9.0: The Top 10 Questions
  Answered Upgrading VMware Cloud Foundation 5.2 to 9.0: Webinar Takeaways Set Your
  Implementation Up for Success with VCF Jumpstart Workshop VMware Cloud Foundation
  (VCF) 9.0 provides a quick and easy way to deploy a private cloud. While the upgrade
  from VCF 5.'
summary: 'Question 1: How does VMware SDDC Manager handle upgrades? Are there major
  changes with upgrades in version 9.0? Question 2: Are there considerations for VMware
  vSAN Original Storage Architecture (OSA) clusters during the upgrade? Question 3:
  How is the VMware NSX upgrade performed? Question 4: If I have VMware Aria Suite
  deployed in VCF aware mode in version 5.2, do I need to decouple Aria Suite from
  the deployment before upgrading? Question 5: Is it possible to upgrade from VCF
  5.2 without LCM and Aria Suite configured? Question 6: How many hosts are allowed
  in a consolidated design in VCF 9.0? Question 7: How can I transition from VMware
  Identity Manager (vIDM) to VCF Identity Broker (VIDB) in VCF 9? Question 8: For
  VCF Operations do we need to download the binaries and where should they be placed?
  Question 9: Is there a regression / rollback pathway if I have an error in my upgrade?
  Question 10: Is there any path for VMware Cloud Director (VCD) to VCF Automation
  Migrations? On-Demand Replay Need Help? Discover more from VMware Cloud Foundation
  (VCF) Blog Related Articles Upgrading VMware Cloud Foundation 5.2 to 9.0: The Top
  10 Questions Answered Upgrading VMware Cloud Foundation 5.2 to 9.0: Webinar Takeaways
  Set Your Implementation Up for Success with VCF Jumpstart Workshop VMware Cloud
  Foundation (VCF) 9.0 provides a quick and easy way to deploy a private cloud. While
  the upgrade from VCF 5. x is designed to be streamlined, it introduces mandatory
  changes in management methodologies and requires careful, phased execution. I recently
  presented a packed webinar with Brent Douglas, diving deep into the VCF 5.2 to VCF
  9.0 upgrade process. With hundreds of attendees and a flood of questions, it’s clear
  this transition is top-of-mind for many of you. I’ve sifted through the noise, merging
  similar inquiries into single, comprehensive challenges. Below are the Top 10 “must-know”
  questions submitted by the audience, complete with the detailed answers you need
  to navigate your VCF 9.0 journey with confidence. There were several questions around
  SDDC Manager and upgrades. There are no major changes to the way upgrades are performed.
  If you are familiar with VCF 5.2 the asynchronous patching functionality is built
  into the console in the same way in the 9.0 release. This lets you schedule upgrades/patches
  as needed. The big difference is that the SDDC Manager interface has been incorporated
  into the VCF Operations console located under the fleet management section.'
---
Open the original post ↗ https://blogs.vmware.com/cloud-foundation/2025/12/18/upgrading-vmware-cloud-foundation-5-2-to-9-0-the-top-10-questions-answered/
