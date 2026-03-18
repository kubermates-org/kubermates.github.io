---
title: Registry Mirror Authentication with Kubernetes Secrets
date: '2026-03-16T11:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2026/03/16/registry-mirror-authentication-with-kubernetes-secrets-2/
post_kind: link
draft: false
tldr: 'Using the credential provider with OpenShift 4.21 OpenShift 4.22+: CRIOCredentialProviderConfig
  API Conclusion Posted on March 16, 2026 by Sascha Grunert, Red Hat CNCF projects
  highlighted in this post Part II: A Platform Integration Example In Part I, we explored
  the architecture of the CRI-O credential provider and walked through a manual setup.
  In this part, we’ll see how platforms like OpenShift and its upstream open-source
  project OKD integrate the credential provider natively, making deployment simpler.'
summary: 'Using the credential provider with OpenShift 4.21 OpenShift 4.22+: CRIOCredentialProviderConfig
  API Conclusion Posted on March 16, 2026 by Sascha Grunert, Red Hat CNCF projects
  highlighted in this post Part II: A Platform Integration Example In Part I, we explored
  the architecture of the CRI-O credential provider and walked through a manual setup.
  In this part, we’ll see how platforms like OpenShift and its upstream open-source
  project OKD integrate the credential provider natively, making deployment simpler.
  OpenShift includes the credential provider starting with version 4.21, with different
  integration levels across versions showing the evolution toward more native platform
  support. OpenShift 4.21 ships the crio-credential-provider RPM package along with
  CRI-O v1.34, which is the minimum version required for the credential provider support.
  Earlier CRI-O versions do not support namespace-scoped auth files. Since there is
  no Custom Resource Definition or API for managing the credential provider configuration
  in OpenShift 4.21, users must manually create a MachineConfig resource to deploy
  the configuration files. By overriding the existing ECR credential provider configuration
  file, the kubelet automatically uses the CRI-O credential provider without requiring
  additional configuration. This approach works on all OpenShift installations regardless
  of the underlying cloud provider. crio-credential-provider MachineConfig Enable
  the KubeletServiceAccountTokenForCredentialProviders feature gate: KubeletServiceAccountTokenForCredentialProviders
  kubectl patch FeatureGate cluster --type merge --patch ''{"spec":{"featureSet":"CustomNoUpgrade","customNoUpgrade":{"enabled":["KubeletServiceAccountTokenForCredentialProviders"]}}}''
  kubectl patch FeatureGate cluster --type merge --patch ''{"spec":{"featureSet":"CustomNoUpgrade","customNoUpgrade":{"enabled":["KubeletServiceAccountTokenForCredentialProviders"]}}}''
  Create Ignition Config Create a file named machine-config. bu with the following
  Ignition Config. This configuration creates both the credential provider configuration
  and the registry mirror configuration on worker nodes. Note that this will overwrite
  both /etc/kubernetes/credential-providers/ecr-credential-provider.'
---
Open the original post ↗ https://www.cncf.io/blog/2026/03/16/registry-mirror-authentication-with-kubernetes-secrets-2/
