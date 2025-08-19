---
title: "Understanding eBPF and Its Application in Modern Cloud Environments 🚀"
date: 2024-09-08T06:53:32+00:00
description: "What is eBPF? 🤔   eBPF (Extended Berkeley Packet Filter) is like magic for the Linux kernel!..."
tags: ["kubernetes", "azure", "networking", "cloud"]
draft: false
slug: "understanding-ebpf-and-its-application-in-modern-cloud-environments-3f99"
devto_id: 1982439
devto_url: "https://dev.to/hkhelil/understanding-ebpf-and-its-application-in-modern-cloud-environments-3f99"
---
## What is eBPF? 🤔

**eBPF** (Extended Berkeley Packet Filter) is like magic for the Linux kernel! 🪄 It lets developers run custom code directly within the kernel, safely and efficiently, without needing to modify the kernel's source code or load new modules. Originally, eBPF was created to help with network packet filtering, but it has evolved into a Swiss Army knife 🛠️ for all sorts of tasks, from observability to security and system performance monitoring.

Imagine being able to intercept and analyze network traffic, monitor system performance, or enforce security policies—all in real-time and with minimal overhead. That’s the power of eBPF! It’s like having superpowers in your toolbox, ready to help you see what's happening under the hood of your systems, tweak things on the fly, and keep everything running smoothly.

## How eBPF Works ⚙️

At its core, eBPF works by attaching tiny programs to hooks in the Linux kernel. These hooks can trigger eBPF programs whenever certain events occur, like a network packet arriving or a file being accessed. The beauty of eBPF is that these programs run in a secure, sandboxed environment, meaning they can’t crash your system or cause instability.

The eBPF programs are compiled into a special bytecode, which the kernel verifies for safety before executing. Once verified, the kernel compiles this bytecode into machine code that runs at near-native speed. This allows eBPF to perform complex tasks with minimal impact on performance, making it a perfect fit for real-time monitoring and security applications.

## Cilium: Bringing eBPF to Kubernetes with AKS 🛡️

One of the coolest ways to use eBPF in modern cloud environments is with **Cilium**. Cilium is an open-source project that supercharges Kubernetes networking, observability, and security using eBPF. It replaces traditional networking tools like iptables with an eBPF-based approach, providing faster, more scalable, and feature-rich networking for your Kubernetes clusters.

### Cilium and AKS: A Perfect Pairing 🤝

**Azure Kubernetes Service (AKS)** is Microsoft Azure's managed Kubernetes service, making it easier to deploy, manage, and scale containerized applications. Integrating Cilium with AKS gives your Kubernetes networking a serious upgrade by harnessing the power of eBPF.

Here’s a quick overview of how you can get Cilium running on your AKS cluster using the latest versions:

1. **Create Your AKS Cluster**:
   - Start by setting up your AKS cluster using the Azure portal, Azure CLI, or Terraform. Ensure your Kubernetes version is compatible with Cilium (typically Kubernetes 1.18 or later).

2. **Install Cilium**:
   - First, add the Cilium Helm repository:
     ```bash
     helm repo add cilium https://helm.cilium.io/
     helm repo update
     ```
   - Next, deploy the latest version of Cilium (1.16.1) to your AKS cluster:
     ```bash
     helm install cilium cilium/cilium --version 1.16.1 \
       --namespace kube-system \
       --set azure.enabled=true
     ```
     The `--version 1.16.1` flag ensures you're using the latest stable release of Cilium.

3. **Deploy Hubble for Observability**:
   - Hubble is an integral part of Cilium that provides observability into your network. You can deploy the latest version of Hubble as follows:
     ```bash
     helm install hubble-relay cilium/hubble-relay \
       --version 1.16.1 \
       --namespace kube-system
     helm install hubble-ui cilium/hubble-ui \
       --version 1.16.1 \
       --namespace kube-system
     ```
   - Access the Hubble UI to get a visual overview of your network traffic and security policies.

4. **Configure Advanced Network Policies**:
   - With Cilium in place, you can define advanced Kubernetes Network Policies. For example, to allow traffic only between specific services:
     ```yaml
     apiVersion: networking.k8s.io/v1
     kind: NetworkPolicy
     metadata:
       name: allow-specific-traffic
       namespace: default
     spec:
       podSelector:
         matchLabels:
           app: my-app
       ingress:
       - from:
         - podSelector:
             matchLabels:
               app: my-allowed-app
       policyTypes:
       - Ingress
     ```
   - This policy ensures that only pods with the label `app=my-allowed-app` can communicate with pods labeled `app=my-app`.

5. **Enable Transparent Encryption**:
   - Cilium also allows you to secure your network traffic with transparent encryption. To enable this feature:
     ```bash
     helm upgrade cilium cilium/cilium --version 1.16.1 \
       --namespace kube-system \
       --set encryption.enabled=true
     ```
   - Transparent encryption encrypts network traffic between nodes, enhancing security without requiring application changes.

6. **Use eBPF-based Load Balancing**:
   - Cilium provides an efficient eBPF-based load balancer. To enable and configure it:
     ```bash
     helm upgrade cilium cilium/cilium --version 1.16.1 \
       --namespace kube-system \
       --set loadBalancer.algorithm=least-conn
     ```
   - This command sets the load balancing algorithm to `least-conn`, distributing traffic to the node with the fewest active connections.

### Deploying Cilium as an AKS Plugin 🧩

Good news! If you’re looking to make your Cilium integration even more seamless, you can deploy Cilium as an **AKS plugin**. This approach simplifies the installation and management process even further by integrating Cilium directly into the AKS ecosystem.

With Cilium as an AKS plugin, you get:

- **Ease of Use**: AKS takes care of the deployment and management, reducing the manual steps you need to take.
- **Tighter Integration**: Enjoy better integration with Azure-specific features and a more consistent management experience.
- **Automatic Updates**: Keep your Cilium deployment up-to-date with the latest features and security patches automatically applied by Azure.

To deploy Cilium as a plugin in AKS, follow the instructions in the AKS documentation or use the Azure CLI with specific flags to enable Cilium during cluster creation. This approach is perfect for those who want the benefits of Cilium without the hassle of manual installation and maintenance.

## Deploying an AKS Cluster with Cilium Enabled via Azure CLI

To deploy an AKS cluster with Cilium as the network plugin, follow these steps:

1. **Install the Azure CLI**: If you haven’t installed the Azure CLI yet, you can do so by following the instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli). Make sure you’re using the latest version to avoid any issues.

2. **Log in to Azure**:
   ```bash
   az login
   ```
   This command opens a web page where you can authenticate with your Azure account.

3. **Set Your Subscription**: If you have multiple Azure subscriptions, set the one you want to use for the AKS cluster.
   ```bash
   az account set --subscription "<your-subscription-id>"
   ```

4. **Create a Resource Group**: A resource group is required to hold your AKS cluster.
   ```bash
   az group create --name MyResourceGroup --location eastus
   ```

5. **Deploy the AKS Cluster with Cilium Enabled**:
   You can now create your AKS cluster and enable Cilium as the network plugin by using the following command:

   ```bash
   az aks create \
     --resource-group MyResourceGroup \
     --name MyAKSCluster \
     --network-plugin azure \
     --network-policy cilium \
     --enable-managed-identity \
     --node-count 3 \
     --enable-addons monitoring \
     --generate-ssh-keys \
     --kubernetes-version 1.30
   ```

   Here’s a breakdown of what each parameter does:
   - `--resource-group`: Specifies the resource group where the AKS cluster will be deployed.
   - `--name`: The name of your AKS cluster.
   - `--network-plugin`: Specifies the network plugin. When using Cilium, the `azure` plugin is used with `cilium` as the network policy.
   - `--network-policy`: Sets the network policy to `cilium` to enable Cilium in your AKS cluster.
   - `--enable-managed-identity`: Enables a managed identity for the cluster, which is the preferred method for AKS.
   - `--node-count`: Specifies the number of nodes in the node pool.
   - `--enable-addons monitoring`: Enables monitoring for your AKS cluster using Azure Monitor.
   - `--generate-ssh-keys`: Automatically generates SSH keys to access the nodes.
   - `--kubernetes-version`: Specifies the Kubernetes version to use, set to the latest supported version, 1.30.

6. **Verify the Deployment**:
   Once the command completes, you can verify that your AKS cluster is up and running:

   ```bash
   az aks get-credentials --resource-group MyResourceGroup --name MyAKSCluster
   kubectl get nodes
   ```

   This command retrieves the credentials to manage your AKS cluster with `kubectl` and lists the nodes in your cluster.

7. **Check Cilium Status**:


   You can check if Cilium is running correctly by using:

   ```bash
   kubectl -n kube-system get pods -l k8s-app=cilium
   ```

   This command lists the Cilium pods running in the `kube-system` namespace. All pods should be in the `Running` state.

## Why Cilium and eBPF Rock on AKS 🤘

- **Blazing Fast Performance**: Thanks to eBPF, Cilium processes network traffic faster than traditional methods.
- **Scalable Solutions**: Cilium’s architecture is designed to handle the needs of large, dynamic Kubernetes environments.
- **Deep Observability**: Hubble, powered by eBPF, gives you unparalleled insights into your network, making it easier to spot issues and optimize performance.
- **Advanced Security**: Cilium’s eBPF-driven network policies provide fine-grained control over traffic, helping to lock down your environment securely.

## Wrapping Up 🎁

eBPF is revolutionizing how we interact with the Linux kernel, opening up new possibilities for networking, security, and observability. Cilium, built on the foundation of eBPF, brings these advancements directly to Kubernetes, making it easier to manage complex, large-scale environments like those on AKS.

Whether you’re deploying Cilium manually or as an AKS plugin, you’ll benefit from faster networking, enhanced security, and deep observability—all with the power of eBPF under the hood. So, if you’re looking to supercharge your Kubernetes experience on AKS, give Cilium a try! 🎉

Happy clustering !
