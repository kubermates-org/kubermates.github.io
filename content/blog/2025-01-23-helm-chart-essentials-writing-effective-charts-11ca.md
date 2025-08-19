---
title: "Helm Chart Essentials & Writing Effective Charts 🚀"
date: 2025-01-23T10:50:53+00:00
description: "Helm charts are a powerful way to define, install, and upgrade Kubernetes applications. By packaging..."
draft: false
slug: "helm-chart-essentials-writing-effective-charts-11ca"
devto_id: 2235397
devto_url: "https://dev.to/hkhelil/helm-chart-essentials-writing-effective-charts-11ca"
---
Helm charts are a powerful way to define, install, and upgrade Kubernetes applications. By packaging all the Kubernetes manifests and parameters in a neat, reproducible format, Helm simplifies the deployment process for engineers and DevOps teams. In this article, we’ll explore some best practices for writing effective Helm charts, introduce the **Helm Schema plugin** for validation, show how to include tests to ensure reliability, discuss **helm-docs** for automated documentation generation, and share an additional resource for testing and linting. Let’s get started! 🎉

## 1. Getting Started with Helm Charts 🏁

### What Is Helm?

[Helm](https://helm.sh/) is a package manager for Kubernetes, similar to how apt/yum/brew work for operating systems. It helps you:

- **Package** your Kubernetes resources into self-contained units called *charts*.
- **Install** and **upgrade** your applications with version tracking.
- **Simplify** complex deployments by parameterizing configurations in YAML.

### Anatomy of a Helm Chart

A typical Helm chart includes the following structure:

```bash
my-awesome-chart/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── tests/
│       └── test-connection.yaml
└── charts/
```

- **Chart.yaml**: Contains metadata about your chart, like name and version.
- **values.yaml**: Holds the default values your chart will use unless overridden by the user.
- **templates/**: Contains Kubernetes manifests that get rendered using the values specified in `values.yaml`.
- **charts/**: A directory to hold other charts your chart depends on (sub-charts).
- **tests/**: A folder inside `templates/` where you can define chart tests.

## 2. Best Practices for Writing Effective Helm Charts 🏆

1. **Follow a Consistent Structure**  
   Keeping a clean chart directory structure helps others (and your future self) navigate easily.

2. **Version Management**  
   - Update `version` in `Chart.yaml` according to [SemVer principles](https://semver.org/).  
   - Keep your `appVersion` (in `Chart.yaml`) aligned with the application’s version it deploys.

3. **Leverage `values.yaml`**  
   - Store user-configurable defaults in `values.yaml`.  
   - Use clear naming to describe each parameter.

4. **Use Helpers and Templates**  
   - Create `_helpers.tpl` for small, reusable snippets (like labels or names).  
   - Standardize your resource naming (e.g., `{{ include "my-awesome-chart.fullname" . }}`).

5. **Document Everything**  
   - Add a `README.md` with usage instructions, examples, and default values.  
   - Provide context for each parameter in `values.yaml`.

Following these tips ensures your charts stay consistent, maintainable, and user-friendly. 🙌

## 3. Introducing the Helm Schema Plugin 📐

When you have multiple parameters and complex configurations, validating your `values.yaml` files becomes crucial. The **[Helm Schema plugin](https://github.com/dadav/helm-schema)** uses **JSON Schema** to validate your Helm chart values. This helps ensure that the values provided by end users conform to the expected data types, structures, and constraints.

### Installation & Usage

1. **Install the plugin**:

   ```bash
   helm plugin install https://github.com/dadav/helm-schema
   ```

2. **Add a `values.schema.json`**:
   In your chart’s root, create a file named `values.schema.json`. This file defines the schema of your values. For example:

   ```json
   {
     "$schema": "http://json-schema.org/draft-07/schema#",
     "type": "object",
     "properties": {
       "replicaCount": {
         "type": "integer",
         "minimum": 1
       },
       "image": {
         "type": "object",
         "properties": {
           "repository": {
             "type": "string"
           },
           "tag": {
             "type": "string"
           }
         },
         "required": ["repository"]
       }
     },
     "required": ["replicaCount", "image"]
   }
   ```

3. **Validate your values**:

   ```bash
   helm schema my-awesome-chart/values.schema.json -f values.yaml
   ```

   This will check if `values.yaml` meets the constraints defined in `values.schema.json`. If something is off (e.g., missing required keys, using a string instead of an integer), it will throw a validation error.

### Benefits of Using Helm Schema

- **Early Catch** 🐞: Validate charts before deploying to production, catching misconfiguration early.  
- **Clear Documentation** 💡: The JSON schema itself acts as documentation, helping end users understand required and optional fields.  
- **Better Collaboration** 🤝: With the schema enforced, teams can rest assured that values used in different environments adhere to the same rules.

## 4. Including Tests in Your Helm Charts ✅

Testing is critical to verify that your Kubernetes resources deploy and function as expected. Helm offers a straightforward way to define and run tests within your chart. These tests are essentially Kubernetes jobs/pods that run checks to ensure your application is responding as intended.

### How Helm Tests Work

1. **Create a Test File**: In your chart’s `templates/tests/` directory, create a file (e.g., `test-connection.yaml`).
2. **Add Test Annotations**: Include special annotations recognized by Helm:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: "{{ include "my-awesome-chart.fullname" . }}-test-connection"
     labels:
       {{- include "my-awesome-chart.labels" . | nindent 4 }}
     annotations:
       "helm.sh/hook": test
       "helm.sh/hook-delete-policy": before-hook-creation
   spec:
     containers:
       - name: test-connection
         image: busybox
         command: ['sh', '-c', 'echo "Running connection test..."; sleep 1; exit 0']
     restartPolicy: Never
   ```

   - **`helm.sh/hook`: `test`** tells Helm that this Pod is used for testing.  
   - **`helm.sh/hook-delete-policy`: `before-hook-creation`** cleans up old test pods before creating new ones.

3. **Run the Tests**:
   After installing or upgrading your chart, simply run:

   ```bash
   helm test my-awesome-chart-release
   ```

   Helm will execute the test pods, and if they all pass (i.e., containers exit with code `0`), your chart tests succeed! 🎉

### Writing Meaningful Tests

- **Functionality Tests**: Verify that your application can handle basic requests (e.g., `curl` the service endpoint).
- **Readiness Tests**: Check your application’s endpoints for readiness or health endpoints.
- **Configuration Tests**: If your chart has multiple configuration options, test them in ephemeral environments to ensure no regressions.

## 5. Auto-Generating Documentation with helm-docs 📝

Maintaining up-to-date documentation can be tricky as your chart evolves. That’s where **[helm-docs](https://github.com/norwoodj/helm-docs)** comes in. It automatically generates documentation for your Helm chart by reading metadata from your chart files (like `Chart.yaml` and `values.yaml`).

### Installing helm-docs

```bash
brew install norwoodj/tap/helm-docs
```

*(See the [helm-docs repo](https://github.com/norwoodj/helm-docs) for alternative installation methods.)*

### Using helm-docs

1. **Add a `README.md.gotmpl`**  
   Create a template for your documentation—usually named something like `README.md.gotmpl`. You can define sections for chart metadata, usage, and parameters. For example:

   ```gotmpl
   # {{ .Name }}

   {{ .Description }}

   ## Parameters
   | Name | Description | Value |
   ||-|-|
   {{- range .Values }}
   | {{ .Path }} | {{ .Description }} | {{ .Default | quote }} |
   {{- end }}
   ```

2. **Run helm-docs**  
   Navigate to your chart directory and run:

   ```bash
   helm-docs
   ```

   This command will parse your `values.yaml`, `Chart.yaml`, and any comments or metadata to generate a `README.md` file based on your template.

3. **Commit & Share**  
   Once `README.md` is generated, commit it to your repository. Now, anyone viewing your chart can see the current parameters, default values, and usage instructions at a glance.

### Benefits of helm-docs

- **Automatic Updates** ⏰: Whenever you update `values.yaml` or `Chart.yaml`, re-running `helm-docs` keeps your README in sync.  
- **Consistent Format** 📄: Enforces a uniform structure across multiple charts in your organization.  
- **Time Savings** ⏲️: Spend less time manually editing documentation and more time improving your charts!

## 6. Wrapping It Up 🎁

By following these guidelines:

1. **Structure** your charts consistently.  
2. **Leverage** the Helm Schema plugin to validate configurations using JSON Schema.  
3. **Include** tests to confirm your chart works as intended.  
4. **Auto-generate** documentation with helm-docs to keep docs current and accurate.

…you’ll have robust, maintainable, and user-friendly Helm charts. Whether you’re deploying a tiny microservice or a huge enterprise application, these best practices will help you ship fast and confidently. ⚡

### Additional Resources

- [Helm Official Docs](https://helm.sh/docs/)
- [Helm Schema Plugin](https://github.com/dadav/helm-schema)
- [helm-docs](https://github.com/norwoodj/helm-docs)
- **Further Reading:** [Ensuring Effective Helm Charts with Linting, Testing, and Diff Checks](https://dev.to/hkhelil/ensuring-effective-helm-charts-with-linting-testing-and-diff-checks-ni0)

If you have any questions or tips, feel free to share them in the comments below. Together, we can make Helm charts smoother to write, more reliable to deploy, and easier to maintain! 🥳

Happy Helming and clustering ! 🐳
