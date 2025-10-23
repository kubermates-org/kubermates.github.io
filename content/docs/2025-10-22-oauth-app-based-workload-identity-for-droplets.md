---
title: OAuth App Based Workload Identity for Droplets
date: '2025-10-22T18:51:32.229000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/oauth-app-workload-identity-droplets
post_kind: link
draft: false
tldr: "OAuth App Based Workload Identity for Droplets What is workload identity federation?\
  \ Security properties Workload identity solution architecture Next steps About the\
  \ author Try DigitalOcean for free Related Articles How DigitalOcean Uses Semgrep\
  \ to Fortify Security: A Highlight From Our Toolset Contextual Vulnerability Management\
  \ With Security Risk As Debt Regresshion vulnerability: Recommended actions and\
  \ steps we've taken By John Andersen Senior Product Security Engineer Published:\
  \ October 22, 2025 8 min read This post is the first entry in a three part series\
  \ on workload identity federation : Part 1: Architecture (this post) Part 1: Architecture\
  \ (this post) Part 2: Deployment and Configuration Part 2: Deployment and Configuration\
  \ Part 3: Usage from Droplets and GitHub Actions Part 3: Usage from Droplets and\
  \ GitHub Actions This entry will cover what workload identity federation is and\
  \ how it can be implemented leveraging DigitalOceanâ\x80\x99s OAuth API. In the\
  \ following entries in this series, weâ\x80\x99ll deploy an open source Proof of\
  \ Concept (PoC) , configure roles and policies for workload identity access control,\
  \ spin up a Droplet, write a GitHub Actions workflow, and access databases and Spaces\
  \ keys from them using their respective workload identity tokens."
summary: "OAuth App Based Workload Identity for Droplets What is workload identity\
  \ federation? Security properties Workload identity solution architecture Next steps\
  \ About the author Try DigitalOcean for free Related Articles How DigitalOcean Uses\
  \ Semgrep to Fortify Security: A Highlight From Our Toolset Contextual Vulnerability\
  \ Management With Security Risk As Debt Regresshion vulnerability: Recommended actions\
  \ and steps we've taken By John Andersen Senior Product Security Engineer Published:\
  \ October 22, 2025 8 min read This post is the first entry in a three part series\
  \ on workload identity federation : Part 1: Architecture (this post) Part 1: Architecture\
  \ (this post) Part 2: Deployment and Configuration Part 2: Deployment and Configuration\
  \ Part 3: Usage from Droplets and GitHub Actions Part 3: Usage from Droplets and\
  \ GitHub Actions This entry will cover what workload identity federation is and\
  \ how it can be implemented leveraging DigitalOceanâ\x80\x99s OAuth API. In the\
  \ following entries in this series, weâ\x80\x99ll deploy an open source Proof of\
  \ Concept (PoC) , configure roles and policies for workload identity access control,\
  \ spin up a Droplet, write a GitHub Actions workflow, and access databases and Spaces\
  \ keys from them using their respective workload identity tokens. Workload identity\
  \ is used to reduce the amount of secrets involved in deploying and administrating\
  \ software systems. Instead of authentication being done based on something a workload\
  \ knows, for example passwords or API tokens, authentication is done based on what\
  \ the workload is. The heart of workload identity federation is asymmetric cryptography.\
  \ By leveraging public / private key pairs, tokens can be issued to workloads, such\
  \ as Droplets, and used for authentication and authorization to APIs exposed by\
  \ resource servers. Workload identity tokens are exchanged for domain specific access\
  \ tokens, or grant access to resources directly. This series showcases how we can\
  \ use DigitalOceanâ\x80\x99s OAuth API and fine grained permission scopes to implement\
  \ and leverage workload identity federation using OpenID Connect (OIDC) protocol\
  \ tokens. Weâ\x80\x99ll enable secretless access to DigitalOcean hosted databases\
  \ and Spaces buckets from Droplets and GitHub Actions workflows. Eliminating the\
  \ need to provision static, long-lived credentials for databases and Spaces buckets\
  \ for those environments. Authentication based on what the workload is requires\
  \ that the infrastructure orchestrating the workload be able to make verifiable\
  \ claims about a workloadâ\x80\x99s properties. To do this, the infrastructure responsible\
  \ for running the workload enables issuance of workload-specific tokens containing\
  \ these claims."
---
Open the original post ↗ https://www.digitalocean.com/blog/oauth-app-workload-identity-droplets
