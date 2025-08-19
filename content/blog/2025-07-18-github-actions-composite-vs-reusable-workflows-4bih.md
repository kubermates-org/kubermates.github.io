---
title: "🧩 GitHub Actions Composite vs Reusable Workflows"
date: 2025-07-18T08:41:53+00:00
description: How to standardize and supercharge your CI/CD pipelines across projects   When your teams...
tags: ["githubactions", "github", "cicd", "automation"]
draft: false
slug: "github-actions-composite-vs-reusable-workflows-4bih"
devto_id: 2702461
devto_url: "https://dev.to/hkhelil/github-actions-composite-vs-reusable-workflows-4bih"
---
## How to standardize and supercharge your CI/CD pipelines across projects

When your teams manage multiple projects with similar deployment patterns, repeating the same GitHub Actions steps over and over can become tedious, error-prone, and hard to maintain

Thankfully, GitHub Actions offers two powerful solutions to help **standardize, reuse, and scale your CI/CD pipelines**: **Composite Actions** and **Reusable Workflows**. When used together, they form a clean, modular, and DRY (don’t repeat yourself) CI/CD strategy

## 🔄 Composite Actions vs Reusable Workflows

### 🧱 Composite Actions

Composite Actions allow you to group steps (like `docker build`, `terraform plan`, or `trivy scan`) into a reusable component. Think of it like a function.

**Best for:**

- Reusing logic (e.g., build and push images)
- Hiding complex logic from the main workflow
- Keeping workflows minimal and maintainable

Use it with:

```yaml
uses: ./.github/actions/your-action
```

### 🔁 Reusable Workflows

Reusable Workflows are full workflows that can be invoked with inputs and secrets.

**Best for:**

- High-level CI/CD orchestration (build, test, scan, deploy)
- Enforcing common practices across repositories
- Abstracting full pipelines

Use it with:

```yaml
uses: org/repo/.github/workflows/your-workflow.yml@ref
```

## 🐳 Example: Docker Build and Scan with Trivy

Here is an example of a **composite action** to build and push a Docker image to Azure Container Registry (ACR) and scan it using Trivy.

### `.github/actions/build-and-scan/action.yml`

```yaml
name: Docker Build and Push

inputs:
  dockerfile:
    default: Dockerfile
  context:
    default: .
  image_name:
    required: true
  tag:
    required: true
  build_args:
    default: ""
  report_name:
    default: trivy-report

runs:
  using: "composite"
  steps:
    - uses: azure/login@v2
      with:
        creds: ${{ env.AZURE_CREDENTIALS }}

    - uses: azure/docker-login@v2
      with:
        login-server: ${{ env.CONTAINER_REGISTRY }}
        username: ${{ env.ACR_USERNAME }}
        password: ${{ env.ACR_PASSWORD }}

    - name: Build and Push Image
      shell: bash
      run: |
        docker build ${{ inputs.build_args }} \
          -t ${{ env.CONTAINER_REGISTRY }}/${{ inputs.image_name }}:${{ inputs.tag }} \
          -f "${{ inputs.dockerfile }}" "${{ inputs.context }}"
        docker push ${{ env.CONTAINER_REGISTRY }}/${{ inputs.image_name }}:${{ inputs.tag }}

    - name: Scan with Trivy
      uses: aquasecurity/trivy-action@0.32.0
      with:
        image-ref: '${{ env.CONTAINER_REGISTRY }}/${{ inputs.image_name }}:${{ inputs.tag }}'
        format: 'sarif'
        output: 'trivy-results.sarif'
        exit-code: 0

    - name: Upload SARIF to GitHub Security tab
      uses: github/codeql-action/upload-sarif@v3
      with:
        sarif_file: 'trivy-results.sarif'
        category: trivy
```

### Usage in Workflow

```yaml
- name: Build and Scan
  uses: ./.github/actions/build-and-scan
  with:
    image_name: my-app
    tag: ${{ github.sha }}
```

## 🌍 Example: Terraform/Terragrunt Validation with Checkov

Now let’s see a **reusable workflow** to validate Terraform code and scan for misconfigurations using Checkov.

### `.github/workflows/infra-check.yml`

```yaml
name: Infra Validation Workflow

on:
  workflow_call:
    inputs:
      working_dir:
        required: true
        type: string

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Terragrunt and OpenTofu
        run: |
          curl -s https://raw.githubusercontent.com/opentofu/opentofu/main/scripts/install.sh | bash
          curl -L https://github.com/gruntwork-io/terragrunt/releases/latest/download/terragrunt_linux_amd64 -o terragrunt
          chmod +x terragrunt
          sudo mv terragrunt /usr/local/bin/

      - name: Validate HCL Syntax
        run: |
          terragrunt hclfmt --terragrunt-check --terragrunt-diff --recursive
        working-directory: ${{ inputs.working_dir }}

      - name: Check Misconfigurations with Checkov
        uses: bridgecrewio/checkov-action@v12
        with:
          directory: ${{ inputs.working_dir }}
          quiet: true
```

### Usage in Project Workflow

```yaml
jobs:
  call-validation:
    uses: your-org/your-repo/.github/workflows/infra-check.yml@main
    with:
      working_dir: infrastructure/staging/eu-west-1
```

## ⚙️ Best Practices

✅ Keep composite actions in `.github/actions`
✅ Keep reusable workflows in `.github/workflows`
✅ Abstract frequently repeated patterns
✅ Use inputs, outputs, and env vars to increase flexibility
✅ Use `workflow_call` and `workflow_dispatch` to structure triggers
✅ Defer secrets to the calling workflow

## 💡 Conclusion

Using **composite actions** and **reusable workflows** together can transform your CI/CD processes into clean, repeatable, and secure pipelines. Whether you're building containers, provisioning infrastructure, or scanning for vulnerabilities, this modular approach will scale with your teams and your systems.

Enjoy building better pipelines !
