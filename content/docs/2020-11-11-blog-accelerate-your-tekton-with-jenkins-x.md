---
title: 'Blog: Accelerate your Tekton with Jenkins X'
date: '2020-11-11T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2020/11/11/accelerate-tekton/
post_kind: link
draft: false
tldr: Accelerate your Tekton with Jenkins X Version 2. x Vision Version 3.
summary: Accelerate your Tekton with Jenkins X Version 2. x Vision Version 3. x Using
  Tekton in your repository Reusing Tekton Catalog Tasks Sharing steps between Tasks
  Custom Pipeline Catalogs Conclusion One of the goals of Jenkins X has always been
  to help accelerate and automate Continuous Delivery so that developers can focus
  on delivering value to their customers; either by creating that new microservice
  or adding features to an existing project and not writing and managing pipelines.
  Pipeline engines like Jenkins and Tekton are awesome - they can do anything! But
  they start as a blank sheet of paper where you have to fill in all the details of
  how to compile your code, test it, verify it, tag it, release, distribute and delivery
  it to production. Figuring all that stuff out can take a huge amount of time to
  create and maintain. This gets even more complex as we are all creating more and
  more microservices each with their own pipelines making more and more things to
  create and manage. We want to be able to reuse pipelines and tasks to get work done.
  But at the same time we want flexibility; not all applications are the same and
  sometimes things need to be changed on a per team or application basis. In Jenkins
  X 2. x we went with a jenkins-x. xml approach to pipelines which let you inherit
  pipelines from reuable pipeline library and then use a composition DSL above Tekton
  which lets you add/remove/replace steps. jenkins-x.
---
Open the original post ↗ https://jenkins-x.io/blog/2020/11/11/accelerate-tekton/
