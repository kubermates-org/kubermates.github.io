---
title: 'Blog: Continuous microservices with databases in Jenkins X'
date: '2021-06-25T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/06/25/jx-cd-databases-2021/
post_kind: link
draft: false
tldr: A common question we get asked on the Jenkins X project is how to get started
  creating microservices that use databases with automated CI/CD with GitOps Promotion
  and Preview Environments. To make things a little easier to get started we’ve created
  a new node-postgresql quickstart.
summary: 'A common question we get asked on the Jenkins X project is how to get started
  creating microservices that use databases with automated CI/CD with GitOps Promotion
  and Preview Environments. To make things a little easier to get started we’ve created
  a new node-postgresql quickstart. If you are using the cloud then we prefer cloud
  over kubernetes for things like databases, storage, ingress and secret managers
  so please try use your clouds managed databases if you can. So ideally you’d set
  up your database via your infrastructure as code solution, such as terraform , and
  then associate your kubernetes Service Account to a cloud IAM role to access the
  database. However to provide something simple that just works in any kubernetes
  cluster this quickstart uses the postgres-operator to manage setting up each database
  cluster in each environment. So to be able to use this quickstart you will need
  to install this operator into your cluster. You can add charts to your cluster via
  the CLI. From inside a git clone of your cluster git repository run the following
  command: This will modify the helmfile. yaml to point at a new helmfiles/postgres/helmfile.
  yaml file to deploy the postgres-operator chart. Then git commit and push that change
  to your cluster. You can watch it run via jx admin log -w.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/06/25/jx-cd-databases-2021/
