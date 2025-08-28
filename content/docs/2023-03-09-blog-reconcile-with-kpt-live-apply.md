---
title: 'Blog: Reconcile with kpt live apply'
date: '2023-03-09T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2023/03/09/kpt-live-apply/
post_kind: link
draft: false
tldr: Since the dawn of Jenkins X 3 the default last step of reconciling the state
  of the files in your cluster repository to your cluster has been to execute kubectl
  apply. You can find more details about this here.
summary: Since the dawn of Jenkins X 3 the default last step of reconciling the state
  of the files in your cluster repository to your cluster has been to execute kubectl
  apply. You can find more details about this here. There are some drawbacks with
  kubectl apply though. The one that made me start looking for alternatives was that
  if you remove a resource from your cluster repository it may not be removed from
  your cluster. The way deletion works with kubectl apply is that it is handed the
  option --prune which will remove resources that are not in the manifests. Except
  that it doesn’t always work as expected. It will only remove certain kinds of resources
  defined in kubectl. In my case I removed an HorizontalPodAutoscaler from my cluster
  repository, but it wasn’t removed from my cluster. When trying to find a solution
  to this I first tried to override this default list in kubectl of things to prune,
  but this turned out to be difficult in the general case. I also tried the already
  existing alternative of using kapp to apply the manifests, but I couldn’t get that
  to work. Looking for other options I settled for kpt live apply. You enable the
  use of kpt live apply by adding to the Makefile of your cluster repository anywhere
  before include versionStream/src/Makefile.
---
Open the original post ↗ https://jenkins-x.io/blog/2023/03/09/kpt-live-apply/
