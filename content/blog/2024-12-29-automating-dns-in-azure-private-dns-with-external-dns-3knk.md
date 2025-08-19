---
title: "Automating DNS in Azure Private DNS with External-DNS ☁️🔐"
date: 2024-12-29T17:07:48+00:00
description: "When running Kubernetes in Azure, one of the biggest time-savers you can implement is automatic DNS..."
draft: false
slug: "automating-dns-in-azure-private-dns-with-external-dns-3knk"
devto_id: 2175541
devto_url: "https://dev.to/hkhelil/automating-dns-in-azure-private-dns-with-external-dns-3knk"
---
*When running Kubernetes in Azure, one of the biggest time-savers you can implement is automatic DNS record management—especially for internal (private) services. By integrating [External-DNS](https://github.com/kubernetes-sigs/external-dns) with Azure Private DNS, you can say goodbye to manual record updates. Better yet, you can skip traditional service principals and use Azure Workload Identity to make your cluster more secure and secrets-free!* 🚀

In this article, we’ll show you how to configure External-DNS for Azure Private DNS using **Azure Workload Identity**, leveraging a snippet of a `values.yaml` that highlights the relevant settings.

## Why Use Azure Workload Identity?

Traditionally, External-DNS needs service principal credentials (client ID and secret) to manage DNS records. Azure Workload Identity allows you to integrate with Azure AD **without storing or distributing credential secrets** in Kubernetes. It utilizes the identity granted to your pods at runtime (managed identity) to request access tokens from Azure AD securely. This:

- **Eliminates** the need for manual secret management.  
- **Reduces** the risk of compromised secrets.  
- **Simplifies** your Kubernetes-to-Azure authentication setup.  

> **Note**: Azure Workload Identity is now **Generally Available (GA)**, so you no longer need to enable preview features.

## Prerequisites Checklist ✅

1. **Kubernetes Cluster**: An AKS cluster or self-managed cluster on Azure.  
2. **Azure Private DNS Zone**:  
   - e.g. `example.internal`, already created in your Azure subscription.  
3. **User-Assigned Managed Identity (UAMI)** created in Azure with the appropriate permissions (e.g., `DNS Zone Contributor`) on the DNS zone resource group.  
4. **Azure Workload Identity components** installed on your cluster (this typically involves the [Azure AD Workload Identity](https://azure.github.io/azure-workload-identity/docs/) setup steps).  
5. **External-DNS** Helm chart or YAML files ready to deploy.  

## Setting Up Azure Private DNS

If you haven’t created your Private DNS zone yet, you can do so quickly:

```bash
az network private-dns zone create \
  --resource-group <RESOURCE_GROUP> \
  --name example.internal
```

Then, link it to your Virtual Network so internal DNS can be resolved:

```bash
az network private-dns link vnet create \
  --resource-group <RESOURCE_GROUP> \
  --zone-name example.internal \
  --name myVnetLink \
  --virtual-network <VNET_ID> \
  --registration-enabled false
```

Replace `<RESOURCE_GROUP>` and `<VNET_ID>` with values for your environment.

## Create a User-Assigned Managed Identity (UAMI) 🔑

1. **Create the UAMI**  

   ```bash
   az identity create \
     --name external-dns-identity \
     --resource-group <RESOURCE_GROUP> \
     --location <LOCATION>
   ```

   This command returns JSON that includes an `id` and a `clientId` (important for later steps).

2. **Assign the Role**  
   Give the identity `DNS Zone Contributor` on your DNS zone resource group or at the subscription level:

   ```bash
   az role assignment create \
     --assignee <CLIENT_ID_OF_UAMI> \
     --role "DNS Zone Contributor" \
     --scope /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>
   ```

> **Note**: The `clientId` is also referred to as the “Application ID” of the managed identity.

## Enable Azure Workload Identity on Your Cluster

Azure Workload Identity is **GA** (generally available), so you don’t need to enable any preview features. However, you **do** need to install the necessary components in your cluster. Follow the [official installation guide](https://azure.github.io/azure-workload-identity/docs/installation.html) to:

1. Install the Azure Workload Identity webhook in your cluster.  
2. Configure a **Federated Identity Credential** referencing your cluster’s issuer and the service account you’ll create. This typically happens when you use the [azwi CLI tool](https://azure.github.io/azure-workload-identity/docs/installation.html#azure-workload-identity-cli-azwi) or manually configure a federated identity in your managed identity.

## The `values.yaml` Snippet Explained

Below is an example of a `values.yaml` you could use with the [External-DNS Helm chart](https://github.com/kubernetes-sigs/external-dns/tree/master/charts/external-dns). It integrates **Azure Workload Identity** and **Private DNS**:

```yaml
podLabels: 
  "azure.workload.identity/use": "true"

serviceAccount:
  create: true
  labels: 
    "azure.workload.identity/use": "true"
  annotations: 
    "azure.workload.identity/client-id": "<CLIENT_ID_OF_UAMI>"
  automountServiceAccountToken: true

logLevel: debug
logFormat: json
interval: 1m

provider:
  name: azure-private-dns # or 'azure' for public DNS

sources:
  - ingress

dnsPolicy: Default

domainFilters: 
  - example.internal

extraVolumes:
  - name: azure-config-file
    secret:
      secretName: <SECRET_NAME>

extraVolumeMounts:
  - name: azure-config-file
    mountPath: /etc/kubernetes/
    readOnly: true
```

### Key Sections Breakdown

1. **Workload Identity Labels & Annotations**  

   ```yaml
   podLabels: 
     "azure.workload.identity/use": "true"

   serviceAccount:
     create: true
     labels: 
       "azure.workload.identity/use": "true"
     annotations: 
       "azure.workload.identity/client-id": "<UAMI_CLIENT_ID>"
   ```

   - Tells Azure Workload Identity that pods in this deployment should use the user-assigned managed identity.  
   - The `client-id` annotation is the **Application ID** of your UAMI (from the step where you created the identity).

2. **Provider**  

   ```yaml
   provider:
     name: azure-private-dns
   ```

   - Tells External-DNS we’re using Azure Private DNS.  
   - For public DNS, use `azure`.

3. **Sources**  

   ```yaml

   sources:
     - ingress
   ```

   - External-DNS will create DNS records for ingresses (you can also add `service` or `crd` as needed).

4. **Domain Filters**

   ```yaml

   domainFilters:
     - "example.internal"
   ```

   - Ensures External-DNS only manages DNS records for `example.internal`.

5. **extraVolumes & extraVolumeMounts**  

   ```yaml

   extraVolumes:
     - name: azure-config-file
       secret:
         secretName: <SECRET_NAME>
   extraVolumeMounts:
     - name: azure-config-file
       mountPath: /etc/kubernetes/
       readOnly: true
   ```

   - If you still have minimal config in a secret (like subscription info or region), you can mount it.  
   - **Note**: With Azure Workload Identity, you typically don’t need a full credential file. If you do, it should not include any secrets, since the identity token is handled automatically.

## Deploying External-DNS via Helm 🏗️

Once you have your `values.yaml` ready, deploy or upgrade External-DNS:

```bash
helm repo add external-dns https://kubernetes-sigs.github.io/external-dns/
helm repo update

helm upgrade --install external-dns external-dns/external-dns \
  --namespace external-dns --create-namespace \
  --values values.yaml
```

This will create:

- A **Deployment** for External-DNS in the `external-dns` namespace.  
- A **ServiceAccount** with the appropriate labels/annotations for Azure Workload Identity.  
- Pods automatically requesting a token from Azure AD using the user-assigned managed identity, eliminating the need for storing a client secret.

## Example: Creating an Ingress

External-DNS will watch for ingresses (since we set `sources: [ingress]`). Here’s a simple example:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: sample-app
  annotations:
    external-dns.alpha.kubernetes.io/hostname: "app.example.internal"
spec:
  rules:
  - host: "app.example.internal"
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: sample-service
            port:
              number: 80
```

External-DNS sees this annotation, and automatically:

1. Authenticates to Azure via Workload Identity.  
2. Creates/Updates the DNS record `app.example.internal` in your private DNS zone to point to the ingress controller’s IP.  

*Zero manual DNS steps—just pure automation.* 🤖🎉

## Validation and Troubleshooting 🏷️

1. **Check Pod Logs**

   ```bash
   kubectl logs -f deploy/external-dns -n external-dns
   ```

   - You should see lines about detecting the ingress and creating/updating records.

2. **Verify the DNS Record**

   ```bash
   az network private-dns record-set a list \
     --zone-name example.internal \
     --resource-group <RESOURCE_GROUP> \
     --output table
   ```

   - Look for `app` in the list of A records.

3. **Ensure Proper Role Assignments**  
   - If External-DNS logs show permission errors, confirm the user-assigned identity has `DNS Zone Contributor`.

4. **Double-Check the Domain Filter**  
   - If your ingress annotation uses a domain not in `domainFilters`, External-DNS will ignore it.

5. **Federated Identity Setup**  
   - If you’re getting token or identity errors, confirm your federated identity configuration (on the UAMI in Azure) matches the service account’s annotation and your cluster’s issuer URL.

## Wrapping Up 🎁

By combining **External-DNS** with **Azure Workload Identity** for your **Azure Private DNS** zones, you’ll have a secure, low-maintenance system for automatic DNS record management. No more storing service principal secrets, no more manual DNS updates—just a smooth, automated workflow.

### Key Takeaways**

- Azure Workload Identity = no secrets needed!  
- External-DNS automates DNS record lifecycle for your cluster.  
- Private DNS means internal-only resolution—ideal for microservices and closed environments.  

Give this setup a spin, and watch your DNS woes disappear! ✨

### Further Reading

- [External-DNS GitHub](https://github.com/kubernetes-sigs/external-dns)  
- [Azure Workload Identity Docs](https://azure.github.io/azure-workload-identity/docs/)  
- [Azure Private DNS Overview](https://docs.microsoft.com/azure/dns/private-dns-overview)

**Happy Automating** and may your internal DNS always resolve! 🎉

Happy Clustering ! 🌟
