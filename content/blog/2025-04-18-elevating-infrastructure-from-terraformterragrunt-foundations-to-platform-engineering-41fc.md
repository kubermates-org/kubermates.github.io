---
title: "🚀🌐 Elevating Infrastructure: From Terraform/Terragrunt Foundations to Platform Engineering 😊"
date: 2025-04-18T10:24:24+00:00
description: "Hey there, cloud adventurers! 🚀 Let’s chat about why keeping Terraform (or OpenTofu) and Terragrunt..."
tags: ["cloud", "terraform", "cloudnative", "terragrunt"]
draft: false
slug: "elevating-infrastructure-from-terraformterragrunt-foundations-to-platform-engineering-41fc"
devto_id: 2415993
devto_url: "https://dev.to/hkhelil/elevating-infrastructure-from-terraformterragrunt-foundations-to-platform-engineering-41fc"
---
Hey there, cloud adventurers! 🚀 Let’s chat about why keeping **Terraform** (or **OpenTofu**) and **Terragrunt** in their own lanes is absolutely essential—and how using **Terraform JSON tfvars** makes life easier when you’re building nifty tools on top. Ready? Let’s dive in! 😄

### Why Separation Is a Must, Not an Option 🙅‍♂️🙅‍♀️

It might be tempting to mix Terraform and Terragrunt into one big file—after all, they work together, right? But trust me, keeping them decoupled is a game‑changer:

- **🔒 Clear boundaries**: Terraform focuses purely on _resource definitions_, while Terragrunt handles _orchestration_, remote state, and DRY patterns.  
- **🔄 Independent versioning**: You can upgrade your Terraform (or OpenTofu) modules (semantic versioning FTW!) without touching your Terragrunt configs—and vice versa!  
- **📦 Reusability everywhere**: Modules stay generic and shareable across projects when they don’t carry Terragrunt baggage.

By giving each tool its own space, you simplify CI/CD, make upgrades safer, and keep responsibilities crystal‑clear. Win‑win! 🏆

### Module Versioning with Terraform 🎯

Hosting Terraform (or OpenTofu) modules in a versioned repo (GitHub, GitLab, private registry—you choose!) lets you tag releases like `v1.2.3`. Then, Terragrunt can lock to that exact version:

```hcl
// modules/storage-account/main.tf
resource "azurerm_storage_account" "sa" {
  name                     = var.account_name
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

variable "account_name" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}

// modules/storage-account/versions.tf
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.0"
    }
  }
  required_version = ">= 1.5"
}
```

Publishing this as, say,  

```hcl
git::ssh://git@github.com/myorg/terraform-modules-repo.git//storage-account?ref=v1.0.0
```  

means everyone downstream knows exactly what they’re getting—no surprises! 🎉

### Decoupling Terraform (or OpenTofu) & Terragrunt 🛠️

For true decoupling, **host your Terraform/OpenTofu modules in a separate Git repository**, each with its own lifecycle, version tags, and release process. Then reference those modules from Terragrunt using Git sources. This keeps module development and environment orchestration fully independent.

**Example Terragrunt config:**

```hcl
# live/dev/terragrunt.hcl
terraform {
  source = "git::ssh://git@github.com/myorg/terraform-modules-repo.git//storage-account?ref=v1.0.0"
}

inputs = jsondecode(file("${get_terragrunt_dir()}/variables.tfvars.json"))
```

- The modules repository evolves on its own schedule.  
- Terragrunt configs in `live/` reference specific module versions via Git source.

This pattern prevents accidental cross‑pollination of concerns, making upgrades, reviews, and rollbacks a breeze. ✨

### Why Terraform JSON `tfvars` Rocks 📑✨

Sure, HCL is human‑friendly, but **JSON tfvars** shine when you need to build tools:

1. **🤖 Machine‑readable**: Every language can parse JSON out of the box—no extra libraries needed!  
2. **✔️ Schema validation**: Hook up a JSON Schema to catch mistakes before you even hit “apply.”  
3. **💡 Dynamic generation**: Your self‑service portal or CLI can spin out a JSON file in milliseconds.

**Example `variables.tfvars.json`:**

```json
{
  "account_name": "myappstorage-${env}",
  "resource_group_name": "rg-${env}",
  "location": "eastus",
  "tags": {
    "environment": "dev",
    "owner": "platform-team"
  }
}
```

And Terragrunt gobbles it up with:

```hcl
# live/dev/terragrunt.hcl
terraform {
  source = "git::ssh://git@github.com/myorg/terraform-modules-repo.git//storage-account?ref=v1.0.0"
}

inputs = jsondecode(file("${get_terragrunt_dir()}/variables.tfvars.json"))
```

See how clean that is? 🥳

### Building Your Own Abstraction Tools 🧰

Looking to give your team a self‑service experience? Here are two solid approaches:

**1. CLI with Go & Cobra ⚙️**  

- **Fast scaffolding**: Cobra generates a project structure with commands, subcommands, and flag parsing out of the box.  
- **Type safety & performance**: Go’s static typing ensures reliable flag handling, and compiled binaries run blazingly fast.  
- **Plugin architecture**: Easily hook in custom modules—for example, a command like `infra gen` that generates Terraform JSON tfvars files for your Terragrunt inputs.  
- **Example snippet:**

  ```go
  package main
  
  import (
    "encoding/json"
    "io/ioutil"
    "github.com/spf13/cobra"
  )
  
  var (
    accountName       string
    resourceGroupName string
    location          string
    env               string
    owner             string
    varsFile          string
  )
  
  var rootCmd = &cobra.Command{
    Use:   "infra",
    Short: "Self-service infra CLI",
  }
  
  var genCmd = &cobra.Command{
    Use:   "gen",
    Short: "Generate Terraform tfvars JSON file",
    RunE: func(cmd *cobra.Command, args []string) error {
      config := map[string]interface{}{
        "account_name":        accountName,
        "resource_group_name": resourceGroupName,
        "location":            location,
        "tags": map[string]string{
          "environment": env,
          "owner":       owner,
        },
      }
      data, err := json.MarshalIndent(config, "", "  ")
      if err != nil {
        return err
      }
      return ioutil.WriteFile(varsFile, data, 0644)
    },
  }
  
  func init() {
    genCmd.Flags().StringVar(&accountName, "account-name", "", "Azure storage account name")
    genCmd.Flags().StringVar(&resourceGroupName, "resource-group", "", "Resource group name")
    genCmd.Flags().StringVar(&location, "location", "eastus", "Azure location")
    genCmd.Flags().StringVar(&env, "env", "dev", "Deployment environment")
    genCmd.Flags().StringVar(&owner, "owner", "platform-team", "Resource owner")
    genCmd.Flags().StringVar(&varsFile, "out", "variables.tfvars.json", "Output JSON tfvars file")
    rootCmd.AddCommand(genCmd)
  }
  ```

**2. Self‑service portal with Backstage 🎭**  

- **Unified developer portal**: Backstage by Spotify lets you surface docs, tooling, and pipelines in one UI.  
- **Infrastructure as Code plugin**: Create a custom Backstage plugin to list available Terraform/OpenTofu modules and trigger Terragrunt runs with JSON inputs.  
- **Policy & approval workflows**: Integrate with existing Identity/Access tools and GitOps pipelines for reviews before provisioning.  
- **Rich catalog**: Use Backstage’s software catalog to track module versions, show metadata (owner, tags, docs), and link to Git repos.

Combine these approaches with strict Terraform/Terragrunt separation and JSON tfvars, and you’ll empower your team with both CLI efficiency and a polished web portal.

### Wrapping Up 🎁

Separating Terraform (or OpenTofu) modules from Terragrunt configs isn’t just a “nice to have”—it’s _essential_ for maintainable, scalable infrastructure. Pair that with JSON tfvars, and you’re set to build amazing tooling that your whole team will love. Happy provisioning! 🌟
