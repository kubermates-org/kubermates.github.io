---
title: 'Now Available: Remote MCP for DigitalOcean Services'
date: '2025-12-09T18:53:48.536000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/remote-mcp-server
post_kind: link
draft: false
tldr: 'Now Available: Remote MCP for DigitalOcean Services Why Remote MCP? Endpoint
  mapping: one MCP server per service Example Remote MCP configuration Local configuration
  (existing) Authentication and request model What’s next About the author(s) Try
  DigitalOcean for free Related Articles DigitalOcean MCP Server is now available
  Choosing the Right GPU Droplet for your AI/ML Workload By Bikram Gupta and Dinesh
  Murthy Published: December 9, 2025 5 min read Earlier this year, DigitalOcean introduced
  the DigitalOcean Model Context Protocol (MCP) Server , allowing developers to connect
  applications and AI-assistants like Cursor and Claude Desktop directly to their
  DigitalOcean cloud infrastructure. You could ask your AI assistant to deploy apps,
  check database status, or troubleshoot droplet issues – all conversationally, making
  your infrastructure “AI-readable”.'
summary: 'Now Available: Remote MCP for DigitalOcean Services Why Remote MCP? Endpoint
  mapping: one MCP server per service Example Remote MCP configuration Local configuration
  (existing) Authentication and request model What’s next About the author(s) Try
  DigitalOcean for free Related Articles DigitalOcean MCP Server is now available
  Choosing the Right GPU Droplet for your AI/ML Workload By Bikram Gupta and Dinesh
  Murthy Published: December 9, 2025 5 min read Earlier this year, DigitalOcean introduced
  the DigitalOcean Model Context Protocol (MCP) Server , allowing developers to connect
  applications and AI-assistants like Cursor and Claude Desktop directly to their
  DigitalOcean cloud infrastructure. You could ask your AI assistant to deploy apps,
  check database status, or troubleshoot droplet issues – all conversationally, making
  your infrastructure “AI-readable”. Until now, this required running the MCP server
  locally using the npx binary on your computer. Remote MCP support is now available
  on DigitalOcean. You can now connect your AI tools to DigitalOcean services without
  installing any binaries locally. Remote MCP endpoints are live for 9 DigitalOcean
  services: Accounts, App Platform, Databases, DigitalOcean Kubernetes, Droplets,
  Insights, Marketplace, Networking, and Spaces. Each service runs as its own MCP
  server at a dedicated HTTPS endpoint (example: https://apps. mcp. digitalocean.
  com/mcp for App Platform). Just update your MCP client configuration to point at
  our hosted endpoints, include your DigitalOcean API token and you’re ready to go
  with immediate, authenticated access to your infrastructure. All existing DigitalOcean
  MCP tutorials and videos continue to work.'
---
Open the original post ↗ https://www.digitalocean.com/blog/remote-mcp-server
