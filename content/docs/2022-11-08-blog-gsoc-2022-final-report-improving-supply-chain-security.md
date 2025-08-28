---
title: 'Blog: GSoC 2022 Final Report: Improving Supply Chain Security'
date: '2022-11-08T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2022/11/08/gsoc-2022/
post_kind: link
draft: false
tldr: 'GSoC 2022 Final Report: Improving Supply Chain Security Project Description
  Work Done Enhancing the jx version output Integrating with Tekton Chains to sign
  TaskRuns and PipelineRuns Software Bill of Materials (SBOM) Signing Jenkins X artifacts
  What’s next? Acknowledgements Supply chain security is a rising concern in the current
  software era. Securing the software supply chain encompasses vulnerability remediation
  and the implementation of controls throughout the software development process.'
summary: 'GSoC 2022 Final Report: Improving Supply Chain Security Project Description
  Work Done Enhancing the jx version output Integrating with Tekton Chains to sign
  TaskRuns and PipelineRuns Software Bill of Materials (SBOM) Signing Jenkins X artifacts
  What’s next? Acknowledgements Supply chain security is a rising concern in the current
  software era. Securing the software supply chain encompasses vulnerability remediation
  and the implementation of controls throughout the software development process.
  Due to massive increase in attacks on software supply chain and the diversity of
  its types , Jenkins X has to make efforts to ensure that the build process is secure.
  As part of securing Jenkins X installation by default I worked on both securing
  our own components and enabling our users to use these features in their build and
  release steps. The work done so far covers these four sections. Enhancing the jx
  version output jx version Integrating with Tekton Chains to sign TaskRuns and PipelineRuns
  Software Bill of Materials (SBOM) Signing Jenkins X artifacts jx version Description:
  A first step towards securing Jenkins X supply chain is to increase the amount of
  information gained from running jx version command. jx version Implementation The
  issue created for this task is here. The PR to fix it is here. Description: As Jenkins
  X uses tekton as its pipeline execution engine, TaskRun and PipelineRun are considered
  the key components of Jenkins X pipeline activities and steps Tekton Chains monitors
  the execution of all TaskRun and PipelineRun inside the cluster and takes a snapshot
  upon completion of each of them to sign with user-provided cryptographic keys and
  store them on the backend storage. The payload and signature cn be verified later
  using cosign verify-blob. TaskRun PipelineRun activities steps TaskRun PipelineRun
  cosign verify-blob Implementation I used the helm chart developed by Chainguard
  for integrating Chains with Jenkins X. To integrate the chart and added support
  for it on jx3-versions to make installation of helm chart easy for our users.'
---
Open the original post ↗ https://jenkins-x.io/blog/2022/11/08/gsoc-2022/
