---
title: "🚀 Enhancing Container Security: The Complete Guide to Secure and Clean Kubernetes Clusters 🛡️🧼"
date: 2024-09-11T07:19:50+00:00
description: "As Kubernetes continues to grow in popularity, ensuring the security and cleanliness of your..."
tags: ["kubernetes", "cloud", "azure", "security"]
draft: false
slug: "enhancing-container-security-the-complete-guide-to-secure-and-clean-kubernetes-clusters-1ida"
devto_id: 1996375
devto_url: "https://dev.to/hkhelil/enhancing-container-security-the-complete-guide-to-secure-and-clean-kubernetes-clusters-1ida"
---
As Kubernetes continues to grow in popularity, ensuring the security and cleanliness of your container images is crucial. In this guide, we’ll cover two key strategies: **image signing using Notary** 🖋️ and the **AKS Image Cleaner (Eraser)** add-on 🧼. Together, they form a robust, secure, and efficient container management workflow.

By the end, you'll know how to ensure that your AKS cluster pulls only verified, trusted images and stays free of unused images that could pose a risk to your environment.

## Why You Shouldn’t Rely on `IfNotPresent` Image Pull Policy 🤔

Kubernetes offers three main image pull policies:

1. `Always`
2. `IfNotPresent`
3. `Never`

While `IfNotPresent` might save bandwidth by using cached images already on the node, it comes with some serious security risks:

1. **Stale Images**: Cached images may become outdated and miss critical security patches.
2. **Compromised Images**: If an image in the local cache has been tampered with, Kubernetes won’t re-verify it, potentially running an unsafe version.
3. **Unverified Changes**: If images are modified or become corrupt locally, Kubernetes won’t detect these changes and will continue running them.

To maintain security, especially in production environments, it’s best to avoid `IfNotPresent` and ensure Kubernetes pulls the latest, signed images by setting the image pull policy to `Always`.

## What Is Image Signing with Notary? 🔐

Image signing ensures that the images running in your Kubernetes clusters come from a **trusted source** and haven’t been tampered with. **Notary** provides a way to cryptographically sign your container images, creating a verifiable chain of trust between your registry and Kubernetes.

### **Why is this important?**
- It ensures that only trusted images are deployed.
- It guarantees that images are unmodified after being signed.
- It prevents supply chain attacks and enhances security.

📘 **Learn more about Notary** in the [official documentation](https://github.com/notaryproject/notary).

## How to Use Notary in Kubernetes 🔧

### Example 1: Signing and Pulling Images with `crictl`

When pushing images to your container registry, it’s crucial to sign them using Notary. Here's a step-by-step guide on how to sign and verify images using `crictl` and Notary:

1. **Pull the Image**: First, pull the image you want to sign.
   ```bash
   crictl pull <your-registry>/<image>:<tag>
   ```

2. **Sign the Image**: Now, sign the image using Notary.
   ```bash
   notary addsign <your-registry>/<image>:<tag>
   ```

3. **Verify Image Signature**: Before deploying, ensure the image is verified.
   ```bash
   notary verify <your-registry>/<image>:<tag>
   ```

This process ensures that the image being pulled into your cluster is signed and secure.

### Example 2: Enforcing Image Signatures with Kubernetes Admission Controllers

You can further enhance security by configuring **Kubernetes admission controllers** to enforce policies that only allow signed images to be deployed.

Using **Kyverno**, you can set up a policy that requires signed images:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-signed-images
spec:
  rules:
    - name: verify-image-signature
      match:
        resources:
          kinds:
            - Pod
      verifyImages:
        - image: "your-registry.io/*"
          key: "your-public-key.pem"
```

This policy ensures that only images signed with your trusted key are allowed in the cluster. If an unsigned or tampered image is pulled, it will be rejected.

📘 **Explore Kyverno’s full documentation** [here](https://kyverno.io/docs/).

## AKS Image Cleaner (Eraser): Keeping Nodes Clean and Secure 🧼

Over time, nodes in AKS can accumulate unused images, which take up space and potentially introduce security risks. The **AKS Image Cleaner (Eraser)** helps solve this problem by automatically identifying and removing images that are no longer in use.

Here’s how it works:
- **Automatic Cleanup**: The Image Cleaner periodically scans nodes to find unused container images and removes them.
- **Free Up Disk Space**: This ensures that nodes remain lightweight and optimized for performance.
- **Reduced Security Risk**: Old, vulnerable images are removed, preventing them from being accidentally redeployed.

## How to Provision AKS with the Image Cleaner Add-On 🛠️

You can enable the **Image Cleaner** add-on during AKS cluster creation, automating the cleanup of unused container images and ensuring a tidy node environment.

### Example: Provisioning AKS with Image Cleaner Add-On

**Create an AKS Cluster with Image Cleaner**: Use the `--enable-image-cleaner` flag during cluster creation to enable the Image Cleaner add-on.

```bash
az aks create \
  --resource-group <your-resource-group> \
  --name <your-cluster-name> \
  --enable-image-cleaner \
  --node-count 3 \
  --enable-managed-identity \
  --generate-ssh-keys
```

  This command creates an AKS cluster with the **Image Cleaner** add-on enabled, which will automatically remove unused images.

**Verify the Add-on**: Check if the Image Cleaner add-on is enabled using the following command:

```bash
az aks show --resource-group <your-resource-group> --name <your-cluster-name> --query "addonProfiles.imageCleaner"
```

📘 Learn more about **AKS Image Cleaner** in the [official documentation](https://learn.microsoft.com/en-us/azure/aks/image-cleaner).

## Putting It All Together: A Secure Workflow for Kubernetes 🔄

To create a secure and clean Kubernetes environment, follow this workflow:

1. **Sign All Images**: Use Notary to sign every image before pushing it to your registry, ensuring that only trusted, verified images are available.
2. **Avoid `IfNotPresent`**: Use the `Always` image pull policy in production environments to avoid relying on potentially stale cached images.
3. **Enforce Signed Image Policies**: Set up admission controllers like Kyverno to ensure only signed images can be deployed in your cluster.
4. **Enable AKS Image Cleaner**: Provision your AKS clusters with the Image Cleaner add-on to automatically remove unused images from nodes.
5. **Regularly Monitor**: Use the Azure CLI to monitor your AKS clusters and ensure that image signing and cleaning are working as expected.

## Conclusion 🎉

By combining **image signing with Notary** and using the **AKS Image Cleaner (Eraser)**, you can create a highly secure and efficient Kubernetes environment. Image signing ensures that only trusted, verified images are deployed, while Image Cleaner keeps your nodes free of unused images that could introduce security risks.

With these tools in place, you can focus on building and deploying your applications, confident that your container infrastructure is both secure and clean. 💪✨

Happy clustering ! 🧼
