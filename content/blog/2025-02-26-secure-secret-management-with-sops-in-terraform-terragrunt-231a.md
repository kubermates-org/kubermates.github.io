---
title: "🔐 Secure Secret Management with SOPS in Terraform & Terragrunt"
date: 2025-02-26T14:44:59+00:00
description: "When managing infrastructure as code (IaC), keeping secrets safe while still making them accessible..."
tags: ["cloud", "security", "azure", "kubernetes"]
draft: false
slug: "secure-secret-management-with-sops-in-terraform-terragrunt-231a"
devto_id: 2299242
devto_url: "https://dev.to/hkhelil/secure-secret-management-with-sops-in-terraform-terragrunt-231a"
---
When managing infrastructure as code (IaC), keeping secrets **safe** while still making them accessible to Terraform/Terragrunt is a challenge. Storing secrets in plaintext is a **security risk** 🚨—and that’s where **SOPS** (Secrets OPerationS) comes in!

In this guide, we’ll cover:

- ✅ How to use **SOPS** with **age** and **GPG**
- ✅ How to configure **SOPS with `sops.yaml`** for better management
- ✅ How to use **Terragrunt’s built-in SOPS decryption** (without `run_cmd`)
- ✅ A **GitHub Actions workflow** to securely use secrets in CI/CD

## 📌 Why Use SOPS?

SOPS is an open-source tool from Mozilla that lets you **encrypt and decrypt** secrets easily. It supports multiple encryption methods, including **GPG**, **AWS KMS**, **Azure Key Vault**, **Google Cloud KMS**, and **age**.

Here’s why it’s awesome:

- ✅ Keeps secrets encrypted in Git repositories
- ✅ Works with YAML, JSON, ENV files
- ✅ Has built-in support in **Terragrunt** (no extra scripting needed!)
- ✅ Integrates with **GitHub Actions**, **Kubernetes**, and **CI/CD pipelines**

Now, let’s see how to use **SOPS with `age` and GPG**, then configure it properly for **Terragrunt and GitHub Actions**.

## 🔑 Using SOPS with `age`

[Age](https://github.com/FiloSottile/age) is a modern, simple, and secure encryption tool. If you’re new to encryption, **age is a great alternative to GPG**.

### ✨ Step 1: Install `age` and `sops`

First, install `age` and `sops`:

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

If you open `secrets.yaml`, you'll see it's fully encrypted! 🛡️

To **decrypt**:

```sh
sops --decrypt secrets.yaml
```

## 🔧 Configuring `sops.yaml` for Better Management

Instead of specifying the encryption method manually every time, **SOPS supports a configuration file** (`.sops.yaml`). This makes it easier to manage secrets across teams.

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

## ⚙️ Using SOPS with Terragrunt’s Built-in Decryption

Terragrunt has **native support for SOPS**, meaning you don’t need to use `run_cmd()`. Instead, you can **directly reference encrypted files** in your `terragrunt.hcl`.

### ✨ Step 1: Encrypt the Secrets

Create `secrets.yaml`:

```yaml
aws_access_key: "AKIAxxxxxxxxxxxx"
aws_secret_key: "abcdefghijklmno1234567890"
```

Encrypt it:

```sh
sops --encrypt -i secrets.yaml
```

### ✨ Step 2: Use Terragrunt's Built-in SOPS Decryption

Modify `terragrunt.hcl`:

```hcl
locals {
  secrets = yamldecode(sops_decrypt_file("secrets.yaml"))
}

inputs = {
  aws_access_key = local.secrets.aws_access_key
  aws_secret_key = local.secrets.aws_secret_key
}
```

Now, when you run:

```sh
terragrunt apply
```

Terragrunt **automatically decrypts** `secrets.yaml` without requiring external scripts! 🚀

## 🤖 Using SOPS in GitHub Actions

When using GitHub Actions, we need to **decrypt secrets safely** without exposing them.

### ✨ Step 1: Store the `age` Private Key in GitHub Secrets

Go to **GitHub → Your Repo → Settings → Secrets and variables → Actions**, and add:

- `SOPS_AGE_KEY`: The **private key** from `~/.config/sops/age/keys.txt`

### ✨ Step 2: Use SOPS in a GitHub Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy with Terraform & SOPS

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

      - name: Set up SOPS
        run: |
          mkdir -p ~/.config/sops/age/
          echo "${{ secrets.SOPS_AGE_KEY }}" > ~/.config/sops/age/keys.txt
          chmod 600 ~/.config/sops/age/keys.txt

      - name: Decrypt Secrets
        run: sops --decrypt secrets.yaml > secrets.decrypted.yaml

      - name: Deploy with Terraform
        run: |
          terragrunt run-all apply --auto-approve
```

### 🔥 What Happens in This Workflow?

1. **Checks out the code** ✅
2. **Installs SOPS & age** ✅
3. **Loads the age private key from GitHub Secrets** ✅
4. **Decrypts secrets** into a temporary file ✅
5. **Runs Terraform/Terragrunt** with the decrypted secrets ✅

**Security Tip:**
Make sure **secrets.decrypted.yaml** is ignored in `.gitignore` and is **never committed** to Git!

## 🎯 Wrapping Up

SOPS is a **powerful** and **secure** way to manage secrets for Terraform, Terragrunt, and GitHub Actions. With **age** encryption, `.sops.yaml` for better configuration, and **Terragrunt's built-in decryption**, managing secrets has never been easier! 💪

By integrating SOPS into your workflow, you get:

- ✅ **Encrypted secrets** in Git repositories
- ✅ **Easy decryption** in Terraform/Terragrunt
- ✅ **Safe usage of secrets in CI/CD**

Want to take it a step further? Try using **AWS KMS, GCP KMS, or Azure Key Vault** instead of age/GPG for even tighter security! 🔐🚀

Have questions or suggestions? Drop them in the comments! 💬

Happy clustering and stay safe ! 🔐
