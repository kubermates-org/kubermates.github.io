---
title: "🌐 Kubernetes DNS: How to Use In-Cluster and Azure Private DNS Together"
date: 2024-08-17T17:51:44+00:00
description: "Kubernetes is a powerful platform for managing containerized applications, providing robust tools for..."
tags: ["kubernetes", "azure", "cloud", "networking"]
draft: false
slug: "kubernetes-dns-how-to-use-in-cluster-and-azure-private-dns-together-48h3"
devto_id: 1961446
devto_url: "https://dev.to/hkhelil/kubernetes-dns-how-to-use-in-cluster-and-azure-private-dns-together-48h3"
---
Kubernetes is a powerful platform for managing containerized applications, providing robust tools for networking, service discovery, and DNS resolution. This guide will explore how Kubernetes handles DNS resolution within the cluster and how you can integrate it with Azure Private DNS to securely resolve external, private resources.

## 🔍 Understanding Kubernetes Services and DNS Resolution

Kubernetes Services provide a stable network identity for a set of Pods, allowing other components to communicate with them reliably. This is crucial since Pods in Kubernetes are ephemeral and their IP addresses can change over time.

### 🛠️ Types of Kubernetes Services

Kubernetes supports several types of Services, each tailored to different use cases:

1. **ClusterIP** 🏠: Exposes the Service on an internal IP, making it accessible only within the cluster.
2. **NodePort** 🌐: Exposes the Service on each Node’s IP at a static port, allowing external access.
3. **LoadBalancer** ⚖️: Exposes the Service externally using a cloud provider’s load balancer.
4. **ExternalName** 🔗: Maps the Service to an external DNS name, returning a CNAME record with that name.

### 🧩 DNS Resolution Inside the Kubernetes Cluster

Kubernetes automatically sets up a DNS system within the cluster, enabling Pods to resolve Services using DNS names. This makes service discovery straightforward, allowing Pods to communicate with each other seamlessly.

#### Example: Resolving a Service Inside the Cluster

Consider a Service named `web-service` in the `default` namespace:

1. **Service Definition**:
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: web-service
   spec:
     selector:
       app: web-app
     ports:
     - protocol: TCP
       port: 80
       targetPort: 8080
   ```

2. **DNS Resolution**:
   - **From the same namespace**: A Pod in the `default` namespace can resolve the Service by simply using `web-service`.
   - **From a different namespace**: A Pod in the `production` namespace would use the full DNS name: `web-service.default.svc.cluster.local`.

   ```bash
   # Inside a Pod in the default namespace
   curl http://web-service

   # Inside a Pod in the production namespace
   curl http://web-service.default.svc.cluster.local
   ```

This built-in DNS system ensures that all Services in the cluster are easily discoverable and accessible by their names.

## 🌐 Integrating and Using Azure Private DNS with Kubernetes

In scenarios where your Kubernetes applications need to resolve private resources hosted in Azure, you can configure your Pods to use Azure Private DNS. Azure Private DNS provides a secure and isolated DNS service within your Azure virtual network (VNet), enabling private domain name resolution.

### Step 1: Set Up Azure Private DNS

First, ensure that your Azure Private DNS Zone is set up within your Azure environment. This DNS zone should be linked to your virtual network to enable private DNS resolution within that VNet.

### Step 2: Configure Kubernetes Pods to Use Azure Private DNS

You can specify Azure Private DNS servers using the `dnsConfig` field in the Pod specification.

#### Example: Using Azure Private DNS for Resolution

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: azure-private-dns-example
spec:
  containers:
  - name: my-app
    image: my-app-image
  dnsConfig:
    nameservers:
      - 10.0.0.4  # Example IP of the Azure Private DNS resolver within your VNet
    searches:
      - myprivatedomain.internal
  dnsPolicy: None
```

Replace `10.0.0.4` with the IP address of the Azure Private DNS resolver within your virtual network. This IP address is typically the address of the DNS server provided by Azure's VNet.

### Step 3: Test DNS Resolution

After deploying the Pod, you can test DNS resolution to ensure it's using Azure Private DNS:

```bash
# Inside the Pod
nslookup myapp.myprivatedomain.internal
```

This command should successfully resolve the private domain using Azure Private DNS.

## 🌐 Combining Internal Cluster DNS with Azure Private DNS

In many cases, you might want to prioritize DNS resolution within the Kubernetes cluster but still resolve private domains using Azure Private DNS. This can be achieved by combining the `ClusterFirst` DNS policy with custom DNS settings.

### 📚 The `ClusterFirst` DNS Policy

The `ClusterFirst` DNS policy ensures that DNS queries for Kubernetes Services are resolved using the cluster's DNS service first. If the query isn't resolved within the cluster, it then falls back to external DNS servers, such as Azure Private DNS.

#### Example: Combining `ClusterFirst` with Azure Private DNS

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: combined-dns-example
spec:
  containers:
  - name: my-app
    image: my-app-image
  dnsConfig:
    nameservers:
      - 10.0.0.4  # Azure Private DNS resolver
    searches:
      - myprivatedomain.internal
  dnsPolicy: ClusterFirst
```

In this configuration:
- **ClusterFirst** ensures that internal cluster DNS queries are handled by the Kubernetes DNS service.
- External DNS queries (those not resolved by the cluster) are forwarded to the Azure Private DNS resolver.

### ⚙️ Benefits of Combining Internal and Azure Private DNS

- **🛠️ Optimized Intra-Cluster Resolution**: Ensures efficient resolution of Services within the Kubernetes cluster.
- **🌐 Controlled Private DNS Resolution**: Custom DNS servers, like Azure Private DNS, allow secure resolution of private domain names within your VNet.
- **🔍 Tailored Search Domains**: Facilitates the resolution of specific private domains without needing fully qualified domain names (FQDNs).

## 🔄 Comparing Private Domains Resolution with External Names

Kubernetes provides different methods for resolving domains, including using private domains through services like Azure Private DNS and resolving external names via the `ExternalName` Service. Here’s a comparison of these approaches:

### 🔐 Private Domains with Azure Private DNS

- **Use Case**: Private domains within your organization's Azure VNet, where security and isolation are critical.
- **Resolution**: Custom DNS servers (e.g., Azure Private DNS) handle the resolution of internal domain names.
- **DNS Management**: You manage the DNS records within the Azure Private DNS Zone.
- **Security**: Offers enhanced security by keeping DNS traffic within the private network, ensuring that sensitive resources are not exposed to the public internet.

#### Example:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-dns-pod
spec:
  containers:
  - name: my-app
    image: my-app-image
  dnsConfig:
    nameservers:
      - 10.0.0.4  # Azure Private DNS resolver
    searches:
      - myprivatedomain.internal
  dnsPolicy: None
```

### 🌍 External Names with `ExternalName` Service

- **Use Case**: Resolving external domain names, typically public DNS names, to internal or external services.
- **Resolution**: Kubernetes automatically maps the Service to a CNAME record that points to an external DNS name.
- **DNS Management**: Managed by the external DNS provider (e.g., public DNS for a website).
- **Security**: While useful for integrating external services, it may expose internal resources if not configured securely.

#### Example:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-service
spec:
  type: ExternalName
  externalName: external-service.com
```

### 📝 Key Differences

1. **Scope**:
   - **Private Domains**: Typically used for internal resources within a private network.
   - **External Names**: Used for mapping Kubernetes Services to external, usually public, domains.

2. **Security**:
   - **Private Domains**: Offers higher security by keeping DNS queries and resolutions within the private network.
   - **External Names**: May involve public DNS resolution, which could expose certain details if not properly managed.

3. **Management**:
   - **Private Domains**: Managed internally within Azure (or another private DNS provider), giving you full control over DNS records.
   - **External Names**: Managed by an external DNS provider, which may be less flexible for internal network use cases.

## 🏁 Conclusion

Kubernetes provides a flexible and robust DNS system that facilitates service discovery within the cluster. By integrating Azure Private DNS, you can securely extend this functionality to resolve private resources within your Azure environment. Combining internal cluster DNS with Azure Private DNS allows you to optimize DNS resolution for both internal Kubernetes services and external private resources, ensuring secure and reliable communication across your applications.

🚀 With these configurations, your Kubernetes applications will be well-equipped to handle complex networking requirements securely and efficiently, both within the cluster and across private domains in Azure.

Happy clustering! 🌐🔒
