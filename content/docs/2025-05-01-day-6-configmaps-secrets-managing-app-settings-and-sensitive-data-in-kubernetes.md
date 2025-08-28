---
title: 'Day 6: ConfigMaps & Secrets — Managing App Settings and Sensitive Data in
  Kubernetes'
date: '2025-05-01T18:11:50+00:00'
tags:
- kodekloud
- kubernetes
source: KodeKloud Blog (Kubernetes)
external_url: https://kodekloud.com/blog/day-6-configmaps-and-secrets/
post_kind: link
draft: false
tldr: 'Let’s Begin With What You Might Know What’s a ConfigMap? What’s a Secret? Why
  Use Them? How It Works Example: Creating a ConfigMap Try It Yourself Real-World
  Analogy Quick Summary Coming Up. Exploring System Architecture for DevOps Engineers
  Why KubeCon India 2025 Meant More to KodeKloud Linux: List Disks Linux: "cat" Command
  Linux Made Easy for DevOps Beginners From CFP to Stage: Win Your Tech Talk Slot
  MCP Explained Simply: How AI Can Actually Do Things Now Still Not Job-Ready After
  Learning DevOps? What Is Kubernetes? Finally, a Simple Explanation! 😬 But in Kubernetes,
  there’s a better and safer way to do this.'
summary: 'Let’s Begin With What You Might Know What’s a ConfigMap? What’s a Secret?
  Why Use Them? How It Works Example: Creating a ConfigMap Try It Yourself Real-World
  Analogy Quick Summary Coming Up. Exploring System Architecture for DevOps Engineers
  Why KubeCon India 2025 Meant More to KodeKloud Linux: List Disks Linux: "cat" Command
  Linux Made Easy for DevOps Beginners From CFP to Stage: Win Your Tech Talk Slot
  MCP Explained Simply: How AI Can Actually Do Things Now Still Not Job-Ready After
  Learning DevOps? What Is Kubernetes? Finally, a Simple Explanation! 😬 But in Kubernetes,
  there’s a better and safer way to do this. Enter: ConfigMaps and Secrets Environment
  variables App settings File paths Feature flags It keeps your app configs separate
  from your app code and container image — which is great for flexibility and security.
  Passwords API tokens TLS certificates Private keys Secrets are base64-encoded and
  can be managed with tighter access controls in Kubernetes. You: Create a ConfigMap
  or Secret Attach it to your Pod using: Environment variables Mounted volumes Environment
  variables Mounted volumes Your app reads the values from the injected location kubectl
  create configmap app-config \ --from-literal=APP_ENV=production \ --from-literal=FEATURE_X=true
  kubectl create configmap app-config \ --from-literal=APP_ENV=production \ --from-literal=FEATURE_X=true
  And a Secret: kubectl create secret generic db-secret \ --from-literal=DB_USER=admin
  \ --from-literal=DB_PASS=1234 kubectl create secret generic db-secret \ --from-literal=DB_USER=admin
  \ --from-literal=DB_PASS=1234 Then, in your Pod spec (simplified YAML): env: - name:
  APP_ENV valueFrom: configMapKeyRef: name: app-config key: APP_ENV - name: DB_USER
  valueFrom: secretKeyRef: name: db-secret key: DB_USER env: - name: APP_ENV valueFrom:
  configMapKeyRef: name: app-config key: APP_ENV - name: DB_USER valueFrom: secretKeyRef:
  name: db-secret key: DB_USER 👉 Use the KodeKloud Kubernetes Playground 1 - Create
  a Secret: kubectl create secret generic mysecret \ --from-literal=password=mypass123
  kubectl create secret generic mysecret \ --from-literal=password=mypass123 2 - Create
  a Pod using that secret: apiVersion: v1 kind: Pod metadata: name: secret-demo spec:
  containers: - name: busybox image: busybox command: ["sleep", "3600"] env: - name:
  DB_PASSWORD valueFrom: secretKeyRef: name: mysecret key: password apiVersion: v1
  kind: Pod metadata: name: secret-demo spec: containers: - name: busybox image: busybox
  command: ["sleep", "3600"] env: - name: DB_PASSWORD valueFrom: secretKeyRef: name:
  mysecret key: password Apply it with: kubectl apply -f pod. yaml kubectl exec -it
  secret-demo -- printenv DB_PASSWORD kubectl apply -f pod. yaml kubectl exec -it
  secret-demo -- printenv DB_PASSWORD You’ll see the password securely injected. Imagine
  you’re deploying an app on a shared team server. Hardcoding passwords in the app
  = leaving your house key in plain sight Using ConfigMaps and Secrets = storing your
  keys in a locked drawer with access logs ConfigMaps store general config data (non-sensitive)
  Secrets store sensitive info (passwords, tokens) Both can be injected into Pods
  via env vars or mounted files They help decouple config from code , enable reuse,
  and improve security 📅 Day 7: Your Kubernetes Learning Roadmap — What’s Next After
  the Basics? You’ll get: A printable roadmap for beginners → advanced Tips on real-world
  practice Recommended projects, labs, and courses to continue your journey New here?
  Start from Day 1 and catch up on the series: Day 1: What Is Kubernetes & Why Should
  You Care? Discover why Kubernetes matters and how it changes the game. Day 2: What
  Are Pods in Kubernetes? Understand the smallest deployable unit in Kubernetes. Day
  3: Understanding Nodes, Clusters & the Kubernetes Control Plane See how all the
  pieces connect behind the scenes. Day 4: Deployments & ReplicaSets — How Kubernetes
  Runs and Manages Your App ⚙Learn how Kubernetes keeps your apps running smoothly.'
---
Open the original post ↗ https://kodekloud.com/blog/day-6-configmaps-and-secrets/
