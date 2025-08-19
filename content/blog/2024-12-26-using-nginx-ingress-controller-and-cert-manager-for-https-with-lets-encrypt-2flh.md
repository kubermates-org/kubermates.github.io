---
title: "Using Nginx Ingress Controller and Cert-Manager for HTTPS with Let’s Encrypt ⚡"
date: 2024-12-26T09:39:11+00:00
description: "Hey there! In today’s world, serving your web apps over HTTPS is a must. Luckily, combining the power..."
draft: false
slug: "using-nginx-ingress-controller-and-cert-manager-for-https-with-lets-encrypt-2flh"
devto_id: 2175477
devto_url: "https://dev.to/hkhelil/using-nginx-ingress-controller-and-cert-manager-for-https-with-lets-encrypt-2flh"
---
Hey there! In today’s world, serving your web apps over HTTPS is a must. Luckily, combining the power of **Nginx Ingress Controller** with **Cert-Manager** helps you easily request, issue, and renew TLS certificates from **Let’s Encrypt**. In this friendly guide, we’ll walk you through:

1. Installing the **Nginx Ingress Controller**  
2. Installing **Cert-Manager**  
3. Creating a **ClusterIssuer** to fetch certificates from Let’s Encrypt  
4. Configuring an example **Ingress** to serve traffic via HTTPS  

Let’s get started! 🚀

## Prerequisites

- **A running Kubernetes cluster** (any flavor you like—Minikube, managed cloud, etc.)  
- **kubectl** installed and configured to connect to your cluster  
- **A domain** you control, where you can edit DNS records to point to your cluster’s Ingress IP  

## Step 1: Install Nginx Ingress Controller

The Nginx Ingress Controller routes external requests to services in your cluster. One easy way to install is using Helm:

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx --create-namespace
```

After installation, confirm everything is up and running:

```bash
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
```

- If you see a **LoadBalancer** service, note its external IP. You’ll point your domain’s DNS record to that IP.  
- If using Minikube or a NodePort setup, you’ll need to retrieve the node IP or the port mapping.

## Step 2: Install Cert-Manager

Cert-Manager automates certificate lifecycle management. Again, Helm makes it simple:

```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update

helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager --create-namespace \
  --version v1.14.1 \
  --set installCRDs=true
```

You should see three pods in the `cert-manager` namespace:

- `cert-manager`  
- `cert-manager-cainjector`  
- `cert-manager-webhook`  

All should be in a **Running** state.

## Step 3: Create a ClusterIssuer for Let’s Encrypt

Next, create a **ClusterIssuer** to handle certificate requests for your entire cluster. Below is an example using Let’s Encrypt’s staging environment (less risk of rate-limit issues):

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-staging
spec:
  acme:
    server: https://acme-staging-v02.api.letsencrypt.org/directory
    email: youremail@example.com
    privateKeySecretRef:
      name: letsencrypt-staging-account-key
    solvers:
      - http01:
          ingress:
            class: nginx
```

Apply it:

```bash
kubectl apply -f letsencrypt-staging.yaml
```

Once you test successfully, switch to production by using `https://acme-v02.api.letsencrypt.org/directory` in the `server` field and a new secret name. For instance:

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-production
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: youremail@example.com
    privateKeySecretRef:
      name: letsencrypt-prod-account-key
    solvers:
      - http01:
          ingress:
            class: nginx
```

Apply it with:

```bash
kubectl apply -f letsencrypt-production.yaml
```

You’ll now have both a staging and a production ClusterIssuer.

## Step 4: Deploy an Example Application

Let’s deploy a simple “Hello World” app on Nginx:

```bash
kubectl create namespace demo
kubectl create deployment hello-world --image=nginx -n demo
kubectl expose deployment hello-world --port=80 --type=ClusterIP -n demo
```

This deployment and service will run your test web page on port 80 inside the `demo` namespace.

## Step 5: Create the Ingress Resource

Now let’s define an Ingress that:

1. Routes HTTP traffic from `example.com` to your `hello-world` service  
2. Requests a TLS certificate from Let’s Encrypt via Cert-Manager  
3. Forces HTTPS (using an Nginx annotation)

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-world-ingress
  namespace: demo
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-production"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - example.com
      secretName: hello-world-tls
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: hello-world
                port:
                  number: 80
```

Apply it:

```bash
kubectl apply -f hello-world-ingress.yaml
```

> **Replace** `example.com` with your actual domain.  

### Additional Example: Multiple Hosts

If you have multiple domains, you can define more `rules` and `tls` entries. For example:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-host-ingress
  namespace: demo
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-production"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - app1.example.com
      secretName: app1-tls
    - hosts:
        - app2.example.com
      secretName: app2-tls
  rules:
    - host: app1.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: hello-world
                port:
                  number: 80
    - host: app2.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: hello-world
                port:
                  number: 80
```

Each domain (`app1.example.com` and `app2.example.com`) will get its own certificate and secret.  

## Step 6: Update Your DNS

Point your domain (`example.com`) to the external IP of the Nginx Ingress Controller. This is typically done by creating or updating an **A record** in your DNS provider. If you have multiple hosts (like `app1.example.com`, `app2.example.com`), create A records for each one pointing to the same Ingress IP.

## Step 7: Verify

1. **Check the Ingress**:
   ```bash
   kubectl describe ingress hello-world-ingress -n demo
   ```
   Confirm the domain, service mapping, and annotations are correct.

2. **Check Cert-Manager logs**:
   ```bash
   kubectl logs -n cert-manager deploy/cert-manager
   ```
   Look for messages about the certificate being successfully issued.

3. **Test in the browser**:
   Visit `https://example.com`. If everything went smoothly, you’ll see the default Nginx page over a secure connection! 🔒

4. **Check the certificate**:
   In your browser, click the padlock icon or check dev tools to ensure it’s signed by Let’s Encrypt.

## Automatic Renewal

Cert-Manager handles certificate renewals automatically, so you won’t need to worry about expiring certificates. It checks each certificate’s expiration date and renews as needed, keeping your sites secure without any hassle. 🙌

## Troubleshooting Tips

- **HTTP challenge fails?**  
  Make sure DNS is pointing to your Ingress IP. If Let’s Encrypt can’t reach your domain, the challenge will fail.

- **Wrong Ingress class?**  
  Double-check `ingressClassName: nginx` (or whatever your Nginx Ingress Controller is using).

- **Rate limits**  
  Use staging mode (like `letsencrypt-staging`) for your initial tests to avoid hitting production rate limits. Switch to production only once you’ve verified everything.

- **Logs & events**  
  Check logs with:
  ```bash
  kubectl describe certificate <certificate-name>
  kubectl describe challenge <challenge-name>
  ```
  These commands can show detailed errors on why a certificate request might fail.

## Conclusion

Congrats! 🎉 You’ve successfully deployed **Nginx Ingress Controller** with **Cert-Manager** and **Let’s Encrypt** on your Kubernetes cluster. This setup not only secures traffic but also takes care of automatic certificate issuance and renewal—so you can focus on building awesome applications. 

Happy clustering ! ✨
