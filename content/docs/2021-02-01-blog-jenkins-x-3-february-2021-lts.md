---
title: 'Blog: Jenkins X 3 - February 2021 LTS'
date: '2021-02-01T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2021/02/01/jx3-lts-feb-21/
post_kind: link
draft: false
tldr: This is the first LTS release for Jenkins X 3. x.
summary: 'This is the first LTS release for Jenkins X 3. x. We are still in the Beta
  release and the leadup to GA includes ensuring the process for LTS monthly releases
  is validated and working well. This first releases focuses on: more documentation
  and examples can be found here Because Jenkins X uses GitOps we can see the git
  diff of changes that will be brought in with a cluster upgrade. Here is the Pull
  Request that has been verified for February LTS release. https://github. com/jenkins-x/jx3-lts-versions/pull/209/files
  Included in the release is a switch of the NGINX Helm chart from the old Helm stable
  registry. It was discussed on the community slack that some users on EKS and not
  using a custom domain had to change the domain in their cluster jx-requirements.
  yml file. The change of Chart repository meant the old resources were removed and
  new ones added, resulting in a new Kubernetes LoadBalancer service was created,
  resulting in a new external IP address. You may need to update the domain in your
  jx-requirements. yml.'
---
Open the original post ↗ https://jenkins-x.io/blog/2021/02/01/jx3-lts-feb-21/
