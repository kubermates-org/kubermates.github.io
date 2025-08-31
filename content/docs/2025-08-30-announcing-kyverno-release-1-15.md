---
title: Announcing Kyverno Release 1.15!
date: '2025-08-30T13:31:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/08/30/announcing-kyverno-release-1-15/
post_kind: link
draft: false
tldr: 'TL;DR New Policy Types MutatingPolicy: Flexible Resource Transformation GeneratingPolicy:
  Intelligent Resource Creation DeletingPolicy: Controlled Cleanup Made Easy Pod Security
  Standard(PSS) Policy Performance: ClusterPolicy vs ValidatingPolicy Key Performance
  Improvements Why It Matters New OpenReports API Group Support Community & Contributions
  Getting Started What’s Next? Conclusion Posted on August 30, 2025 by The Kyverno
  Team CNCF projects highlighted in this post Kyverno 1.15 makes Kubernetes policy
  management more powerful, extensible, and user-friendly. We are thrilled to announce
  the release of Kyverno 1.15.0, continuing our mission to make policy management
  in Kubernetes environments more modular, performant, and user-friendly.'
summary: 'TL;DR New Policy Types MutatingPolicy: Flexible Resource Transformation
  GeneratingPolicy: Intelligent Resource Creation DeletingPolicy: Controlled Cleanup
  Made Easy Pod Security Standard(PSS) Policy Performance: ClusterPolicy vs ValidatingPolicy
  Key Performance Improvements Why It Matters New OpenReports API Group Support Community
  & Contributions Getting Started What’s Next? Conclusion Posted on August 30, 2025
  by The Kyverno Team CNCF projects highlighted in this post Kyverno 1.15 makes Kubernetes
  policy management more powerful, extensible, and user-friendly. We are thrilled
  to announce the release of Kyverno 1.15.0, continuing our mission to make policy
  management in Kubernetes environments more modular, performant, and user-friendly.
  This release introduces new capabilities across multiple policy types, enhances
  testing and CLI functionality, and brings many improvements that a vibrant community
  has contributed. New MutatingPolicy for dynamic resource transformation with native
  Kubernetes integration New GeneratingPolicy for intelligent resource creation and
  synchronization using CEL expressions New DeletingPolicy resource for controlled
  cleanup of Kubernetes resources Advanced CEL functions and enhanced policy exception
  support for fine-grained control Community milestone: over 850 changes merged from
  70+ contributors, including many first-timers! Building on the foundation of ValidatingPolicy
  and ImageValidatingPolicy from previous releases, Kyverno 1.15 introduces three
  new CEL-based policy types that complete our comprehensive policy ecosystem. While
  Kyverno, created by Nirmata, maintains its traditional policy engine capabilities,
  these new policy types provide native Kubernetes integration by automatically converting
  to Kubernetes admission controllers – MutatingPolicy converts to MutatingAdmissionPolicy
  (MAP) and ValidatingPolicy converts to ValidatingAdmissionPolicy (VAP). This hybrid
  approach gives users the flexibility to choose between Kyverno’s rich policy engine
  features and native Kubernetes performance. The new MutatingPolicy type provides
  native Kubernetes integration through MutatingAdmissionPolicy, offering: Full support
  for all functions that a mutate rule of a traditional policy supports Easier for
  each loop iteration with CEL’s map() and filter() functions Full support of advanced
  custom CEL libraries for complex policy logic CLI support for offline resources
  mutation in CI/CD pipelines Here is an example of adding default labels to deployments.
  Previous ClusterPolicy approach: apiVersion: kyverno. io/v1 kind: ClusterPolicy
  metadata: name: add-default-labels spec: rules: - name: add-labels match: resources:
  kinds: - Deployment mutate: patchStrategicMerge: metadata: labels: environment:
  "production" managed-by: "kyverno" apiVersion: kyverno. io/v1 kind: ClusterPolicy
  metadata: name: add-default-labels spec: rules: - name: add-labels match: resources:
  kinds: - Deployment mutate: patchStrategicMerge: metadata: labels: environment:
  "production" managed-by: "kyverno" New MutatingPolicy approach: MutatingPolicy apiVersion:
  policies. kyverno. io/v1alpha1 kind: MutatingPolicy metadata: name: add-default-labels
  spec: mutations: - patchType: ApplyConfiguration applyConfiguration: expression:
  > Object{ metadata: Object.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/08/30/announcing-kyverno-release-1-15/
