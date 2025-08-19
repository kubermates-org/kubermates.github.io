---
title: "🌐 Securing Kubernetes Secrets in AKS: Using Azure Key Vault with Managed and User Assigned Identities 🚀"
date: 2024-09-04T11:35:22+00:00
description: "Hello Kubernetes enthusiast! 👋 Let’s dive into a critical aspect of securing your applications..."
tags: ["kubernetes", "azure", "cloud", "security"]
draft: false
slug: "securing-kubernetes-secrets-in-aks-using-azure-key-vault-with-managed-and-user-assigned-identities-569k"
devto_id: 1982431
devto_url: "https://dev.to/hkhelil/securing-kubernetes-secrets-in-aks-using-azure-key-vault-with-managed-and-user-assigned-identities-569k"
---
Hello Kubernetes enthusiast! 👋 Let’s dive into a critical aspect of securing your applications running in Azure Kubernetes Service (AKS): managing secrets. While Kubernetes Secrets provide a way to manage sensitive information like passwords and API keys, they aren’t encrypted by default and can be vulnerable if not handled correctly. In this guide, we'll explore how to securely manage secrets by integrating Azure Key Vault with AKS using both **VM Managed Identities** and **User Assigned Identities**. Plus, we'll show you how to enable the Secret Store CSI Driver directly in AKS.

## Why Not Just Use Kubernetes Secrets? 🤔

Kubernetes Secrets are only base64-encoded, not encrypted. This means if someone gains access to your Kubernetes cluster or its etcd database, they could easily decode and retrieve your sensitive information. Therefore, it’s recommended to use an external secrets management service like [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview), which offers robust security features and integrates seamlessly with AKS.

## Step 1: Enabling the Secret Store CSI Driver in AKS 🛠️

Before diving into examples, let’s enable the Secret Store CSI Driver in AKS. Azure makes this integration straightforward by allowing you to enable the Secret Store CSI Driver directly on your AKS cluster.

### Enabling the Secret Store CSI Driver in AKS

1. **Enable the Azure Key Vault Provider for Secrets Store CSI Driver** during AKS cluster creation or by updating an existing cluster:

```bash
az aks update -n MyAKSCluster -g MyResourceGroup --enable-secret-store-csi-driver
```

This command enables the Secrets Store CSI Driver and installs the necessary components in your AKS cluster.

- Learn more about enabling the [Secrets Store CSI Driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver) in AKS.

2. **Verify Installation**:

After enabling the feature, you can verify the installation by checking the pods in the `kube-system` namespace:

```bash
kubectl get pods -n kube-system
```

You should see pods related to the CSI driver running.

## Method 1: Securing Secrets with Azure Key Vault Using VM Managed Identity 🔐

### Understanding VM Managed Identities 🤖

**VM Managed Identities** (also known as **System-Assigned Managed Identities**) are automatically created by Azure when you enable a managed identity on a virtual machine or an AKS cluster. This identity is tied to the lifecycle of the VM or AKS cluster, meaning it will be deleted if the resource is deleted. VM Managed Identities are convenient because they don’t require any manual management of credentials. Azure handles the authentication process automatically, which simplifies securing access to resources like Azure Key Vault.

- Learn more about [Managed Identities for Azure Resources](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview).

### Step 2: Set Up Azure Key Vault ☁️

Let’s start by creating an Azure Key Vault and adding a secret:

1. **Create an Azure Key Vault**:

```bash
az keyvault create --name MyKeyVault --resource-group MyResourceGroup --location eastus
```

Refer to the official documentation for [creating and managing Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal).

2. **Add Secrets to the Vault**:

```bash
az keyvault secret set --vault-name MyKeyVault --name MySecret --value "SuperSecretValue"
```

More details on [storing and retrieving secrets](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal) in Azure Key Vault.

### Step 3: Grant Access to the VM Managed Identity 🤖

1. **Assign the Managed Identity to the AKS Cluster**:

If your AKS cluster uses a **system-assigned identity**, this step may already be completed during cluster creation. However, if necessary, you can assign one:

```bash
az aks update -g MyResourceGroup -n MyAKSCluster --assign-identity
```

This command enables the AKS cluster to use a VM Managed Identity, which Azure automatically manages. The identity is used to authenticate and access resources like Azure Key Vault.

2. **Grant Access to Azure Key Vault**:

Next, give the AKS cluster's VM Managed Identity permission to read secrets from the Key Vault:

```bash
az keyvault set-policy -n MyKeyVault --secret-permissions get --spn <aks-identity-client-id>
```

Replace `<aks-identity-client-id>` with the client ID of your AKS cluster's system-assigned identity. This allows the AKS cluster to retrieve secrets from the Azure Key Vault using its managed identity.

### Step 4: Configure and Deploy to Kubernetes 🚀

1. **Create a SecretProviderClass for VM Managed Identity**:

Here’s how to configure the Secret Store CSI Driver to use the VM Managed Identity:

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: azure-keyvault-provider-vm
spec:
  provider: azure
  parameters:
    useVMManagedIdentity: "true"  # Enables VM Managed Identity
    keyvaultName: "MyKeyVault"
    objects: |
      array:
        - |
          objectName: MySecret
          objectType: secret
    tenantId: "<your-tenant-id>"
```

- **`useVMManagedIdentity: "true"`**: This tells the Secret Store CSI Driver to authenticate to Azure Key Vault using the AKS cluster’s VM Managed Identity.

- Learn more about [Secret Store CSI Driver](https://learn.microsoft.com/en-us/azure/aks/csi-secrets-store-driver) and how to configure it.

2. **Deploy Your Application**:

Update your pod spec to mount the secrets:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod-vm
spec:
  containers:
  - name: mycontainer
    image: nginx
    volumeMounts:
    - name: secrets-store-inline
      mountPath: "/mnt/secrets-store"
      readOnly: true
  volumes:
    - name: secrets-store-inline
      csi:
        driver: secrets-store.csi.k8s.io
        readOnly: true
        volumeAttributes:
          secretProviderClass: "azure-keyvault-provider-vm"
```

### Step 5: Access Your Secrets 🎉

Once deployed, your secret will be available in the mounted path within your container:

```bash
cat /mnt/secrets-store/MySecret
```

## Method 2: Securing Secrets with Azure Key Vault Using User Assigned Identity 🔐

### Understanding User Assigned Identities 🤔

**User Assigned Managed Identities** are identities created as standalone Azure resources. Unlike VM Managed Identities, these identities are not tied to any specific Azure resource and can be assigned to multiple resources, including VMs and AKS clusters. This gives you more control and flexibility, as you can create and manage identities independently of the lifecycle of any particular resource.

- Learn more about [User Assigned Managed Identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities).

### Step 2: Set Up Azure Key Vault ☁️

This step is similar to the first method:

1. **Create an Azure Key Vault**:

```bash
az keyvault create --name MyKeyVault --resource-group MyResourceGroup --location eastus
```

Refer to the official documentation for [creating and managing Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal).

2. **Add Secrets to the Vault**:

```bash
az keyvault secret set --vault-name MyKeyVault --name MySecret --value "SuperSecretValue"
```

More details on [storing and retrieving secrets](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal) in Azure Key Vault.

### Step 3: Set Up a User Assigned Managed Identity 🔧

1. **Create a User Assigned Identity**:

Create a User Assigned Identity to attach to the AKS cluster:

```bash
az identity create --resource-group MyResourceGroup --name MyUserAssignedIdentity
```

Note the resource ID and client ID of this identity.

- Learn how to [create a User Assigned Managed Identity](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-manage-user-assigned-managed-identities).

2. **Grant Access to the User Assigned Identity**:

Next, grant the User Assigned Identity access to the Key Vault:

```bash
az keyvault set-policy -n MyKeyVault --secret-permissions get --spn <user-assigned-client-id>
```

Replace `<user-assigned-client-id>` with the client ID of the User Assigned Identity. This enables the identity to access secrets in the Azure Key Vault.

3. **Assign the Identity to AKS Cluster**:

Attach the User Assigned Identity to your AKS cluster:

```bash
az aks update -g MyResourceGroup -n MyAKSCluster --assign-identity <user-assigned-identity-id>
```

Replace `<user-assigned-identity-id>` with the resource ID of the User Assigned Identity. This allows the AKS cluster to authenticate using the User Assigned Identity.

- Learn more about [assigning managed identities to Azure resources](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-assign-access-azure-resource).

### Step 4: Configure and Deploy to Kubernetes 🚀

1. **Create a SecretProviderClass for User Assigned Identity**:

Unlike in Method 1, we will disable the use of VM Managed Identities and configure the Secret Store CSI Driver to use the User Assigned Identity instead:

```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: azure-keyvault-provider-user
spec:
  provider: azure
  parameters:
    useVMManagedIdentity: "false"  # Disables VM Managed Identity
    userAssignedIdentityID: "<user-assigned-client-id>"  # Specifies the User Assigned Identity
    keyvaultName: "MyKeyVault"
    objects: |
      array:
        - |
          objectName: MySecret
          objectType: secret
    tenantId: "<your-tenant-id>"
```

- **`useVMManagedIdentity: "false"`**: This disables the use of VM Managed Identity.
- **`userAssignedIdentityID: "<user-assigned-client-id>"`**: Specifies the User Assigned Identity that will authenticate with Azure Key Vault.

2. **Deploy Your Application**:

Update your pod spec as follows:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod-user
spec:
  containers:
  - name: mycontainer
    image: nginx
    volumeMounts:
    - name: secrets-store-inline
      mountPath: "/mnt/secrets-store"
      readOnly: true
  volumes:
    - name: secrets-store-inline
      csi:
        driver: secrets-store.csi.k8s.io
        readOnly: true
        volumeAttributes:
          secretProviderClass: "azure-keyvault-provider-user"
```

### Step 5: Access Your Secrets 🎉

Access the mounted secret in your container as shown:

```bash
cat /mnt/secrets-store/MySecret
```

## Wrapping It Up 🎁

By leveraging Azure Key Vault and the Secret Store CSI Driver in AKS, you can significantly improve the security of your Kubernetes Secrets. Whether you use **VM Managed Identities** or **User Assigned Identities**, you ensure that sensitive information is securely managed and accessed without directly storing credentials in your cluster.

- **VM Managed Identities** are ideal for scenarios where you want the simplicity of automatic identity management tied to your AKS cluster's lifecycle.
- **User Assigned Identities** provide greater control and flexibility, allowing you to manage and share identities across multiple resources.

By enabling the Secret Store CSI Driver in AKS, you make the integration process smoother and more secure, allowing your applications to seamlessly access secrets from Azure Key Vault. This approach not only simplifies secret management but also strengthens your security posture, reducing the risk of credential exposure.

Happy clustering, and keep those secrets safe! 🚀🔐
