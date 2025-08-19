---
title: "🔐 Secure Secret Management with SOPS in Helm 🚀"
date: 2025-02-27T08:15:10+00:00
description: "When managing applications deployed on Kubernetes, keeping secrets safe while still making them..."
draft: false
slug: "secure-secret-management-with-sops-in-helm-1940"
devto_id: 2300501
devto_url: "https://dev.to/hkhelil/secure-secret-management-with-sops-in-helm-1940"
---
When managing applications deployed on Kubernetes, keeping secrets safe while still making them accessible to Helm charts is a challenge. Storing secrets in plaintext is a **security risk** 🚨 — and that’s where **SOPS** (Secrets OPerationS) and the **Helm Secrets plugin** come in!

In this guide, we’ll cover:

- ✅ How to use **SOPS** with **age** and **GPG**
- ✅ How to configure **SOPS with `sops.yaml`** for better management
- ✅ How to use **Helm Secrets Plugin** to manage encrypted secrets directly in your Helm charts
- ✅ A **GitHub Actions workflow** to securely deploy Helm charts using encrypted secrets

## 📌 Why Use SOPS with Helm?

SOPS is an open-source tool from Mozilla that lets you **encrypt and decrypt** secrets with ease. When combined with the Helm Secrets plugin, you can safely store your sensitive data in Git repositories and automatically decrypt them during Helm deployments. Here’s why it’s awesome:

- ✅ Keeps secrets encrypted in your repos  
- ✅ Works with YAML, JSON, and ENV files  
- ✅ Integrates seamlessly with Helm via the **Helm Secrets plugin**  
- ✅ Fits perfectly into CI/CD pipelines like **GitHub Actions** for secure deployments

## 🔑 Using SOPS with `age`

[Age](https://github.com/FiloSottile/age) is a modern, simple, and secure encryption tool. If you’re new to encryption, **age is a great alternative to GPG**.

### ✨ Step 1: Install `age` and `sops`

Install `age` and `sops`:

```sh
sudo apt install age    # Ubuntu/Debian
```

### ✨ Step 2: Generate an `age` Key

Run:

```sh
age-keygen -o ~/.config/sops/age/keys.txt
```

This will generate a key similar to:

```text
# public key: age1xxxxxxx
AGE-SECRET-KEY-1XXXXXXYYYYYYYYZZZZZZ
```

Copy the **public key** (`age1xxxxxxx`)—this will be used for encryption.

### ✨ Step 3: Encrypt a YAML File with SOPS

Create a file called `secrets.yaml`:

```yaml
db_user: "admin"
db_password: "supersecret"
```

Now, encrypt it using SOPS:

```sh
sops --encrypt --age age1xxxxxxx -i secrets.yaml
```

When you open `secrets.yaml`, you’ll see it’s fully encrypted! 🛡️

To **decrypt**:

```sh
sops --decrypt secrets.yaml
```

## 🔧 Configuring `sops.yaml` for Better Management

Instead of specifying the encryption method manually every time, SOPS supports a configuration file (`.sops.yaml`). This makes it easier to manage secrets across your team.

Create `.sops.yaml` in your repository:

```yaml
creation_rules:
  - path_regex: secrets/.*\.yaml$
    age:
      - age1xxxxxxx  # Replace with your public key
  - path_regex: secrets/.*\.json$
    pgp:
      - ABC12345  # Replace with your GPG key ID
```

Now, when encrypting secrets inside the `secrets/` folder, SOPS will **automatically** use the right encryption method! 🎉

Encrypt a new secret:

```sh
sops --encrypt -i secrets/app.yaml
```

## 🛠️ Using Helm with the Helm Secrets Plugin

The **Helm Secrets plugin** allows you to work with encrypted secrets directly in your Helm charts—no need to expose sensitive data!

### ✨ Step 1: Install the Helm Secrets Plugin

Install the plugin with:

```sh
helm plugin install https://github.com/jkroepke/helm-secrets
```

This plugin leverages SOPS to decrypt your secret files during Helm chart deployments.

### ✨ Step 2: Encrypt Your Secrets File

Create a file named `secrets.yaml` (if you haven’t already):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=          # base64 encoded
  password: c3VwZXJzZWNyZXQ=   # base64 encoded
```

Encrypt it using SOPS:

```sh
sops --encrypt -i secrets.yaml
```

### ✨ Step 3: Deploy with Helm Using Encrypted Secrets

Deploy your Helm chart using the encrypted secrets file:

```sh
helm secrets upgrade --install my-release ./my-chart
```

The Helm Secrets plugin will automatically decrypt `secrets.yaml` during the deployment process. 🚀

## 🤖 Using SOPS and Helm in GitHub Actions

Integrate your secure secrets management into your CI/CD pipeline with GitHub Actions. Here’s an example workflow that deploys your Helm chart with encrypted secrets:

### ✨ Step 1: Store the `age` Private Key in GitHub Secrets

In your GitHub repository, navigate to **Settings → Secrets and variables → Actions**, and add:

- `SOPS_AGE_KEY`: The **private key** from `~/.config/sops/age/keys.txt`

### ✨ Step 2: Create the GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy with Helm & SOPS

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y sops age
          curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
          helm plugin install https://github.com/jkroepke/helm-secrets

      - name: Set up SOPS
        run: |
          mkdir -p ~/.config/sops/age/
          echo "${{ secrets.SOPS_AGE_KEY }}" > ~/.config/sops/age/keys.txt
          chmod 600 ~/.config/sops/age/keys.txt

      - name: Deploy with Helm
        run: |
          helm secrets upgrade --install my-release ./my-chart
```

### 🔥 What Happens in This Workflow?

1. **Checks out the code** ✅  
2. **Installs SOPS, age, Helm, and the Helm Secrets plugin** ✅  
3. **Loads the age private key from GitHub Secrets** ✅  
4. **Deploys the Helm chart** with decrypted secrets on the fly ✅  

**Security Tip:**  
Make sure that any decrypted files are never committed to your repository! Always keep them out of version control. 🔒

## 🎯 Wrapping Up

SOPS and the Helm Secrets plugin offer a **powerful** and **secure** way to manage secrets in your Kubernetes deployments. With **age** encryption, a handy `.sops.yaml` configuration, and seamless integration via Helm, managing secrets has never been easier! 💪

By integrating these tools into your workflow, you get:

- ✅ **Encrypted secrets** safely stored in Git repositories  
- ✅ **Automatic decryption** during Helm deployments  
- ✅ **Secure usage** of secrets in CI/CD pipelines

Want to take it a step further? Try exploring **AWS KMS, GCP KMS, or Azure Key Vault** for even tighter security! 🔐🚀

Have questions or suggestions? Drop them in the comments! 💬

Happy clustering and stay safe! 🔐😊
