---
title: "Unlocking Secrets with External Secrets Operator 🔐✨"
date: 2025-01-03T20:00:01+00:00
description: "In modern cloud-native applications, securely managing sensitive data like API keys, database..."
draft: false
slug: "unlocking-secrets-with-external-secrets-operator-2f89"
devto_id: 2181529
devto_url: "https://dev.to/hkhelil/unlocking-secrets-with-external-secrets-operator-2f89"
---
In modern cloud-native applications, securely managing sensitive data like API keys, database credentials, and certificates is a top priority. Two powerful tools stand out when integrating secrets into Kubernetes: **External Secrets Operator** and **SecretStoreProviders plugin** (for Azure and AWS). Let’s dive into how to use them, their differences, and when to pick one over the other. 🚀

## **What Is External Secrets Operator?** 🤔

The **External Secrets Operator** (ESO) simplifies secret management in Kubernetes by integrating external secret stores directly into your cluster. Instead of manually creating Kubernetes Secrets, ESO syncs secrets from providers like AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault.

### **Why Use External Secrets Operator?** 🌟

- **Centralized Secret Management:** Manage secrets in your provider of choice while syncing them to Kubernetes.
- **Automation:** No need to manually update Kubernetes Secrets when values change.
- **Security:** Leverages providers' robust access control and encryption mechanisms.

## **How to Use External Secrets Operator** 🛠️

Here’s a quick guide to setting up ESO:

### **Step 1: Install External Secrets Operator**

Install ESO via Helm:

```bash
helm repo add external-secrets https://charts.external-secrets.io
helm repo update
helm install external-secrets external-secrets/external-secrets
```

### **Step 2: Configure a SecretStore**

Create a `SecretStore` resource to connect to your external provider. For example, if you're using AWS Secrets Manager:

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secret-store
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-west-2
```

For Azure Key Vault:

```yaml
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: azure-secret-store
spec:
  provider:
    azurekv:
      tenantId: <your-tenant-id>
      vaultUrl: https://<your-vault-name>.vault.azure.net/
```

### **Step 3: Define an ExternalSecret**

Bind your external secret to a Kubernetes Secret:

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: my-app-secret
spec:
  secretStoreRef:
    name: aws-secret-store
  target:
    name: my-k8s-secret
  data:
    - secretKey: apiKey
      remoteRef:
        key: /my-app/api-key
```

This example pulls the `/my-app/api-key` from AWS Secrets Manager and creates a Kubernetes Secret named `my-k8s-secret`.

For templating values:

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: my-template-secret
spec:
  secretStoreRef:
    name: azure-secret-store
  target:
    name: templated-secret
  data:
    - secretKey: connectionString
      remoteRef:
        key: /database/connection-string
  dataFrom:
    - extract: key-values
```

## **How Does It Compare to SecretStoreProviders Plugin?** ⚖️

Both ESO and the SecretStoreProviders plugin enable secure secret management in Kubernetes. Here’s how they stack up:

### **1. Scope and Features** 🌍

- **External Secrets Operator**:
  - Supports multiple providers (AWS, Azure, GCP, HashiCorp Vault, etc.).
  - Extensive customization and features like templating.
- **SecretStoreProviders Plugin**:
  - Focused primarily on Azure Key Vault and AWS Secrets Manager.
  - Limited to CSI driver-based integration.

### **2. Installation and Complexity** 🤹

- **ESO**: Requires deploying the operator and defining `SecretStore` and `ExternalSecret` resources. It’s slightly more complex but offers more flexibility.
- **SecretStoreProviders**: Simpler setup with a CSI driver. However, its capabilities are narrower.

### **3. Performance and Scalability** 🚀

- **ESO**: Handles more complex scenarios but may introduce slight overhead due to the operator’s reconciliation process.
- **SecretStoreProviders**: Lightweight but less feature-rich, making it better for straightforward use cases.

### **4. Provider Support** 🌐

- **ESO**: Supports a broad range of providers beyond AWS and Azure.
- **SecretStoreProviders**: Limited to Azure Key Vault and AWS Secrets Manager.

### **5. Example Use Cases**

- **ESO**:
  - Sync multiple secrets from AWS Secrets Manager and Azure Key Vault into a single Kubernetes namespace.
  - Templating and merging secrets from different sources into one Secret.
  - Using annotations to dynamically manage secret lifecycles.
- **SecretStoreProviders**:
  - Directly mount Azure Key Vault secrets as files in a pod.
  - Lightweight secret access for apps needing minimal Kubernetes API interaction.

## **How to Use SecretStoreProviders Plugin for Azure and AWS** 🔧

### **Azure Key Vault Example**

1. Install the Azure Key Vault CSI driver:

    ```bash
    kubectl apply -f https://raw.githubusercontent.com/Azure/secrets-store-csi-driver-provider-azure/main/deployment/secretproviderclass.yaml
    ```

2. Create a `SecretProviderClass` to define the secrets you want to access:

    ```yaml
    apiVersion: secrets-store.csi.x-k8s.io/v1
    kind: SecretProviderClass
    metadata:
    name: azure-keyvault
    spec:
    provider: azure
    parameters:
        usePodIdentity: "false"
        clientID: "<your-client-id>"
        tenantID: "<your-tenant-id>"
        keyvaultName: "<your-keyvault-name>"
        objects: |
        array:
            - |
            objectName: secret1
            objectType: secret
            - |
            objectName: certificate1
            objectType: cert
    ```

3. Mount the secrets in a pod:

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    name: nginx-secrets-store
    spec:
    containers:
        - name: nginx
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
            secretProviderClass: "azure-keyvault"
    ```

### **AWS Secrets Manager Example**

1. Install the AWS Secrets Manager CSI driver:

    ```bash
    kubectl apply -k "github.com/aws/secrets-store-csi-driver-provider-aws/deployment?ref=main"
    ```

2. Create a `SecretProviderClass` to define the secrets:

    ```yaml
    apiVersion: secrets-store.csi.x-k8s.io/v1
    kind: SecretProviderClass
    metadata:
    name: aws-secrets
    spec:
    provider: aws
    parameters:
        objects: |
        - objectName: "mySecret"
            objectType: "secretsmanager"
            region: "us-west-2"
    ```

3. Mount the secrets in a pod:

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    name: nginx-secrets-store
    spec:
    containers:
        - name: nginx
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
            secretProviderClass: "aws-secrets"
    ```

## **Which One Should You Choose?** 🤷‍♀️

### **Use External Secrets Operator if:**

- You need to work with multiple providers.
- Your use case involves advanced templating or secret transformation.
- Flexibility and extensibility are priorities.

### **Use SecretStoreProviders Plugin if:**

- You primarily work with Azure or AWS secrets.
- Simplicity and minimal resource usage are key.
- You prefer to use the Kubernetes CSI driver.

## **Conclusion** 🎉

Both **External Secrets Operator** and **SecretStoreProviders plugin** are excellent tools for managing secrets in Kubernetes. Your choice depends on your use case, complexity, and cloud provider preferences. With either option, you’ll be well-equipped to handle secrets securely in your Kubernetes clusters. 🔒

Happy Clustering! 🚀
