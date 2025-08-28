---
title: 'Blog: Don''t use docker, use kubernetes'
date: '2021-05-17T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/05/17/dont-use-docker/
post_kind: link
draft: false
tldr: Don't use docker, use kubernetes Why use kubernetes instead of docker? How to
  get kubernetes? How do I connect to kubernetes? How do I replace docker with kubernetes?
  docker run => kubectl run docker build => kubectl build compose => helm testcontainers
  => sidecars / kubedock help! we are not even using kubernetes yet other handy kubectl
  commands inner loop Conclusion Are you developing software that’s intended to run
  on kubernetes? If so we recommend not to use docker on your laptop. Docker on Windows/MacOS
  helps you run a VM that can then run linux containers easily.
summary: 'Don''t use docker, use kubernetes Why use kubernetes instead of docker?
  How to get kubernetes? How do I connect to kubernetes? How do I replace docker with
  kubernetes? docker run => kubectl run docker build => kubectl build compose => helm
  testcontainers => sidecars / kubedock help! we are not even using kubernetes yet
  other handy kubectl commands inner loop Conclusion Are you developing software that’s
  intended to run on kubernetes? If so we recommend not to use docker on your laptop.
  Docker on Windows/MacOS helps you run a VM that can then run linux containers easily.
  But why bother? We highly recommend just use a development kubernetes cluster -
  build and run your containers there instead then you’re closer to a production like
  environment. why test on a completely different VM and container orchestrator than
  production? It’s better to test on a similar environment to where you are really
  going to deploy your code test your kubernetes yaml / helm chart and associated
  configuration at the same time as you run your containers helps you catch mistakes
  earlier: it’s not just about running the container image; it’s about lots of other
  things too like networking, configuration, secrets, storage/volumes, cloud infrastructure,
  service mesh, liveness/readiness/startup probes - so why not test all of those things
  rather than just the image? it’s not just about running the container image; it’s
  about lots of other things too like networking, configuration, secrets, storage/volumes,
  cloud infrastructure, service mesh, liveness/readiness/startup probes - so why not
  test all of those things rather than just the image? some corporate environments
  don’t let you run VMs on your laptop anyway so running docker locally isn’t an option
  First you’ll need a kubernetes cluster. I fully agree with James Ward that developers
  should not need to run kubernetes. Friends don’t let friends setup and manage kubernetes
  clusters by hand :). So try ask your infrastructure team for a development cluster
  or, if you can, use the cloud to set-up a managed kubernetes cluster. All the public
  clouds have a relatively straightforward way to spin up a fully managed kubernetes
  cluster for you that will be relatively inexpensive & they are easy to scale down
  when you don’t need them. e. g. on Google Cloud it’s a couple of clicks and about
  5 minutes later you’ll have a fully managed kubernetes cluster ready to use. Its
  easy to enable auto-scaling too.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/05/17/dont-use-docker/
