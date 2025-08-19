---
title: "🚀 Building a Kubernetes Operator with an NGINX CRD"
date: 2024-08-29T08:25:36+00:00
description: "Kubernetes is a powerful platform that automates the deployment, scaling, and management of..."
tags: ["kubernetes", "cloud", "containers", "opensource"]
draft: false
slug: "building-a-kubernetes-operator-with-an-nginx-crd-3lil"
devto_id: 1963961
devto_url: "https://dev.to/hkhelil/building-a-kubernetes-operator-with-an-nginx-crd-3lil"
---
Kubernetes is a powerful platform that automates the deployment, scaling, and management of containerized applications. One of the coolest features of Kubernetes is its ability to be extended with **Custom Resource Definitions (CRDs)** and **Operators**. In this guide, we'll build a simple Kubernetes operator using an NGINX CRD to manage NGINX instances in your cluster.

### 🤖 Understanding Kubernetes Controllers, Operators, and CRDs

#### What is a Kubernetes Controller?

A Kubernetes controller is like a robot 🤖 that continuously monitors your cluster. It checks whether the actual state of the resources matches the desired state (what you want) and makes adjustments to align them.

**Kubernetes Operators** take this a step further. They use CRDs to define new resource types and handle the entire lifecycle of complex applications.

#### What is a Custom Resource Definition (CRD)?

A CRD allows you to define your own custom resources in Kubernetes. For instance, you can create an `Nginx` resource that specifies how you want NGINX to be deployed, and an operator will manage these resources for you.

### 🛠️ Core Components: Manager, Scheme, and Kinds

Before we dive into the code, here’s a quick overview of some key components:

- **Manager:** Handles the lifecycle of your operator's controllers and provides shared dependencies. 📚 [Learn more](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/manager)
- **Scheme:** Maps Kubernetes resource kinds (like `Pod` or `Service`) to their corresponding Go types. 📚 [Learn more](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Scheme)
- **Kinds:** These represent specific types of resources, such as `Pod`, `Deployment`, or in our case, `Nginx`. 📚 [Learn more](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/#understanding-kubernetes-objects)

### 🧑‍💻 A Simple NGINX Operator Example

Let’s build a Kubernetes operator that uses an `Nginx` CRD to manage NGINX instances.

#### Step 1: Define the Nginx CRD

First, define the custom resource. This CRD tells Kubernetes how to understand our custom `Nginx` objects.

Create a file named `nginx_crd.yaml`:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: nginxes.example.com
spec:
  group: example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                replicas:
                  type: integer
                image:
                  type: string
  scope: Namespaced
  names:
    plural: nginxes
    singular: nginx
    kind: Nginx
    shortNames:
    - ng
```

Apply this CRD to your cluster:

```bash
kubectl apply -f nginx_crd.yaml
```

#### Step 2: Import Required Packages

Now let’s write the Go code for our operator. Start by importing the necessary packages:

```go
package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"syscall"

	corev1 "k8s.io/api/core/v1"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/client-go/kubernetes/scheme"
	"k8s.io/client-go/rest"
	"sigs.k8s.io/controller-runtime/pkg/client"
	"sigs.k8s.io/controller-runtime/pkg/controller"
	"sigs.k8s.io/controller-runtime/pkg/manager"
	"sigs.k8s.io/controller-runtime/pkg/reconcile"
	"sigs.k8s.io/controller-runtime/pkg/runtime/signals"
	"sigs.k8s.io/controller-runtime/pkg/source"
	"sigs.k8s.io/controller-runtime/pkg/handler"
	"k8s.io/apimachinery/pkg/runtime/schema"
	"sigs.k8s.io/controller-runtime/pkg/client/config"
)

// Define the Nginx type
type Nginx struct {
	v1.TypeMeta   `json:",inline"`
	v1.ObjectMeta `json:"metadata,omitempty"`

	Spec NginxSpec `json:"spec,omitempty"`
}

type NginxSpec struct {
	Replicas int    `json:"replicas"`
	Image    string `json:"image"`
}

// Define the NginxList type
type NginxList struct {
	v1.TypeMeta `json:",inline"`
	v1.ListMeta `json:"metadata,omitempty"`
	Items       []Nginx `json:"items"`
}
```

#### Step 3: Initialize the Manager and Register the CRD

Next, create and initialize a `manager`, and register the custom `Nginx` resource with the manager's scheme.

```go
func main() {
	// Create a new Kubernetes client config
	cfg, err := config.GetConfig()
	if err != nil {
		fmt.Printf("Error creating config: %v\n", err)
		return
	}

	// Create a new manager to provide shared dependencies and start components
	mgr, err := manager.New(cfg, manager.Options{})
	if err != nil {
		fmt.Printf("Error creating manager: %v\n", err)
		return
	}

	// Register the Nginx type with the manager's scheme
	if err := addSchemes(mgr.GetScheme()); err != nil {
		fmt.Printf("Error adding schemes: %v\n", err)
		return
	}

	// Set up the controller
	if err := add(mgr); err != nil {
		fmt.Printf("Error setting up controller: %v\n", err)
		return
	}

	// Start the manager
	if err := mgr.Start(signals.SetupSignalHandler()); err != nil {
		fmt.Printf("Error starting manager: %v\n", err)
	}
}

func addSchemes(scheme *runtime.Scheme) error {
	gvk := schema.GroupVersion{Group: "example.com", Version: "v1"}
	scheme.AddKnownTypes(gvk, &Nginx{}, &NginxList{})
	v1.AddToGroupVersion(scheme, gvk)
	return nil
}
```

#### Step 4: Create the Reconcile Logic

Now we define the reconciliation logic. This logic ensures that for each `Nginx` custom resource, a corresponding NGINX pod is created and maintained.

```go
type ReconcileNginx struct {
	client client.Client
}

func (r *ReconcileNginx) Reconcile(ctx context.Context, request reconcile.Request) (reconcile.Result, error) {
	// Fetch the Nginx instance
	nginx := &Nginx{}
	err := r.client.Get(ctx, request.NamespacedName, nginx)
	if err != nil {
		if errors.IsNotFound(err) {
			// Nginx resource not found. Ignoring since it must have been deleted.
			return reconcile.Result{}, nil
		}
		// Error reading the object - requeue the request.
		return reconcile.Result{}, err
	}

	// Define the desired Nginx Pod object
	pod := &corev1.Pod{
		ObjectMeta: v1.ObjectMeta{
			Name:      nginx.Name + "-pod",
			Namespace: request.Namespace,
		},
		Spec: corev1.PodSpec{
			Containers: []corev1.Container{
				{
					Name:  "nginx",
					Image: nginx.Spec.Image,
				},
			},
		},
	}

	// Check if the Pod already exists
	found := &corev1.Pod{}
	err = r.client.Get(ctx, request.NamespacedName, found)
	if err != nil && errors.IsNotFound(err) {
		fmt.Printf("Creating a new NGINX Pod %s/%s\n", pod.Namespace, pod.Name)
		err = r.client.Create(ctx, pod)
		if err != nil {
			return reconcile.Result{}, err
		}
	} else if err != nil {
		return reconcile.Result{}, err
	}

	return reconcile.Result{}, nil
}
```

#### Step 5: Set Up the Controller

Finally, we set up the controller that will use the `ReconcileNginx` struct to manage NGINX instances based on the `Nginx` custom resource.

```go
func add(mgr manager.Manager) error {
	r := &ReconcileNginx{client: mgr.GetClient()}

	// Create a new controller
	c, err := controller.New("nginx-controller", mgr, controller.Options{Reconciler: r})
	if err != nil {
		return err
	}

	// Watch for changes to Nginx custom resources
	return c.Watch(&source.Kind{Type: &Nginx{}}, &handler.EnqueueRequestForObject{})
}
```

### 🔄 Object Lifecycle and Garbage Collection

One of the critical aspects of Kubernetes is how it handles the lifecycle of objects, ensuring that resources are created, updated, and deleted according to the desired state specified by the user or an operator.

#### Object Lifecycle

In Kubernetes, every resource has a lifecycle, including creation, updates, and deletion:

- **Creation**: When a new custom resource like `Nginx` is created, the operator’s controller is triggered to reconcile the resource by creating the corresponding NGINX pod.
- **Updates**: If the `Nginx` resource is updated (e.g., changing the image or replica count), the controller detects this and updates the corresponding resources to match the desired state.
- **Deletion**: When a custom resource is deleted, Kubernetes expects that the associated resources (like pods) will be cleaned up to prevent orphaned resources.

#### Garbage Collection in Controller Runtime

Controller-runtime, the library we use in this example, provides built-in support for managing the lifecycle of resources and performing garbage collection:

- **OwnerReferences**: One of the key features is the use of `OwnerReferences`. When a controller creates a resource (like a pod), it sets the custom resource (like `Nginx`) as the owner of the pod. This means that if the `Nginx` resource is deleted, Kubernetes automatically deletes the associated pod, ensuring that resources do not get orphaned.
  
- **Finalizers**: Finalizers are another mechanism to ensure that cleanup tasks are completed before a resource is fully deleted. For example, you can add a finalizer to the `Nginx` resource that ensures the associated pod is deleted before the `Nginx` resource itself is removed.

This automatic garbage collection helps keep your cluster clean and prevents resource leaks, making your operators more robust and reliable.

### 🚢 Building and Deploying the Operator

Now that the code is ready, let’s build and deploy your operator to the Kubernetes cluster.

#### Step 1: Build the Operator

1. Create a `Dockerfile`:

    ```Dockerfile
    FROM golang:1.23 as builder
    WORKDIR /workspace
    COPY . .
    RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -o nginx-operator main.go

    FROM alpine:3.20
    WORKDIR /
    COPY --from=builder /workspace/nginx-operator .
    ENTRYPOINT ["/nginx-operator"]
    ```

2. Build and push the Docker image:

    ```bash
    docker build -t your-docker-repo/nginx-operator:v1 .
    docker push your-docker-repo/nginx-operator:v1
    ```

#### Step 2: Deploy the Operator

Create a Kubernetes deployment to run your operator:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-operator
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      name: nginx-operator
  template:
    metadata:
      labels:
        name: nginx-operator
    spec:
      containers:
        - name: nginx-operator
          image: your-docker-repo/nginx-operator:v1
          imagePullPolicy: Always
```

Apply the deployment:

```bash
kubectl apply -f deployment.yaml
```

### 🧑‍🏭 Creating an Nginx Custom Resource

Now, let’s create an `Nginx` custom resource to deploy an NGINX instance:

```yaml
apiVersion: example.com/v1
kind: Nginx
metadata:
  name: my-nginx
spec:
  replicas: 1
  image: nginx:latest
```

Apply this resource:

```bash
kubectl apply -f my_nginx.yaml
```

Your operator will detect this custom resource and automatically create an NGINX pod in your cluster!

### 🎉 Conclusion

In this guide, we’ve walked through creating a Kubernetes operator using a Custom Resource Definition (CRD) to manage NGINX instances. You’ve learned how to define a CRD, implement a custom controller, and deploy it to a Kubernetes cluster.

We also discussed the lifecycle of objects in Kubernetes and how controller-runtime handles garbage collection automatically, ensuring that resources are managed efficiently and without leaving orphaned resources.

While this example gives you a solid foundation, in real-world scenarios, you’ll likely want to use tools like **Kubebuilder** or **Operator SDK**. These tools greatly simplify the development of Kubernetes operators by providing scaffolding, code generation, and built-in best practices, allowing you to focus more on the business logic of your operators rather than the boilerplate code.

For more advanced operator development, check out:
- [Kubebuilder](https://kubebuilder.io/)
- [Operator SDK](https://sdk.operatorframework.io/)

Happy clustering! 🚀
