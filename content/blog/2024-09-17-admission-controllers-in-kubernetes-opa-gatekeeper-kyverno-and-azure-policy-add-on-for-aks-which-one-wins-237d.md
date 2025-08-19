---
title: "Admission Controllers in Kubernetes: OPA GateKeeper, Kyverno, and Azure Policy Add-on for AKS—Which One Wins? 🏆"
date: 2024-09-17T07:25:52+00:00
description: "When managing a Kubernetes cluster, controlling what gets deployed and ensuring resources comply with..."
tags: ["kubernetes", "cloud", "azure", "security"]
draft: false
slug: "admission-controllers-in-kubernetes-opa-gatekeeper-kyverno-and-azure-policy-add-on-for-aks-which-one-wins-237d"
devto_id: 1998616
devto_url: "https://dev.to/hkhelil/admission-controllers-in-kubernetes-opa-gatekeeper-kyverno-and-azure-policy-add-on-for-aks-which-one-wins-237d"
---
When managing a Kubernetes cluster, controlling what gets deployed and ensuring resources comply with security, governance, and operational policies is essential. Admission controllers act as "gatekeepers" for your cluster, ensuring only compliant resources get through. 🛡️

Three popular options for extending Kubernetes' admission control functionality are **OPA GateKeeper**, **Kyverno**, and the **Azure Policy Add-on for AKS** (which incorporates OPA GateKeeper's engine). In this article, we’ll compare these solutions and show why **Kyverno** is still the most user-friendly and versatile option for Kubernetes users. 🌊

## What Do Admission Controllers Do? 🤔

Admission controllers intercept requests to the Kubernetes API server before objects like Pods, Services, or ConfigMaps are persisted. They can either:

- **Validate** the request to ensure it adheres to specific policies (e.g., preventing privileged containers).
- **Mutate** the request to modify or fix it so that it complies with policies (e.g., automatically adding labels or setting resource limits).

Now, let's compare **OPA GateKeeper**, **Kyverno**, and **Azure Policy Add-on for AKS**.

## OPA GateKeeper 🛡️

**OPA GateKeeper** integrates the **Open Policy Agent (OPA)** with Kubernetes to enforce policies using the **Rego** language. Originally designed as a validating admission controller, GateKeeper now also supports **mutating webhooks**. This means it can both validate and modify incoming Kubernetes resources. [Learn more about GateKeeper’s mutation capabilities](https://open-policy-agent.github.io/gatekeeper/website/docs/mutation).

### Key Features:
- **Flexible Policies**: With Rego, you can create complex rules, such as enforcing that certain namespaces only contain specific types of resources.
- **Constraint Templates**: These allow for reusable policies that can be applied across multiple clusters.
- **Mutating Webhooks**: OPA GateKeeper now supports mutation, enabling it to modify resources to meet policy requirements, similar to Kyverno.

Example OPA GateKeeper policy in Rego:

```rego
package kubernetes.admission

deny[msg] {
  input.kind == "Pod"
  input.spec.securityContext.runAsRoot == true
  msg = "Running as root is not allowed!"
}
```

### Challenges:
- **Rego Learning Curve**: While Rego is powerful, it can be challenging to learn, especially for teams not familiar with policy-as-code approaches.
  
With the new mutating webhooks feature, OPA GateKeeper can now validate and mutate resources, narrowing the gap between it and Kyverno in terms of functionality.

## Kyverno 💡

**Kyverno** is a Kubernetes-native policy engine. It uses **YAML**, which makes it much more approachable for Kubernetes users, as policies can be written using familiar formats. Kyverno supports both **validation** and **mutation**, offering a full spectrum of policy enforcement.

### Key Features:
- **Easy Policy Writing**: Policies are written in YAML as Kubernetes Custom Resources (CRs), which is far easier to write and understand compared to OPA’s Rego.
  
Example Kyverno policy to enforce resource limits on Pods:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: enforce-resource-limits
spec:
  rules:
  - name: check-resource-limits
    match:
      resources:
        kinds:
        - Pod
    validate:
      message: "All Pods must have resource limits defined."
      pattern:
        spec:
          containers:
          - resources:
              limits:
                memory: "?*"
                cpu: "?*"
```

- **Mutating and Validating**: Kyverno can modify and validate requests. For example, if a Pod doesn’t have resource limits, Kyverno can automatically add those limits.
- **Auto-Generate Resources**: Kyverno can automatically create resources such as network policies or security configurations, helping enforce security and compliance across clusters.

### Advantages:
- **YAML Policies**: Policies are written in a language Kubernetes users already understand, making it easier to adopt compared to Rego.
- **Mutating Power**: Kyverno can both reject and modify requests, making it versatile for real-world Kubernetes workloads.
  
## Azure Policy Add-on for AKS ⚙️

The **Azure Policy Add-on for AKS** is Microsoft’s solution for policy enforcement in **Azure Kubernetes Service (AKS)** clusters. It is powered by **OPA GateKeeper** but is integrated with **Azure Policy**, making it easy to ensure compliance across AKS clusters. [Learn more about Azure Policy Add-on for AKS](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes#create-a-policy-definition).

### Key Features:
- **Azure Integration**: The Azure Policy Add-on integrates with AKS and Azure Policy, making it easy to apply policies across an entire Azure environment.
- **Rego-Based Policies**: Policies are still defined in Rego, leveraging OPA’s policy engine under the hood.

Example policy to restrict privileged containers in AKS using Azure Policy:

```yaml
{
    "properties": {
        "displayName": "Restrict privileged containers",
        "policyType": "BuiltIn",
        "mode": "Microsoft.Kubernetes.Data",
        "metadata": {
            "category": "Kubernetes"
        },
        "parameters": {
            "effect": {
                "type": "String",
                "defaultValue": "deny",
                "allowedValues": [
                    "audit",
                    "deny",
                    "disabled"
                ]
            }
        },
        "policyRule": {
            "if": {
                "allOf": [
                    {
                        "field": "type",
                        "equals": "Microsoft.Kubernetes/connectedClusters"
                    },
                    {
                        "field": "Microsoft.KubernetesData.securityContext.privileged",
                        "equals": "true"
                    }
                ]
            },
            "then": {
                "effect": "[parameters('effect')]"
            }
        }
    }
}
```

This example uses Azure Policy syntax but is backed by OPA GateKeeper under the hood. [Learn how to create Azure Policy for AKS](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes#create-a-policy-definition).

### Challenges:
- **Azure-Specific**: The Azure Policy Add-on is tailored for AKS environments, which means it may not be ideal for multi-cloud or hybrid setups.
- **Rego Learning Curve**: Since it is still based on Rego, it requires teams to learn this language, which can be a barrier for some users.

## Why Kyverno is the Best Choice 🏅

After reviewing all three options—OPA GateKeeper, Kyverno, and Azure Policy Add-on for AKS—**Kyverno** continues to stand out for its simplicity and versatility. Here’s why:

1. **YAML-Based Policies**: Kyverno uses YAML, a format that Kubernetes users are already familiar with, making it easy to get started without learning a new policy language like Rego.

   Example of a simple Kyverno policy to ensure Pods have labels:
   
   ```yaml
   apiVersion: kyverno.io/v1
   kind: ClusterPolicy
   metadata:
     name: require-label
   spec:
     rules:
     - name: check-label
       match:
         resources:
           kinds:
           - Pod
       validate:
         message: "All Pods must have the 'app' label."
         pattern:
           metadata:
             labels:
               app: "?*"
   ```

2. **Mutating and Validating**: Both OPA GateKeeper and Kyverno now support mutation and validation, but Kyverno’s use of YAML makes it easier to write and maintain policies without a steep learning curve.

3. **Kubernetes-Native**: Kyverno was designed specifically for Kubernetes, whereas OPA GateKeeper was adapted to work within Kubernetes. This gives Kyverno a more intuitive and seamless integration with Kubernetes workflows.

4. **Multi-Cloud and Hybrid Support**: While Azure Policy Add-on is ideal for AKS, Kyverno works across any Kubernetes environment—on-prem, multi-cloud, or hybrid setups—making it the more flexible option.

## Final Thoughts 🌟

While OPA GateKeeper has evolved to support mutation, **Kyverno** remains the best choice for most Kubernetes users due to its user-friendly YAML policies, Kubernetes-native approach, and versatility across various environments. If you're looking for a simple yet powerful policy engine, Kyverno is the clear winner for Kubernetes policy enforcement. Give it a try, and see how it simplifies your policy management! 😊

Happy clustering !
