---
title: 'SAS Viya Platform with Red Hat OpenShift – Part 2: Security and Storage Considerations'
date: '2026-03-24T00:00:00+00:00'
tags:
- openshift
source: OpenShift Blog
external_url: https://www.redhat.com/en/blog/sas-viya-on-red-hat-openshift-part-2-security-and-storage-considerations
post_kind: link
draft: false
tldr: 'SAS Viya Platform with Red Hat OpenShift – Part 2: Security and Storage Considerations
  Security Considerations OpenShift Machine Management 1. Workload Placement 2.'
summary: 'SAS Viya Platform with Red Hat OpenShift – Part 2: Security and Storage
  Considerations Security Considerations OpenShift Machine Management 1. Workload
  Placement 2. Autoscaling SAS Viya Storage Requirements Cloud Native Storage Integration
  Conclusion About the authors Patrick Farley Hans-Joachim Edert More like this Modernize
  virtual machines on Google Cloud with Red Hat OpenShift Virtualization From experiment
  to production: A reliable architecture for version-controlled MLOps Technically
  Speaking | Build a production-ready AI toolbox Technically Speaking | Platform engineering
  for AI agents Browse by channel Automation Artificial intelligence Open hybrid cloud
  Security Edge computing Infrastructure Applications Virtualization Share Welcome
  back to this 2nd part of our blog where we want to share some basic technical information
  about the SAS Viya platform on Red Hat OpenShift platform. While we have been discussing
  the reference architecture and details on the deployment process in the first part
  of the blog , we now want to dive deeper into security and storage topics, which
  are at the core of any deployment. As discussed in the first part of this blog ,
  the SAS Viya analytical platform is not just a single application, but a suite of
  integrated applications. While most services are microservices following the 12-factor-app
  pattern, SAS also uses compute engines and stateful services which are essential
  for the platform. SAS integrates with the standard security approach that applies
  to OpenShift, namely the use of Security Context Constraints (SCCs). Following Red
  Hat guidelines, most SAS Viya platform pods are deployed in the restricted SCC,
  which applies the highest level of security. However, there are a few exceptions:
  two other OpenShift predefined SCCs ( nonroot and hostmount-anyuid ) may be required
  for specific SAS services depending on use case. In addition, a few custom SCCs
  are either required by essential SAS Viya platform components, such as the CAS server,
  or associated with specific SAS offerings that might be included in your software
  order. restricted nonroot hostmount-anyuid All custom SCCs which might be applied
  to the SAS deployment are shipped as part of the SAS deployment assets collection
  of files and templates, so there is no need to create them manually. As OpenShift
  administrators often want to review the content of these SCCs, the following command
  might be helpful to quickly see which custom SCCs are available and where they can
  be found: # change to the top-level folder of the deployment # directory and list
  all available SCCs cd $deploy find.'
---
Open the original post ↗ https://www.redhat.com/en/blog/sas-viya-on-red-hat-openshift-part-2-security-and-storage-considerations
